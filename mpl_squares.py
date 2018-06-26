#!/usr/bin/env python
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square or Value", fontsize=18)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=16)

plt.show()