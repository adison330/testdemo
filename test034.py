#! /usr/bin/env python

import pymongo
import jieba
from jieba import analyse
from matplotlib import pyplot
from wordcloud import WordCloud

test = None

with pymongo.MongoClient(host = "192.168.0.105",port = 27017) as client:
    # 获取集合
    comments = client.douban.movie_26752088_comments

    # 不知道为什么爬虫只取到另外1000条
    print("count:", comments.estimated_document_count())

    # pymongo.cursor.Cursor
    cursor = comments.find()

    # 遍历数据，这里只遍历短评数据
    test = " ".join(map(lambda doc: doc.get("comment"),cursor)

#对短语数据文本进行分词
#添加自定义分词
(jieba.add_word(k) for k in [])

#取top50的词生成词云
tags = analyse.extract_tags(text, topK = 50, withWeight = False)
new_text = " ".join(tags)
print(new_text)