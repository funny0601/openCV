# 0410.py
import cv2
import numpy as np
 
src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
shape = src.shape[0], src.shape[1], 3
dst = np.zeros(shape, dtype=np.uint8)

dst[:,:,0] = src      # B-채널 
##dst[:,:,1] = src    # G-채널 
##dst[:,:,2] = src    # R-채널 

dst[100:400, 200:300, :] = [255, 255, 255]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()
