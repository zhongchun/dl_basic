#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: nn
 @Desc:  
 @Author: yuzhongchun
 @Date: 2018-12-24 22:42
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-12-24 22:42
"""

import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def identity_function(x):
    """
    恒等函数
    将其作为输出层的激活函数
    """
    return x


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


if __name__ == '__main__':
    """
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1, 1)
    plt.show()

    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 5.5)
    plt.show()
    """
    network = init_network()
    x = np.array([1.0, 0.5])
    print(x.shape)
    print(x)
    print(network['W1'].shape)
    print(network['W1'])
    y = forward(network, x)
    print(y)
