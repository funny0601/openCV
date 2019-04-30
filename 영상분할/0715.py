# 0715.py
import cv2
import numpy as np

#1
src = cv2.imread('../data/circles.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

#2
ret, labels = cv2.connectedComponents(res)
print('ret=', ret)

#3
dst   = np.zeros(src.shape, dtype=src.dtype)
for i in range(1, ret): # 분할영역 표시
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    dst[labels == i] = [b, g, r]

cv2.imshow('res',  res)
cv2.imshow('dst',  dst) 
cv2.waitKey()
cv2.destroyAllWindows()
