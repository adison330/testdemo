#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import re

phone = "4008-996-996"   #这是一个电话号码

#删除注释
num = re.sub(r"#.*$","",phone)
print("电话号码 ： ", num)

#移除非数字的内容
num = re.sub(r"\D", "", phone)
print ("电话号码 ： ", num)

