# README

This is a projects about deep learning basics.

All the contents are from Deep learning introduction. 

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

