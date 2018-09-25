#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def main (self,language,city,collectionType):
    print('当前爬取语言为 => ' + language + ' 当前爬取的城市为 => ' + city)
    utl = self.getUrl(language,city)
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(10)
    for i in range(30):
        selector = etree.HTML(browser.page_source)  #获取源码
        soup = BeautifulSoup(browser.page_source,'html.parser')
        span = soup.find('div', attrs = {'class': 'pagr_container'}).find('spam',attrs={'action':'next'})
