import re

"""
match函数语法
re.match 尝试从字符串的起始位置匹配一个模式
re.match(pattern, string, flags=0)
输入参数说明：
pattern---匹配的正则表达式
string---要匹配的字符串
flags---标志位，用于控制正则表达的匹配方式，
比如是否区分大小写，多行匹配等

返回参数说明：
re.match 尝试从字符串的起始位置匹配一个模式
如果起始位置匹配成功则返回matchObject（匹配对象）
如果不是起始位置匹配成功返回none
"""
s1 = 'www.python.org'
# 在起始位置匹配
# 返回的匹配对象拥有span属性，如果返回None
# 则没有span属性，调用span后返回一个二元素
# 元组，第一个表示在匹配字符串的开始位置，第二
# 个表示结束
print(re.match('www', s1).span())
# 不在起始位置匹配
# 不是起始位置匹配成功返回None，NoneType没有span属性
print(re.match('org', s1))


"""

"""
line = 'Cats are smarter than dogs'

m = re.match(r'(.*) are (.*?) .*', 
line, re.MULTILINE|re.IGNORECASE)

if m:
    print('matchObject.group():', m.group())
    print('matchObject.group(1):', m.group(1))
    print('matchObject.group(2):', m.group(2))
else:
    print('not match!')

"""
re.search扫描整个字符串并且返回第一个成功的
匹配
re.search(pattern, string, flags=0)
"""
print(re.search('www', 'www.python.org').span())
print(re.search('org', 'www.python.org').span())

search_obj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if search_obj:
    print(search_obj.group())
    print(search_obj.group(1))
    print(search_obj.group(2))
else:
    print('nothing found!')

"""
match和search的区别：
re.match只匹配字符串的开始，
如果字符串开始不符合正则表达式，
则匹配失败，函数返回None；
而re.search匹配整个字符串，
直到找到一个匹配
"""

"""
re.sub用于替换字符串中的匹配项
语法：
re.sub(pattern, rep1, string, count=0, flags=0)
输入参数说明：
其中rep1替换的字符串，可以为函数，可用lambda函数
count为模式匹配后替换的最大次数，默认为0替换所有匹配
返回参数说明：
如果检索不到，则返回None
如果检索了，返回替换后的string
"""
phone = '2004-959-559 # 这是一个国外电话号码'

# 删除字符串汇总的python注释
num_1 = re.sub(r'#.*$', '', phone)
print('now the phone is', num_1)

# 删除非数字-字符
num_2 = re.sub(r'\D', '', num_1)
print(num_2) 

print(phone)

# rep1可以是一个可调用对象
def doubleTheStr(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub(r'(?P<value>\d+)', doubleTheStr, s))

"""
compile函数用于编译正则表达式， 生成一个正则表达式
pattern对象，供match和search这两个函数使用
语法：
re.compile(pattern[, flags])
flags：可选，表示匹配模式，具体参数：
re.I---忽略大小写
re.L---表示特殊字符集\w等依赖于当前环境
re.M---多行模式
re.S---即为.，并且包括换行符在内的任意字符
re.U---表示特殊字符集依赖于Unicode字符属性数据库
re.X---为了增加可读性，忽略空格和#后面的注释
"""

pattern = re.compile(r'\d+') # 用于匹配至少一个数字
# 开始没有匹配，返回None
m = pattern.match('one12twothree34four')
print(m)
# 开始匹配到了，返回匹配的结果
m = pattern.match('12asdhaksdhasd')
print(m, m.group(), m.groups(), 
m.group(0), sep='\n')
# start和end属性
print(m.start(), m.end(), sep='\n')

# 从第三个位置开始操作，到第十个位置
m = pattern.match('one12twothree34four', pos=3, endpos=10)  
print(m.group(), m.span(), sep='\n')

"""
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group)
"""

p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = p.match('Hello World Wide Web') 
# 匹配成功，返回match对象
print(m)
# 返回匹配成功的整个子串
print(m.group(), m.group(0))  
# 返回匹配成功的整个子串的索引
print(m.span(), m.span(0))
# 返回第一个分组匹配成功的子串
print(m.group(1))
# 返回第一个分组匹配成功的子串的索引
print(m.span(1))
# 返回第二个分组匹配成功的子串
print(m.group(2))
# 返回第二个分组匹配成功的子串的索引
print(m.span(2))
# m.groups()等价于(m.group(1), m.group(2)...) 
print(m.groups(), (m.group(1), m.group(2)))
# 不存在第三个分组
try:
    m.group(3)
except Exception as err:
    print(err)

"""
re.findall
在字符串中找到正则表达式所匹配的所有子串
并返回一个由子串组成的列表，如果没有匹配的
则返回一个空列表
语法：
findall(string[, pos[, endpos]])
pos---可选参数，指定字符串的起始位置，默认为0
endpos---可选参数，指定字符串的结束位置，默认为字符串的长度
注意：match 和 search 是匹配一次 findall 匹配所有
"""
# 查找数字，贪婪匹配（greedy）和非贪婪匹配（non-greedy）
for i in [r'\d+', r'\d+?']:
    p = re.compile(i)
    r1 = p.findall('runoob 123 google 456')
    r2 = p.findall('run88oob123google456', 0, 10)
    print(r1, r2)

"""
re.finditer
和 findall 类似，
在字符串中找到正则表达式所匹配的所有子串，
并把它们作为一个迭代器返回，当考虑到性能优化时可以用
这个方法
语法：
re.finditer(pattern, string, flags=0)
每次返回一个match对象
"""
it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())

"""
re.split
split 方法按照能够匹配的子串将字符串
分割后返回列表
语法：
re.split(pattern, string[, maxsplit=0, flags=0])
maxsplit---分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
"""

print(re.split(r'\W+', 'runoob, runoob, runoob.'))
print(re.split(r'(\W+)', 'runoob, runoob, runoob.'))
print(re.split(r'\W+', 'runoob, runoob, runoob.'), 1)
print(re.split('a*', 'Hello world'))

"""
正在表达式可选修饰符flags说明:
re.I---使匹配对大小写不敏感
re.L---做本地化识别（locale-aware）匹配
re.M---多行匹配，影响 ^ 和 $
re.S---使 . 匹配包括换行在内的所有字符
re.U---根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X---该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""

"""
正则表达模式：
字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串
多数字母和数字前加一个反斜杠时会拥有不同的含义
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义
反斜杠本身需要使用反斜杠转义
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 '\\t')匹配相应的特殊字符
^---匹配字符串开头
$---匹配字符串末尾
.---匹配任意字符，除了换行符，当re.DOTALL标记被指定时，
则可以匹配包括换行符的任意字符
[...]---用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]---不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符
re*---匹配0个或多个的表达式
re+---	匹配1个或多个的表达式
re?---匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{n}---精确匹配 n 个前面表达式。例如,o{2}不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o
re{n,}---匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"
re{n, m}---匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a|b---匹配a或b
(re)---匹配括号内的表达式，也表示一个组
(?imx)---正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域
(?-imx)---正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域
(?: re)---类似 (...), 但是不表示一个组
\w---匹配字母数字及下划线
\W---匹配非字母数字及下划线
\s---匹配任意空白字符，等价于 [\t\n\r\f]
\S---匹配任意非空字符
\d---匹配任意数字，等价于 [0-9]
\D---匹配任意非数字
\A---匹配字符串开始
\z---匹配字符串结束
\b---匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'
\B---匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'
\n, \t, 等---匹配一个换行符。匹配一个制表符。等
\1...\9---匹配第n个分组的内容
"""




