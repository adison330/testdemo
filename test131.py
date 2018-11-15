#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from prettytable import PrettyTable
purchase_base = 10 #购买基数
ratio = 2  #中奖倍率
price_list = [] #投入金额
def init_purchase_list():
    x = PrettyTable(['投入','投入总额','获利','净利润'])
    cost = 0
    price_list.append(purchase_base)