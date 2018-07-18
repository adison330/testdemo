#! /usr/bin/env python

#修改为什么提交不上去呢？


def demo(*args,**kwargs):

    print(args)
    print(kwargs)

gl_num = (1,2,3,4,5,6)
gl_person = {"name" : "小明","age" : 18}

#会把两个作为元组传送给 args
demo(gl_num,gl_person)
demo(*gl_num,**gl_person)
