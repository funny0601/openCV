# 0409.py
import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#dst = src          #참조: 이름만 2개가 붙여진 것이고 하나를 가리키고 있음

# 0410.py
shape = src.shape[0], src.shape[1]
dst = np.zeros(shape, dtype=np.uint8)
#dst = src.copy()     #복사 
dst[100:400, 200:300] = 255

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()
