#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def show_data(self):
    for index in range(5):
        queryArgs = {"day_avg_pv": {"$lt": 100000}}
        rets = self.zfdb.national_month_index.find(queryArgs).sort("day_avg_pv", pymongo.DESCENDING).limit(10).skip(index*10)
        atts = []
        values = []
        file_name = "top" + str(index * 10) + "-" + str((index + 1) * 10) + ".html"
        for ret in rets:
            print(ret)
            atts.append(ret["address"])
            values.append(ret["day_avg_pv"])
        self.show_line("各景点 30 天内平均搜索量", atts, values)
        os.rename("render.html", file_name)

def show_data(self):
    for index in range(5):
        queryArgs = {'day_avg_pv': {'slt': 100000}}
        rets = self.zfdb