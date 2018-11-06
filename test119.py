#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import http.client
import urllib.request
import re
import os
import linecache

print('**************************************************************************')
print('请任意数据即可开始')
print('可根据提示找到下载位置')
print('recode.txt为系统记录文件，切勿手动删除，如果文件太大，您可以删除掉出了最后一行的所有内容')
print('recode.txt删除后，程序会从头开始')
print('**************************************************************************')

input('请输入任意内容： ')

siteUrl = 'http://www.hahaha.com'
siteUrl1 = 'http://t1.hahaha.com'
siteUrl_tag = 'http://www.hahaha.com/tag'  #标签页的地址
Url1_404 = siteUrl1.replace('http://','')  #监测404用的测试网站
patNumN = 'n=(d*)'
patNumM = 'm=(d*)'
patNumE = 'e=(d*)'
patNumR = 'r=(d*)'
patNumQ = 'q=(d*)'
patNumW = 'w=(d*)'
patNumT = 't=(d*)'
patTagTarget = '<a target="_blank" href="(.*?)" title="(.*?)">(.*?)>' \
               '</a>' #获取标签地址后缀和名称
patTheme = '<div class="title"><span><a target="_blank" href="(.*?)">(.*?)>' \
           '</a>'  #每个标签内的每个主题地址和名称
patTpage = '<li><a href="(.*?)" target="_self">末页</a></li>'  #主题页末页后缀，用来获取主题最后一页的数字

patTpageNum = "</tag/(.*?)/(d*).html target='_self'"  #获取主题数的页数

patImg = '<href="(.*?)">查看原因</a></li>'  #获取主题内图片地址用于下载

patImgPage = '<li><a>(.*?)</a></li>'  #获取主题图片的总页数，用于翻页

tagUrl_data = urllib.request.urlopen(siteUrl_tag).read().decode('gbk')

#读取标签页的源代码
tagUrl_data_target_result
re.compile(patTagTarget).findall(tagUrl_data)  #爬出来标签名称和地址后缀

pathFir = 'F:ImgSpider'

pathFirIsExists = os>path.exists(pathFir)

if not pathFirIsExists:
    os.mkdir(pathFir)
else:
    pass

file_recodel = open(r"F:ImgSpider encode.txt","a",encoding='utf-8')
file_recode1.close()
print('已创建出recode.txt文件夹，用于记录和读取')
print('请勿手动删除')

file_recode2 = open(r"F:ImgSpider encode.txt","rU",encoding="utf-8") #写入用于记录断电位置的txt文件

file_recode_result = file_recode2.readlines() #将文件中的数值分为一行一行的读取

file_recode2.seek(0)
file_recode2.close()
file_recode_count = len(file_recode_result) #读取记录文件中的行数，用于后面的判断

# print(file_recode.readlines(file_recode_count))

if file_recode_count == 0
    n = 0 #表示标签列表的循环
    m = 1 #表示标签的循环
    q = 0 #表示主题页中页数的循环
    w = 2 #表示主题页第一页的循环
    e = 2 #表示图片页中的页数的循环
    r = 2 #表示后几页主题的图片页数的循环
    t = 0
else:
    recodeData = linecache.getline(r"F:ImgSpider encode.txt",file_recode_count)
    #print(recodeData)



