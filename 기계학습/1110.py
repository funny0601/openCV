#1110.py
''' ref1: http://yann.lecun.com/exdb/mnist/
    ref2: https://gist.github.com/ischlag/41d15424e7989b936c1609b53edd1390
'''
import gzip
import numpy as np
import cv2

IMAGE_SIZE = 28
PIXEL_DEPTH = 255
NUM_LABELS = 10

#1
def extract_data(filename, num_images):
  '''Extract the images into a 4D tensor [image index, y, x, channels].
     Values are rescaled from [0, 255] down to [0, 1].
  '''
##  print('Extracting', filename)
  with gzip.open(filename) as bytestream:
    bytestream.read(16)
    buf = bytestream.read(IMAGE_SIZE * IMAGE_SIZE * num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
##    data = data/PIXEL_DEPTH
    data = data.reshape(num_images, IMAGE_SIZE, IMAGE_SIZE)
    return data

def extract_labels(filename, num_images):
  '''Extract the labels into a vector of int64 label IDs.'''
##  print('Extracting', filename)
  with gzip.open(filename) as bytestream:
    bytestream.read(8)
    buf = bytestream.read(1 * num_images)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int32)
  return labels

def ont_hot_encoding(y): # assume that y is 1-D array
    t = np.zeros((y.size, 10), dtype=np.float32) # 주어진 값에 대해 라벨링 값을 모두 0으로 만들고 라벨에 해당되는 것만 1로 표현
    for i, row in enumerate(t):
        row[y[i]] = 1      
    return t
  
# Extract it into np arrays.
def load_MINIST(flatten=True, one_hot=True):
  x_train=extract_data('./mnist/train-images-idx3-ubyte.gz',  60000)
  y_train=extract_labels('./mnist/train-labels-idx1-ubyte.gz',60000)
  x_test =extract_data('./mnist/t10k-images-idx3-ubyte.gz',   10000)
  y_test =extract_labels('./mnist/t10k-labels-idx1-ubyte.gz', 10000)

  if flatten:
    x_train= x_train.reshape(-1, IMAGE_SIZE*IMAGE_SIZE) # (60000, 784)
    x_test = x_test.reshape(-1, IMAGE_SIZE*IMAGE_SIZE)  # (10000, 784)
  if one_hot:# 원핫인코딩
    y_train = ont_hot_encoding(y_train)
    y_test = ont_hot_encoding(y_test)    
  return (x_train, y_train), (x_test, y_test)

#2
(x_train, y_train), (x_test, y_test) = load_MINIST()
print('x_train.shape=', x_train.shape) # (60000, 784)
print('y_train.shape=', y_train.shape) # (60000, 10)
print('x_test.shape=',  x_test.shape)  # (10000, 784)
print('y_test.shape=',  y_test.shape)  # (10000, 10)

dst = np.zeros((20*IMAGE_SIZE, 20*IMAGE_SIZE), dtype=np.uint8)
for i in range(400): # 처음 400개의 데이터만 보기로 함
  x = i%20
  y = i//20
  x1 = x*IMAGE_SIZE
  y1 = y*IMAGE_SIZE
  x2 = x1+IMAGE_SIZE
  y2 = y1+IMAGE_SIZE  
  
  img = x_train[i].astype(np.uint8)
#  img = x_test[i].astype(np.uint8)
  img = img.reshape(IMAGE_SIZE, IMAGE_SIZE)
  dst[y1:y2, x1:x2] = img

cv2.imshow('MINIST 400', dst)
cv2.waitKey()
cv2.destroyAllWindows()
