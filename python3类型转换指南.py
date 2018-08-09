#! /usr/bin/env python
#! -*- coding: utf-8 -*-


#float-int
int(-12.94)   # -12

#str-int
int('1209')
int('-12')
int('+1000')  #1000

# int-float
float(-1290)  # -1290.0

#str-float 如果字符串含有正负号、数字、小数点以外字符，则不支持转换。
float('-1209')    #-1209.0
float('-00120.2934')  #-120.2934
float('#726.9T')  #不支持转换

#bytes-float 如果bytes中含有正负号、数字、小数点以外字符，则不支持转换
float(b'-1209')     #-1209.0
float(b'-00120.290')  #-120.290
float(b'-#*06#')    #不支持转换

#int-complex  int转换complex时，会自动添加叙述部分并以0j表示。
complex(12)    #(12=0j)

#str-complex
"""
str转换complex时，如果能够转换成int 或 float,
则会转换后再转换为complex,如果字符串完全符合complex表达式规则，
也可直接转换。
"""
complex('-12.09')       #(-12.09+0j)
complex('-12.0')        #(-12+0j),去除了小数部分
complex('-12')          #(-12+0j)
complex('-12+9j')       #(-12+9j)
complex('(-12+9j)')     #(-12+9j)
complex('-12.0-2.0j')   #(-12+2j),去掉了小数点
complex('-12.0-2.09j')  #(-12-2.09j)
complex(b'12')          #报错，不支持bytes转换为complex
complex('12 + 9j')      #报错，加好两侧不能有空格

#str可将任意对象转换成字符串
str(12)                 # 12
str(-12.90)             # -12.9 会去除末尾为0的部分
str(complex(12 + 9j))   #(12+9j)
str(complex(12,9))      #(12+9j)

#bytes-str
str(b'hello world')      # b'hello world’
b'hello world'.decode()  # hello world
str(b'hello world', encoding = 'utf-8')    # hello world
str(b'ä¸­å½', encoding='utf-8')     #输出 ”中国“


# list-str 会先将值格式化为标准list表达式，然后再转换为字符串
str([])             #[]
str([1,2,3])        #[1,2,3]
"".join(['a','b','c'])  #abc

# tuple-str 会先将值格式化为标准的tuple表达式，然后再转换为字符串
str(())              # ()
str((1,2,3))         # (1,2,3)
''.join(('a','b','c'))  #abc

#dict-str 会先将值格式化为标准的dict表达式,然后再转换为字符串
str({})
str({'name':'hello','age':18})  #{'name':'hello',’age':18}
''.join({'name':'hello','age':18})  #nameage

#set-str 会先将值格式化为标准的set表达式，然后再转换为字符串
str(set({}))                        # set()
str({1,2,3})                        # {1,2,3}
'',join({'a','b','c'})              # abc

#转换内置对象
str(int)                            # <class 'int'>,转换内置类
str(hex)                            # <built-in function hex>,转换内置函数

# 转换类实例
class Hello:
    pass
obj = Hello()
print(str(obj))
#<__main__.Hello object at 0x107c6630>

# 转换函数
def hello():
    pass
print(str(hello))
# <function hello at 0x104d5a048>

# bytes 仅支持str转换为bytes类型
'中国'.encode()        # b'ä¸­å½'
bytes('中国',encoding = 'utf-8')  # b'ä¸­å½'

# list 支持转换为list类型的只能是序列，比如： str\tuple\dict\set等

list('123abc')            # ['1','2','3','a','b','c']
list(b'hello')            # [104,101,108,108,111] 会取没格子间的ASCII十进制值并组合成列表
list((1,2,3))             # [1,2,3]
list({1,2,3,3,2,1})       # {1,2,3}

#tuple 与列表一样,支持转换为tuple的类型，只能是序列
tuple('中国人')            # （’中‘，’国‘，’人‘）
tuple(b'hello')           # (104,101,108,108,111)
tuple([1,2,3])            # (1,2,3)
tuple(['name':'hello','age':18])  #('name','age')
tuple({1,2,3,3,2,1})              #(1,2,3)

# str-dict 的三种方法
# 使用json模块转换JSON字符串为字典时，需要完全符合JSON规范，尤其注意键和值只能由单引号包裹，否则会报错
import json
user_info = '{"name":"join","gender":"male","age":28}'
print(json.loads(user_info))
# {'name':'join','gender':'male','age':28}

# 使用eval函数能执行任何符合语法表达式的字符串，所以存在安全问题，不建议
user_info = "{'name':'join','gender':'male','age':28}"
print(eval(user_info))
#{'name':'john','gender':'male','age':28}

# 使用ast.listeral_eval进行转换既不存在使用json进行转换的问题，也不存在使用eval进行转换的安全性问题，因此推荐。
import ast

user_info = "{'name':'join’,'gender':'male','age':28}"
user_dict = ast.literal_eval(user_info)
print(user_dict)
# {'name':'john','gender':'male','age':28}


# list-dict  两个方法
# 通过zip将2个列表映射为字典：
list1 = [1,2,3,4]
list2 = [1,2,3]
print(dict(zip(list1,list2)))
#{1:1.2:2.3:3}

#将镶嵌的列表转换为字典
li = [
    [1,111]
    [2,222]
    [3,333]
]
print(dict(li))
#{1:111,2:222,3:333}


#tuple-dict
#通过zip将2个元组映射为字典：
tp1 = (1,2,3)
tp2 = (1,2,3,4)
print(dict(zip(tp1,tp2)))
#{1:1,2:2,3:3}

#将嵌套的元组转换为字典：
tp = (
    (1,111)
    (2,222)
    (3,333)
)
print(dict(tp))
# {1:111,2:222,3:333}

#set-dict 通过zip将2个集合映射为字典：
set1 = {1,2,3}
set2 = {'a','b','c'}
print(dict(zip(set1,set2)))
# {1:'c',2:'b',3:'a'}

# set
print(set('hello'))   # {'1','o','e','h'}
set(b'hello')         # {104,108,101,111}  会取每个字节的 ASCII 十进制值并组合成元组，再去重。
set([1,2,3,2,1])      # {1,2,3}
set((1,2,3,2,1))      # {1,2,3}
set({'name':'hello','age':18})    #{'age','name'}
