#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def get_pic(link,text):
    #获取当前页面图片并保存
    html = download_page(link)   #下载界面
    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find('div', id='picture').find_all('img')  #找到界面所有图片
    headers = {'User-Agent': 'Mozilla/5.0 (windows NT 10.0; win64; x64; rv:61.0) Gecko/20100101 firefox/61.0'}
    create_dir('pic/{}'.format(text))
    for i in pic_list:
        pic_link = i.get('src')   # 拿到图片的具体 url
        r = requests.get(pic_link, headers=headers)  #下载图片 之后保存
        with open('pic/{}/{}'.format(text, link.split('/')[-1]), 'wb') as f:
            f.write(r.content)
            time.sleep(3) #休息一下

