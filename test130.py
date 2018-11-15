#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def get_year_list():
    year_list = []
    for i in range(1949,2017):
        year_list.append(str(i))
        return year_list

def get_totle_population():
    year_list = get_year_list()
    with open('总人口.csv','a+',encoding = 'utf-8', newline = '') as files:
        fieldnames = ['年份','年末总人口（万人）','男性人口（万人）','女性人口（万人）',
                      '城镇人口（万人）','乡村人口（万人）']
        writer = csv.DictWriter(files, fieldnames = fieldnames)
        writer.writeheader()
        for year in year_list:
            url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds' \
                  '=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22{year}%22%7D%5D'.format(
 year=year)
            wbdata = requests.get(url,headers = headers)
            jsdata = json.loads(wbdata.text)
            data = jsdata['returndata']['datanodes']
            item =