#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import re

print(re.search("www", "www.alibaba.com").span())   #在起始位置匹配
print(re.search("com", "www.alibaba.com").span())   #不在起始位置匹配
