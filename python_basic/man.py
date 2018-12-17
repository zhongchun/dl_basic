#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: man.py
 @Desc:  
 @Author: yuzhongchun
 @Date: 2018-12-13 23:15
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-12-13 23:15
"""


class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")


if __name__ == '__main__':
    m = Man("David")
    m.hello()
    m.goodbye()
