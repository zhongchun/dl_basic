#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: numpy
 @Desc:  
 @Author: yuzhongchun
 @Date: 2018-12-13 23:17
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-12-13 23:17
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])
C = A + B
print(B)
print(C)
