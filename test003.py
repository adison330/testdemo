#! usr/bin/env  python
#计算0-100累计求和结果。
#0、定义最终结果的变量
result = 0

#1、定义一个整数的变量记录循环的次数
i = 0

#2、开始循环
while i <= 100:
    print(i)

    #每一次循环都让 result 这个变量和 i 这个计数器相加
    result += i

    #处理计数器、
    i+=1

print("0-100之前的数字求和结果为： %d" % result)
