#! /usr/bin/env python
#! -*- coding: utf-8 -*-

# Bokeh库
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, NumeralTickFormatter
from bokeh.layouts import gridplot

# 步骤一：将数据储存在ColumnDataSource中
gm_stats_cds = ColumnDataSource(phi_gm_stats_2)

# 步骤二：生成一个静态的html文件
output_file('phi-gm-linked-selections.html',
            title='76ers Percentages vs. Win-Loss')

# 创建CategoricalColorMapper，对win和loss分配特定颜色
win_loss_mapper = CategoricalColorMapper(factors = ['W', 'L'], palette=['Green', 'Red'])

# 自定义工具
toolList = ['lasso_select', 'tap', 'reset', 'save']

# 步骤三：配置图形界面
pctFig = figure(title='2PT FG % vs 3PT FG %, 2017-18 Regular Season',
                plot_height=400, plot_width=400, tools=toolList,
                x_axis_label='2PT FG%', y_axis_label='3PT FG%')

# 步骤四：采用圆点图绘制数据
pctFig.circle(x='team2P%', y='team3P%', source=gm_stats_cds,
              size=12, color='black')

# 将y轴标记变为百分比形式
pctFig.xaxis[0].formatter = NumeralTickFormatter(format='00.0%')
pctFig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# 创建一个与整体相关的图形
totFig = figure(title='Team Points vs Opponent Points, 2017-18 Regular Season',
                plot_height=400, plot_width=400, tools=toolList,
                x_axis_label='Team Points', y_axis_label='Opponent Points')

# 绘制正方形点图
totFig.square(x='teamPTS', y='opptPTS', source=gm_stats_cds, size=10,
              color=dict(field='winLoss', transform=win_loss_mapper))

# 创建图形布局
grid = gridplot([[pctFig, totFig]])

# 可视化展示
show(grid)