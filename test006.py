#!/usr/bin/env python
#输入age变量
age = int(input("请输入您的年龄："))

#要求输入年龄在0-60岁之间
if age >= 0 and age <= 60:
    print("年龄可以参加活动")
else:
    print("年龄不能参加活动")