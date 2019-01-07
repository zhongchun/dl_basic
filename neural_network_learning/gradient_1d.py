#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: gradient_1d
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-07 22:33
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-07 22:33
"""

import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def funtction_1(x):
    return 0.01 * x ** 2 + 0.1 * x


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d * x
    return lambda t: d * t + y


if __name__ == '__main__':
    x = np.arange(0.0, 20.0, 0.1)
    y = funtction_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")

    tf = tangent_line(funtction_1, 5)
    y2 = tf(x)

    print(x)
    print(y2)

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.show()
