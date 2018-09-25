#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import numpy as np #矩阵
import matplotlib.pyplot as plt #绘图

def fish_predict(Dt): #Δt
    t_init = 0 #第0天开始
    t_end = 30 #第30天结束
    p_init = 30 #初始数量30
    n_steps = int(round((t_end - t_init) / Dt))

t_arr = np.zeros(n_steps +1) #创建一维矩阵t,记录自变量变化（初始为零）
P_arr = np.zeros(n_steps +1) #创建一维矩阵P，记录因变量变化（初始为零）
t_arr[0] = t_init  #默认值
P_arr[0] = P_init  #默认值
