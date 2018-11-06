#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from prettytable import PrettyTable

purchase_base = 10 #购买基数
ratio = 2 #中奖倍数
price_list = []  #投入金额

def init_purchase_list():
    x = PrettyTable(['投入','投入总额','获利','净利润'])
    cost = 0
    price_list.append(purchase_base)
    # 其他进行动态计算
    print('初始化投入金额表格...')
    for i in range(0,10):
        cost += purchase_base * (2**i)  #花费
        bonus = purchase_base * (2**i) * ratio  #奖金
        x.add_row([purchase_base * (2**i), cost, bonus, bonus - cost])
        print(x)
    if __name__ == '__main__':
        init_purchase_list()