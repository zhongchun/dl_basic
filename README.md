# README

This is a projects about deep learning basics.

All the contents are from a book called Deep learning from Scratch.

## 简介
深度学习入门：基于Python的理论和实现
![](https://note.youdao.com/yws/api/personal/file/WEB1b21eedb4a3e78c5e742ffa97d9c15d5?method=download&shareKey=b4dea69cb97bc9518be0886de84013c7)

- 日本深度学习入门经典畅销书，原版上市不足2年印刷已达100000册。长期位列日亚“人工智能”类图书榜首，众多五星好评。
- 使用Python 3，尽量不依赖外部库或工具，从零创建一个深度学习模型。
- 示例代码清晰，源代码可下载，需要的运行环境非常简单。读者可以一边读书一边执行程序，简单易上手。
- 使用平实的语言，结合直观的插图和具体的例子，将深度学习的原理掰开揉碎讲解，简明易懂。
- 使用计算图介绍复杂的误差反向传播法，非常直观。
- 相比“花书”，本书更合适入门。

从零开始编写可实际运行的程序，一边看源代码，一边思考。

## 主要内容
- Python 入门
- 感知机
- 神经网络
- 神经网络的学习
- 误差反向传播法
- 与学习相关的技巧
- 卷积神经网络
- 深度学习

## Contents 
### Python basic
python_basic

### Perceptron
perceptron

### Neural Network
neural_network

### Neural Network Learning
neural_network_learning

### Backward Propagation algorithm
backward_algorithm

### Learning skills
learning_skills

### Convolutional Neural Network
cnn

### Deep Learning
dnn

## MNIST DataSet
The [MNIST](http://yann.lecun.com/exdb/mnist/) database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.

Four files are available on this site:
```
train-images-idx3-ubyte.gz:  training set images (9912422 bytes) 
train-labels-idx1-ubyte.gz:  training set labels (28881 bytes) 
t10k-images-idx3-ubyte.gz:   test set images (1648877 bytes) 
t10k-labels-idx1-ubyte.gz:   test set labels (4542 bytes)
```

1. uncompress the above files
```
gunzip train-images-idx3-ubyte.gz
```
or
```
gzip -d train-images-idx3-ubyte.gz
```

2. look an insight to the file
```
train-images-idx3-ubyte.gz
```
just like this:
```
00000000  00 00 08 03 00 00 ea 60  00 00 00 1c 00 00 00 1c  |.......`........|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
000000a0  00 00 00 00 00 00 00 00  03 12 12 12 7e 88 af 1a  |............~...|
000000b0  a6 ff f7 7f 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000000c0  1e 24 5e 9a aa fd fd fd  fd fd e1 ac fd f2 c3 40  |.$^............@|
000000d0  00 00 00 00 00 00 00 00  00 00 00 31 ee fd fd fd  |...........1....|
000000e0  fd fd fd fd fd fb 5d 52  52 38 27 00 00 00 00 00  |......]RR8'.....|
```

