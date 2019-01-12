#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: layer_native
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-12 22:29
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-12 22:29
"""


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy
