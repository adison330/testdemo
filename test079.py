#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import json

# python 字典类型转换为json 对象
data1 = {
    "no" : 1,
    "name" : "zhyfoundry",
    "url" : "http://www.zhyfoundry.com"
}

json_str = json.dumps(data1)
print ("python 原始数据： ", repr(data1))
print ("json 对象: ", json_str)

# 对json对象转换为python字段
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])