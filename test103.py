#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def get_pic_list(html):
    #获取每一个页面的套图列表，之后循环调用get_pic函数获取图片

    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find_all('li', class_ = 'wp-item')
    for i in pic_list:
        a_tag = i.find('h3', class_='tit').find('a')
        link = a_tag.get('href')    #套图链接
        text = a_tag.get_text()     #套图名字
        get_pic(link,text)