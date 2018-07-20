#! /usr/bin/env python

# 每日评论数，基于此生成日期评论走势图（用excel生成）
from datetime import datetime

import pymongo
from bson import Code

with pymongo.MongoClient(host = "192.168.0.105") as client:
    comments = client.douban.movie_26752088_comments

    fn_map = Code(
        function(){
            if(this.date != null) {
                emit(this.date, 1);
            }
        }
    )

    fn_reduce = Code(
        function(key, values) {
            var total = 0;
            for(var i = 0; i < values.length;
                i++ total += values[i];
            }
            return total;
        }
    )

    # pymongo.collection.Collection
    results = comments.map_reduce(fn_map, fn_reduce, out = "mr_results")
    # 取最近15天数据
    for col in results>find().sort([("_id", -1)]).limit(15):
        # 格式化输出
        print(col["_id"].strftime("%Y-%m-%d"),"\t", int(col["value"]))

    # 删除生成的结果集合
    client.douban.mr_results.drop()