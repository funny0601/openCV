# 0501.py
import cv2
import numpy as np
src = cv2.imread('./heart10.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)

#ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY) # thresholding 값: 120, 기준이 올라가면 올라갈 수록, 검은색 픽셀이 많아진다
ret, dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY_INV)   # THRESH_BINARY_INV : 색 반전

print('ret=', ret)
cv2.imshow('dst',  dst)

ret2, dst2 = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#THRESH_OTSU : 제시된 thresholding 값을 쓰지 않고, 자동으로 계산한 뒤 Binary에서 이진화 계산

print('ret2=', ret2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()    
cv2.destroyAllWindows()
