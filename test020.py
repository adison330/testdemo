#! /usr/bin/env python
def measure():
    """返回当前的温度"""

    print("开始测量...")
    temp = 39
    wetness = 10
    #return (temp, wetness)
    print("测量结束...")

    return (temp,wetness)

result = measure()
print(result)