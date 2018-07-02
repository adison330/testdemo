#!/usr/bin/env python
import matplotlib.pyplot as plt

squares = [1,4,9,16,15]
plt.plot(squares)
plt.show()

def testFun():
    temp = [lambda x : i*x for i in range(4)]
    return temp

for everylambda in testFun():
    print (everylambda(2))


def testFun():
    temp = [lambda x,i=i: i*x for i in range(4)]
    return temp

for everylambda in testFun():
    print (everylambda(2))
