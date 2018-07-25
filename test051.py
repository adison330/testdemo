#! /usr/bin/env python

import json

#将数据加载到一个列表
filename = "population.json"
with open(filename) as f:
    pop_data = json.load(f)

#打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict["Year"] == "1960":
        country_name = pop_dict["Country Name"]
        population = pop_dict["Value"]
        print(country_name + ":" + population)


