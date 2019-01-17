# Python 入门
[TOC]

简单介绍了 python 的基本语法，初步介绍了 NumPy（线性代数矩阵和数组），Matplotlib（绘制图形）库的基本使用。

## 基本用法
### with

1. with语句时用于对try except finally 的优化，让代码更加美观

2. 除了打开文件，with语句还可以用于哪些地方呢
   
    with只适用于上下文管理器的调用，除了文件外，with还支持 threading、decimal等模块，当然我们也可以自己定义可以给with调用的上下文管理器

### 用于序列化的两个模块
#### json
用于字符串和Python数据类型间进行转换

json提供四个功能：dumps,dump,loads,load

#### pickle

用于python特有的类型和python的数据类型间进行转换

pickle提供四个功能：dumps,dump,loads,load

 
