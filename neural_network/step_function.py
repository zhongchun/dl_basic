#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: step_function
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-06 18:18
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-06 18:18
"""
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()
