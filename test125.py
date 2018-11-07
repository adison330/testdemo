#! /usr/bin/env python
#! -*- coding: utf-8 -*-

def show_data(self):
    for index in range(5):
        queryArgs = {'day_avg_pv':{'$1t':10000}}
        rets = self