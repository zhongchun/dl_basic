#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: basic_python.py
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-17 23:17
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-17 23:17
"""
import numpy as np

x = np.array([[0.1, 0.8, 0.1],
              [0.3, 0.1, 0.6],
              [0.2, 0.5, 0.3],
              [0.8, 0.1, 0.1]])

print(x)
y = np.argmax(x, axis=1)
print(y)

a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
b = np.argmax(a, axis=1)
print(b)