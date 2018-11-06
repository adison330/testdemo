#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import math
import time

start = time.clock()
number = int(740914799/2)
marks_list = [True] * (number + 1)
marks_list[0] = marks_list[1] = False
for i in range(2, int(math,sqrt(number)) + 1):
    j = i
    t = j
    # 去掉倍数
    while j * t <= number:
        marks_list[j * t] = False
        t += 1

elapsed = str(time.clock() - start)

print(marks_list.count(True))
print('Time used:' + elapsed)
