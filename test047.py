#! /usr/bin/env python

from test046 import Die

#创建一个D6
die = Die()

#掷骰子，并将结果储存在列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)