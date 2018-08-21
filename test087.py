#! /usr/bin/env python
#! -*- coding: utf-8 -*-
from Tkinter import *  #导入Tkinter库
root = Tk()            #创建窗口对象的背景色
                       #创建两个列表
li  = ['c','python','php','html','SQL','java']
movie = ['css','jQuery','Bootstrap']
listb = Listbox(root)   #创建两个列表组建
listb2 = Listbox(root)
for item in li:
    listb.insert(0,item)

for item in movie:          #第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()             #将小部件放置到主窗口中
listb2.pack()
root.mainloop()         #进入消息循环