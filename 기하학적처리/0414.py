# 0414.py
import cv2
import numpy as np
src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#dst = cv2.resize(src, dsize=(320, 240))
#dst2 = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.2)

# 가로로 1.5배 확대, 세로로 1.2배 확대 

# 0415.py
dst = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
