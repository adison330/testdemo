#! /usr/bin/env python

import jieba
seg_list = jieba.cut("我做的说唱从来不是为了混这个圈子", cut_all=True)
print("Full Mode: " + "/".join(seg_list))