#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: im2col_test
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-14 22:42
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-14 22:42
"""

import sys, os

sys.path.append(os.pardir)
import numpy as np
from common.util import im2col

x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)

x2 = np.random.rand(10, 3, 7, 7)
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape)
