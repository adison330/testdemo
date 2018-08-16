#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import requests
import time
import random
import json

# 获取每一夜数据
def get_one_page(url):

    response = requests.get(url=url)
    if response.status_code == 200
        return response.text
    return None

#解析每一页数据
def parse_one_page(html):

    data = json.loads(html)['cmts'] #获得评论许可
    for item in data:
        yield{
            'date' : item['time'].split(' ')[0],
            'nickname': item['nickName'],
            'city':item['cityName'],
            'rate':item['score'],
            'conment':item['contemt']
        }

#保存到文本文档中
def save_to_txt():
    for i in range(1,1001):

        print('开始保存第%d页' % i)
        url = 'http://m.maoyan.com/mmdb/comments/movie/1175253.json?_v_=yes&offset=' +

        html = get_one_page(url)
        for item in parse_one_page(html):
            with open('爱情公寓.txt','a',encoding='utf-8') as f:
                f.write(item['date'] + ',' + item['nickname'] + ',' + item['city']
                        + ',' + str(item['rate']) + ',' + item['conment'] + '')
                #time.sleep(random.randint(1,100)/20
                time.sleep(2)

#去重重负的评论内容
def delete_repeat(old,new):
    oldfile = open(old,'r',encoding = 'utf-8')
    newfile = open(new,'w',encoding = 'utf-8')
    content_list = oldfile.readlines() #获取所有评论数据集
    content_alread = [] #存贮去重后的评论数据集

    for line in content_list:
        if line not in content_alread:
            newfile.write(line + '')
            content_alread.append(line)

if __name__ == '__main__':
    save_to_txt()
    delete_repeat(r'爱情公寓_old.txt',r'爱情公寓_new.txt')