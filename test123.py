#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from prettytable import PrettyTable

purchase_base = 10 #购买基数
ratio = 1.96 #中奖倍数
price_list = []  #投入金额

def init_purchase_list():
    x = PrettyTable(['投入',])