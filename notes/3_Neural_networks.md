# 神经网络

[TOC]

上一章我们学习了感知机。关于感知机，既有好消息，也有坏消息。好消息是，即便对于复杂的函数，感知机也隐含着能够表示它的可能性。上一章已经介绍过，即便是计算机进行的复杂处理，感知机（理论上）也可以将其表示出来。坏消息是，设定权重的工作，即确定合适的、能符合预期的输入与输出的权重，现在还是由人工进行的。上一章中，我们结合与门、或门的真值表人工决定了合适的权重。

神经网络的出现就是为了解决刚才的坏消息。具体地讲，神经网络的一个重要性质是它可以自动地从数据中学习到合适的权重参数。本章中，我们会先介绍神经网络的概要，然后重点关注神经网络进行识别时的处理。

## 从感知机到神经网络
### 神经网络的例子
![](https://note.youdao.com/yws/api/personal/file/WEBeb20bbfd6913a60d54d65b3b44a024e6?method=download&shareKey=ff10baf984ecbf110a88d649fe51c58a)

图 3-1 中的网络一共由 3 层神经元构成，但实质上只有 2 层神经元有权重，因此将其称为“2 层网络”。请注意，有的书也会根据构成网络的层数，把图 3-1 的网络称为“3 层网络”。本书将根据实质上拥有权重的层数（输入层、隐藏层、输出层的总数减去 1 后的数量）来表示网络的名称。

### 复习感知机


### 激活函数登场
激活函数 (activation function)

激活函数的作用在于决定如何来激活输入信号的总和。

激活函数是连接感知机和神经网络的桥梁。

一般而言，“朴素感知机”是指单层网络，指的是激活函数使用了阶跃函数 （阶跃函数是指一旦输入超过阈值，就切换输出的函数） 的模型。
“多层感知机”是指神经网络，即使用 sigmoid 函数（后述）等平滑的激活函数的多层网络。

## 激活函数
感知机中使用了阶跃函数作为激活函数。也就是说，在激活函数的众多候选函数中，感知机使用了阶跃函数。

### sigmoid 函数

神经网络中用 sigmoid 函数作为激活函数，进行信号的转换，转换后的信号被传送给下一个神经元。实际上，上一章介绍的感知机和接下来要介绍的神经网络的主要区别就在于这个激活函数。其他方面，比如神经元的多层连接的构造、信号的传递方法等，基本上和感知机是一样的。
 
### 阶跃函数的实现
```python
def step_function(x):
    y = x > 0
    return y.astype(np.int)

```

### 阶跃函数的图形

### sigmoid 函数的实现
```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

### sigmoid 函数和阶跃函数的比较
**不同点**
- 首先注意到的是“平滑性”的不同。sigmoid 函数是一条平滑的曲线，输出随着输入发生连续性的变化。而阶跃函数以 0 为界，输出发生急剧性的变化。sigmoid 函数的平滑性对神经网络的学习具有重要意义。

- 另一个不同点是，相对于阶跃函数只能返回 0 或 1，sigmoid 函数可以返回 0.731 ...、0.880 ... 等实数（这一点和刚才的平滑性有关）。也就是说，感知机中神经元之间流动的是 0 或 1 的二元信号，而神经网络中流动的是连续的实数值信号。

**相同点**
- 阶跃函数和 sigmoid 函数虽然在平滑性上有差异，但是如果从宏观视角看图 3-8，可以发现它们具有相似的形状。实际上，两者的结构均是“输入小时，输出接近 0（为 0）；随着输入增大，输出向 1 靠近（变成 1）”。也就是说，当输入信号为重要信息时，阶跃函数和 sigmoid 函数都会输出较大的值；当输入信号为不重要的信息时，两者都输出较小的值。
- 还有一个共同点是，不管输入信号有多小，或者有多大，输出信号的值都在 0 到 1 之间。

### 非线性函数
阶跃函数和 sigmoid 函数还有其他共同点，就是两者均为非线性函数。sigmoid 函数是一条曲线，阶跃函数是一条像阶梯一样的折线，两者都属于非线性的函数。

神经网络的激活函数必须使用非线性函数。换句话说，激活函数不能使用线性函数。为什么不能使用线性函数呢？因为使用线性函数的话，加深神经网络的层数就没有意义了。

线性函数的问题在于，不管如何加深层数，总是存在与之等效的“无隐藏层的神经网络”。

使用线性函数时，无法发挥多层网络带来的优势。因此，为了发挥叠加层所带来的优势，激活函数必须使用非线性函数。

### ReLU 函数
在神经网络发展的历史上，sigmoid 函数很早就开始被使用了，而最近则主要使用 ReLU（Rectified Linear Unit）函数。

ReLU（Rectified Linear Unit）函数

ReLU 函数在输入大于 0 时，直接输出该值；在输入小于等于 0 时，输出 0。

```python
def relu(x):
    return np.maximum(0, x)

```

## 多维数组的运算
### 多维数组
多维数组就是“数字的集合”，数字排成一列的集合、排成长方形的集合、排成三维状或者（更加一般化的）N 维状的集合都称为多维数组。

### 矩阵乘法

### 神经网络的内积
通过矩阵的乘积一次性完成计算的技巧，在实现的层面上可以说是非常重要的。

## 3层神经网络的实现
![](https://note.youdao.com/yws/api/personal/file/WEBa80f3fa277753b55d223ab0b855fab1e?method=download&shareKey=fb85afafaea3a9569dfc0e90a2bccf14)

图 3-15　3 层神经网络：输入层（第 0 层）有 2 个神经元，第 1 个隐藏层（第 1 层）有 3 个神经元，第 2 个隐藏层（第 2 层）有 2 个神经元，输出层（第 3 层）有 2 个神经元

### 符号确认
![](https://note.youdao.com/yws/api/personal/file/WEBdbb9371f96dead4b5f9ea2f1b1724040?method=download&shareKey=5d56679e2450e9a8eeee28e03e3971c7)

图 3-16　权重的符号

### 各层间信号传递的实现
![](https://note.youdao.com/yws/api/personal/file/WEB1d37ee9cc77bd70c88d975df157c60ea?method=download&shareKey=e14e448e636523ce7f8167435b453d70)
图 3-18　从输入层到第 1 层的信号传递

输出层所用的激活函数，要根据求解问题的性质决定。一般地，回归问题可以使用恒等函数，二元分类问题可以使用 sigmoid 函数，多元分类问题可以使用 softmax 函数。

### 代码实现小结
至此，神经网络的前向处理的实现就完成了。通过巧妙地使用 NumPy 多维数组，高效地实现了神经网络。

## 输出层的设计
神经网络可以用在分类问题和回归问题上，不过需要根据情况改变输出层的激活函数。一般而言，回归问题就用恒等函数，分类问题用 softmax 函数。

### 恒等函数和 softmax 函数
恒等函数会将输入按原样输出，对于输入的信息，不加以任何改动地直接输出。因此，在输出层使用恒等函数时，输入信号会原封不动地被输出。

![](https://note.youdao.com/yws/api/personal/file/WEBadda8e2a7eb060c1096942730afdce8b?method=download&shareKey=7e2df3b03ea84cb558a45dc5a67127fb)

图 3-21　恒等函数

类问题中使用的 softmax 函数可以用下面的式（3.10）表示。

![](https://note.youdao.com/yws/api/personal/file/WEBd6614b621fc683d557389315bbb61248?method=download&shareKey=86a3581df3a637cbfa0ada1d5b7983d4)

用图表示 softmax 函数的话，如图 3-22 所示。图 3-22 中，softmax 函数的输出通过箭头与所有的输入信号相连。这是因为，从式（3.10）可以看出，输出层的各个神经元都受到所有输入信号的影响。

![](https://note.youdao.com/yws/api/personal/file/WEBd1d90e48bcc30f6cf9598b540abec08b?method=download&shareKey=1acedc89ec02a4d33d72953d923363e6)

图 3-22　softmax 函数

```python
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
```

### 实现 softmax 函数时的注意事项
上面的 softmax 函数的实现虽然正确描述了式（3.10），但在计算机的运算上有一定的缺陷。这个缺陷就是溢出问题。
softmax 函数的实现中要进行指数函数的运算，但是此时指数函数的值很容易变得非常大。

softmax 函数的实现可以像式（3.11）这样进行改进。

![](https://note.youdao.com/yws/api/personal/file/WEB9993e79f53ee02ac1cc81a50535ba5bd?method=download&shareKey=377f4e77c4d229691b8624ad477cc826)

式（3.11）说明，在进行 softmax 的指数函数的运算时，加上（或者减去）某个常数并不会改变运算的结果。这里的 C' 可以使用任何值，但是为了防止溢出，一般会使用输入信号中的最大值。我们来看一个具体的例子。

```python
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
```

### softmax 函数的特征
softmax 函数的输出是 0.0 到 1.0 之间的实数。并且，softmax 函数的输出值的总和是 1。输出总和为 1 是 softmax 函数的一个重要性质。正因为有了这个性质，我们才可以把 softmax 函数的输出解释为“概率”。

一般而言，神经网络只把输出值最大的神经元所对应的类别作为识别结果。并且，即便使用 softmax 函数，输出值最大的神经元的位置也不会变。因此，神经网络在进行分类时，输出层的 softmax 函数可以省略。在实际的问题中，由于指数函数的运算需要一定的计算机运算量，因此输出层的 softmax 函数一般会被省略。

求解机器学习问题的步骤可以分为“学习”{5[“学习”也称为“训练”，为了强调算法从数据中学习模型，本书使用“学习”一词。——译者注]} 和“推理”两个阶段。首先，在学习阶段进行模型的学习 {6[这里的“学习”是指使用训练数据、自动调整参数的过程，具体请参考第 4 章。——译者注]}，然后，在推理阶段，用学到的模型对未知的数据进行推理（分类）。如前所述，推理阶段一般会省略输出层的 softmax 函数。在输出层使用 softmax 函数是因为它和神经网络的学习有关系（详细内容请参考下一章）。

### 输出神经元的数量
输出层的神经元数量需要根据待解决的问题来决定。对于分类问题，输出层的神经元数量一般设定为类别的数量。

## 手写数字的识别
介绍完神经网络的结构之后，现在我们来试着解决实际问题。这里我们来进行手写数字图像的分类。假设学习已经全部结束，我们使用学习到的参数，先实现神经网络的“推理处理”。这个推理处理也称为神经网络的前向传播（forward propagation）。

和求解机器学习问题的步骤（分成学习和推理两个阶段进行）一样，使用神经网络解决问题时，也需要首先使用训练数据（学习数据）进行权重参数的学习；进行推理时，使用刚才学习到的参数，对输入数据进行分类。

### MNIST 数据集
MNIST 是机器学习领域最有名的数据集之一，被应用于从简单的实验到发表的论文研究等各种场合。实际上，在阅读图像识别或机器学习的论文时，MNIST 数据集经常作为实验用的数据出现。

MNIST 数据集是由 0 到 9 的数字图像构成的。训练图像有 6 万张，测试图像有 1 万张，这些图像可以用于学习和推理。MNIST 数据集的一般使用方法是，先用训练图像进行学习，再用学习到的模型度量能在多大程度上对测试图像进行正确的分类。

MNIST 的图像数据是 28 像素 × 28 像素的灰度图像（1 通道），各个像素的取值在 0 到 255 之间。每个图像数据都相应地标有“7”, “2”, “1”等标签。

Python 有 pickle 这个便利的功能。这个功能可以将程序运行中的对象保存为文件。如果加载保存过的 pickle 文件，可以立刻复原之前程序运行中的对象。用于读入 MNIST 数据集的 load_mnist() 函数内部也使用了 pickle 功能（在第 2 次及以后读入时）。利用 pickle 功能，可以高效地完成 MNIST 数据的准备工作。

### 神经网络的推理处理
下面，我们对这个 MNIST 数据集实现神经网络的推理处理。神经网络的输入层有 784 个神经元，输出层有 10 个神经元。输入层的 784 这个数字来源于图像大小的 28 × 28 = 784，输出层的 10 这个数字来源于 10 类别分类（数字 0 到 9，共 10 类别）。此外，这个神经网络有 2 个隐藏层，第 1 个隐藏层有 50 个神经元，第 2 个隐藏层有 100 个神经元。这个 50 和 100 可以设置为任何值。

预处理在神经网络（深度学习）中非常实用，其有效性已在提高识别性能和学习的效率等众多实验中得到证明。在刚才的例子中，作为一种预处理，我们将各个像素值除以 255，进行了简单的正规化。实际上，很多预处理都会考虑到数据的整体分布。比如，利用数据整体的均值或标准差，移动数据，使数据整体以 0 为中心分布，或者进行正规化，把数据的延展控制在一定范围内。除此之外，还有将数据整体的分布形状均匀化的方法，即数据白化（whitening）等。

### 批处理
批处理对计算机的运算大有利处，可以大幅缩短每张图像的处理时间。那么为什么批处理可以缩短处理时间呢？这是因为大多数处理数值计算的库都进行了能够高效处理大型数组运算的最优化。并且，在神经网络的运算中，当数据传送成为瓶颈时，批处理可以减轻数据总线的负荷（严格地讲，相对于数据读入，可以将更多的时间用在计算上）。也就是说，批处理一次性计算大型数组要比分开逐步计算各个小型数组速度更快。

## 小结
本章介绍了神经网络的前向传播。本章介绍的神经网络和上一章的感知机在信号的按层传递这一点上是相同的，但是，向下一个神经元发送信号时，改变信号的激活函数有很大差异。神经网络中使用的是平滑变化的 sigmoid 函数，而感知机中使用的是信号急剧变化的阶跃函数。这个差异对于神经网络的学习非常重要，我们将在下一章介绍。

- 神经网络中的激活函数使用平滑变化的 sigmoid 函数或 ReLU 函数
- 通过巧妙地使用 NumPy 多维数组，可以高效地实现神经网络
- 机器学习的问题大体上可以分为回归问题和分类问题
- 关于输出层的激活函数，回归问题中一般用恒等函数，分类问题中一般用 softmax 函数
- 分类问题中，输出层的神经元数量设置为要分类的类别数
- 输入数据的集合称为批，通过以批为单位进行推理处理，能够实现高效运算


## Reference
1. [https://playground.tensorflow.org](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.45086&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
2. [第3章代码 GitHub](https://github.com/oreilly-japan/deep-learning-from-scratch/tree/master/ch03)
