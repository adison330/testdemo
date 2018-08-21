#! /usr/bin/env python
#! -*- coding: utf-8 -*-

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k) and (i != j) and (j != k):
                print (i,j,k)

i = int(input('净利润： '))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i = arr[idx]
print (r)

for i in range(1,85):
    if 168%i == 0:
        j = 168/i;
        if i > j and (i+j) % 2 == 0 and (i-j) % 2==0:
            m =(i+j)/2
            n =(i-j)/2
            x = n*n - 100
            print(x)