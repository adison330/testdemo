#! /usr/bin/env python
#! -*- coding: utf-8 -*-

#pythonic way of value swapping

a,b = 5,10
print(a,b)
a,b = b,a
print(a,b)

a = ['python',' ','is',' ','awesome']
print(''.join(a))

#most frequent element in a list
a = [1,2,3,1,2,3,2,2,4,5,1]
print(max(set(a),key = a.count))

#using counter from collections
from collections import Counter

cnt = Counter(a)
print(cnt.most_common(3))

from collections import Counter
Counter(str1) == Counter(str2)

#reversing string with special case of slice step param
a = "asdfghjkloiuytre"
print(a[::-1])

#iterating over string contents in reverse efficiently
for char in reversed(a):
    print(char)

#reversing an integer through type conversion and slicing

num = 123456789
print(int(str(num)[::-1]))

#reversing list with special case of slice step param
a = [5,4,3,2,1]
print(a[::-1])

#interating over list contents in reverse efficiently
for ele in reversed(a):
    print(ele)

# chained comparison with all kind of operators
b = 6
print(4<b<7)
print(1==b<20)

# calling different functions with same arguments based on condition
def product(a,b):
    return a*b

def add(a,b):
    return a+b

b = True
print((product if b else add)(5,7))

# a fast way to make a shallow copy of a list
b = a
b[0] = 10

#both a and b will be [10,2,3,4,5]
b = a[:]
