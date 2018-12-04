#! /usr/bin/env python
#! -*- coding: utf-8 -*-

# Bokeh库
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Div
from bokeh.layouts import gridplot, column

# 输出文件
output_file('ps-gm-linked-stats.html',
                title='Golden State Game Log')

# 将数据存入ColumnDataSource
gm_stats_cds = ColumnDataSource(gs_gm_stats)

# 调整布局
grid = gridplot([[stat_figs['Points'], stat_figs['Assists']],
                [stat_figs['Rebounds'], stat_figs['Turnovers']]])

# 将x轴联动
stat_figs['Points'].x_range = \
    stat_figs['Assists'].x_range = \
    stat_figs['Rebounds'].x_range = \
    stat_figs['Turnovers'].x_range

# 添加整体的大标题
html = """<h3>Golden State Game Log</h3>
<b><i>2017-18 Regular Season</i>
<br>
</b><i>Wins in green, losses in red</i>
"""
sup_title = Div(text=html)

# 可视化展示
show(column(sup_title, grid))