#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

data = np.arange(100,201)
plt.subplot(2,1,1)
plt.plot(data)

data2 = np.arange(200,301)
plt.subplot(2,1,2)
plt.plot(data2)

plt.show( )