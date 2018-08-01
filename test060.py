#! /usr/bin/env python

from pyecharts import Bar, Line, Overlap

attr = ["A", "B", "C", "D", "E", "F"]
v1 = [10, 20, 30, 40, 50, 60]
v2 = [38, 28, 58, 48, 78, 68]
bar = Bar("Line - Bar示例")
bar.add("bar", attr, v1)
line = Line()
line.add("line", attr, v2)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)

overlap