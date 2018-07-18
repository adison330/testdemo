#! /usr/bin/env python
def test(num):

    print("-" * 50)
    print("%d 在函数内的内存地址为 %x" % (num,id(num)))

    result = 100

    print("返回值 %d 在内存中的地址是 %x" % (result , id(result)))
    print("-" * 50)

    return result

a = 10
print("函数调用前，内存的地址是 %x" % id(a))

r = test(a)
print("调用函数后，实参内存地址为 %x" % id(a))
print("调用函数后，返回值的内存地址为 %x" % id(r))