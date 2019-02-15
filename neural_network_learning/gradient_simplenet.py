#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: gradient_simplenet
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-10 22:56
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-10 22:56
"""

import sys
import os

sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss


if __name__ == '__main__':
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])
    net = simpleNet()
    print("=================================================")
    print(net.W)
    z = net.predict(x)
    print(z.shape)
    # lambda 参数 大小写没有影响吗？
    f = lambda W: net.loss(x, t)
    f2 = lambda w: net.loss(x, t)
    dW = numerical_gradient(f, net.W)
    dW2 = numerical_gradient(f2, net.W)
    print("=================================================")
    print(dW)
    print("=================================================")
    print(dW2)
