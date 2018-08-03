#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import json

# Python 字典类型转换为 JSON 对象
data = {
    "no" : 1,
    "name" : "zhyfoundry",
    "url" : "http://www.zhyfoundry.com"
}

json_str = json.dumps(data)
print("python 原始数据", repr(data))
print("Json 对象", json_str)
