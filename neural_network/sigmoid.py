#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: sigmoid
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-06 18:16
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-06 18:16
"""

import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()
