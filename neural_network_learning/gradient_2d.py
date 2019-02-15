#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: gradient_2d
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-08 22:25
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-08 22:25
"""

import numpy as np
import matplotlib.pylab as plt
# from mpl_toolkits.mplot3d import Axes3D
# import sys


def _numerical_gradient_no_batch(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val

    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)

        return grad


def function_2(x):
    if x.ndim == 1:
        return np.sum(x ** 2)
    else:
        return np.sum(x ** 2, axis=1)


def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d * x
    return lambda t: d * t + y


if __name__ == '__main__':
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)

    # # explore the data: x0, x1, X, Y
    # print(type(x0))
    # print(x0.shape)
    # print(x0)
    # print(X.shape)
    # print(type(X))
    # print(X)
    # print(Y.shape)
    # print(Y)

    X = X.flatten()
    Y = Y.flatten()

    # # explore the data: X, Y
    # print(type(X))
    # print(X.shape)
    # print(X.size)
    # print(X)
    # print(Y.shape)
    # print(Y.size)
    # print(Y)
    # Z = np.array([X, Y])
    # print(type(Z))
    # print(Z.shape)
    # print(Z.size)
    # for idx, x in enumerate(Z):
    #     print(idx, x)
    # exit()

    grad = numerical_gradient(function_2, np.array([X, Y]))
    print(grad.shape)
    print(grad.size)

    plt.figure()
    plt.quiver(X, Y, -grad[0], -grad[1], angles="xy", color="#666666")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
