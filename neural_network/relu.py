#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: relu
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-06 18:17
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-06 18:17
"""
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()
