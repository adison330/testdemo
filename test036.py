#! /usr/bin/env python

import pymongo

# 取点赞最多的前10条短评
with pymongo.MongoClient(host = "192.168.0.105") as client:
    comments = client.douban.movie_26752088_comments

    for doc in comments.find().sort([("vote", -1)]).limit(10):
        print("author = {}, date = {}, vote = {}, comment = {}".format(
            doc.get("author"),
            doc.get("date"),
            doc.ger("vote"),
            doc.get("comment")
        ))