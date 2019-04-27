#Sketch.py
import cv2
import numpy as np

img = cv2.imread('../data/lena.jpg')
cv2.imshow('src',img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이 영상 변환

img_gray = cv2.medianBlur(img_gray, 7) # 잡음제거

#스케치화 : 에지 검출
edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)  
ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV) 
#kernel = np.ones((3,3), np.uint8)        
#mask = cv2.erode(mask, kernel, iterations=5)     

img_sketch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) # 출력 영상을 위해 컬러 영상 변환

cv2.imshow('Sketch', img_sketch)

cv2.waitKey()    
cv2.destroyAllWindows()
