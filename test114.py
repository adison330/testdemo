#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import random
def SelectRandomk(L,N,k):

    for i in range(0,k):
        #产生i到n-1间的随机数
        j = random.randint(i,n-1)
        L[i],L[j] = L[j],L[i]

def SelectRandom1(L):
    # 计数器
    num = 2
    for item in L[1:]:
        if random.random() < 1.0/num:
            L[0],L[num-1] = L[num-1],L[0]
        num += 1

def SelectRandowK(L,k):
    #计数器
    num = k+1
    for item in L[k:]:
        if random.random() < float(k/num):
            # 产生0-k-1之间的随机数
            j = random.randint(0,k-1)
            L[num - 1],L[j] = L[j],L[num -1]
        num += 1