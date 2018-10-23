#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import random
test1 = (1,2,3,4,5,6,7,8,9,0,)
test2 = ('a','b','c','d',)

num1 = random.sample(test1,2)
nump1 = random.sample(test2,2)
test_out = random.sample(num1 + nump1,4)
test_print = str(test_out[0]) + str(test_out[1]) + str(test_out[2]) + str(test_out[3])

if __name__ == '__import__':
    main()