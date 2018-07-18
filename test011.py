#! /usr/bin/env python
i = 0

while i < 10:

    #当i==7的时候不希望执行相应代码
    if i == 7:
        #在用continue之前，一定要修改计数器
        i += 1

        continue

    print (i)

    i += 1