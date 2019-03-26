# 0419.py
import cv2
import numpy as np

## ..: 부모로 올라감
## . : 현재 자기 위치

src1 = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#src2 = np.zeros(shape=(512,512), dtype=np.uint8)+255 # white 영상 

src2 = np.zeros(shape=(512,512), dtype=np.uint8)+ 100
dst1 = 255 - src1 # src2 - src1 
dst2 = cv2.subtract(src2, src1)
dst3 = cv2.compare(dst1, dst2, cv2.CMP_NE) # cv2.CMP_EQ
n    = cv2.countNonZero(dst3)
print('n = ', n)

# 0418.py
dst1 = src1 + src2
dst2 = cv2.add(src1, src2, dtype=cv2.CV_8U)

# 클램핑 처리되어서 255이상의 값은 모두 255로 처리 
cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
