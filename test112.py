#! /usr/bin/env python
#! -*- coding: utf-8 -*-

class JobboleArticleItem(scrapy.Item)
    front_img = scrapy.Field() #封面图
    title = scrapy.Field()  #标题
    create_time = scrapy.Field()  #发布时间
    url = scrapy.Field()  #当前页url

