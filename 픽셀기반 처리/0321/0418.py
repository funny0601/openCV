# 0418.py: OpenCV-Python Tutorials 참조
import cv2
import numpy as np

src1 = cv2.imread('../data/lena.jpg')
src2 = cv2.imread('../data/opencv_logo.png')

mask = cv2.imread('../data/opencv_logo_mask.png', cv2.IMREAD_GRAYSCALE)
mask_inv = cv2.imread('../data/opencv_logo_mask_inv.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('src2',  src2)

#1
rows,cols,channels = src2.shape
roi = src1[0:rows, 0:cols]
# lena 이미지 전체에서 opencv 로고에 해당되는 동일한 크기만큼 잘라낸다. 

#2
#gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
#ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
#mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask',  mask)
#cv2.imshow('mask_inv',  mask_inv)

#3
src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
# roi와 mask를 and 해준다. (이진 비트 연산)
# 화이트는 색을 날리고~ 원본 색상이 남게 되고,  블랙은 색을 남기고.. 
cv2.imshow('src1_bg',  src1_bg)

#4
src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
cv2.imshow('src2_fg',  src2_fg)

#5
##dst = cv2.add(src1_bg, src2_fg)
dst = cv2.bitwise_or(src1_bg, src2_fg)
cv2.imshow('dst',  dst)

#6
src1[0:rows, 0:cols] = dst

cv2.imshow('result',src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
