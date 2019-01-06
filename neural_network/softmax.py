#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: softmax
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-06 17:20
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-06 17:20
"""

import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

if __name__ == '__main__':
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)
    print(y)