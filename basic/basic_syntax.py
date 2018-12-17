#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: basic_syntax
 @Desc:  
 @Author: yuzhongchun
 @Date: 2018-12-13 23:00
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-12-13 23:00
"""

# arithmetic operation
print(1 + 2)

# data type
print(type(10))
print(type(2.718))
print(type("hello"))

# variable
x = 10
print(x)

x = 100
print(x)

y = 3.14
print(y)

z = x * y
print(z)
print(type(z))

# Python 是属于“动态类型语言”的编程语言，所谓动态，是指变量的类型是根据情况自动决定的

# list
a = [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[0])
print(a[4])
a[4] = 99
print(a)
# slicing
print(a[0:2])
print(a[1:])
print(a[:3])
print(a[:-1])
print(a[:-2])

# dict
me = {'height': 180}
print(me['height'])
me['height'] = 70
print(me)

# bool
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)

# if
hungry = True
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")

# for
for i in [1, 2, 3]:
    print(i)


# function
def hello():
    print("Hello World!")


hello()


def hello(object):
    print("Hello " + object + "!")


hello("cat")


