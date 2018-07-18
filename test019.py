#! /usr/bin/env python
a = 10

def demo():
    print("%d" % a)
    print("%d" % b)
    print("%d" % c)

#全局变量要定义在调用之前，所以最好都在最前面定义。
b = 20
demo()
c = 30