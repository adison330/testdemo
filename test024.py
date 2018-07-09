#! usr/bin/env  python

def sum_numbers(*args):

    num = 0
    for n in args:
        num += n

    #return num
print(sum_numbers(1,2,3,4,5,6))