#! /usr/bin/env python
#! -*- coding: utf-8 -*-

a = [1,2,3]
b = a[ : ]
print(b)

for i in range(1,10):
    print
    for j in range(1,i+1):
        print('%d*%d=%d' % (i,j,i*j))