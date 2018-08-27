#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import time

myD = {1:'a',2:'b'}
for key,value in dict.items(myD):
    print (key,value)
    time.sleep(3)  #暂停3秒

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time,time())))

#暂停三秒
time.sleep(3)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))