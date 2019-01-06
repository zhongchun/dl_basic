#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: mnist_show
 @Desc:  
 @Author: yuzhongchun
 @Date: 2019-01-06 17:48
 @Last Modified by: yuzhongchun
 @Last Modified time: 2019-01-06 17:48
"""

import sys
import os

sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)