#! /usr/bin/env python
name = '小明'

#解释器知道这里定义了一个函数

def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")

print(name)

say_hello

print(name)

def sum_2_num(num1,num2):

    result = num1 + num2

    print("%d + %d = %d" % (num1,num2,result))

sum_2_num(30,20)
