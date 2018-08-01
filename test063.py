#! /usr/bin/env python

from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20,40,60,80,100,120]
funnel = Funnel('漏斗图示例', width = 600, height = 400, title_pos = "center")
funnel.add("商品", attr, value, is_label_show = True,
           label_pos = "outside", legend_orient = "vertical", legend_pos = "left")
funnel.render()


