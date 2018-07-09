#! usr/bin/env  python
#1、请输入用户年龄
age = int(input("你今年年龄多大了？"))

#2、判断是否满18岁
#if语句以及缩进部分是个完整的代码块
if age >= 18:
    print ("可以进网吧")
else:
    print ("年龄不到，不准进")

#3、这行代码无论何时都会打印
print ("不用猜，都会打印")