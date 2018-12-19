#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: gates
 @Desc:  
 @Author: yuzhongchun
 @Date: 2018-12-17 23:15
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-12-17 23:15
"""

import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def AND1(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND1(s1, s2)
    return y


if __name__ == '__main__':
    print("and gate")
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = AND1(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("nand gate")
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("or gate")
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("nor gate")
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
