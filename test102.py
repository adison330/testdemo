#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def download_page(url):
    #用于下载页面
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    r = requests.get(url,headers=headers)
    r.encoding = 'gb2312'
    return r.text
