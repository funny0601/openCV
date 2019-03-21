# 0401.py
import cv2
import numpy as np

img = cv2.imread('../data/lena.jpg') # cv2.IMREAD_COLOR
#img = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print('img.ndim=', img.ndim)
print('img.shape=', img.shape)
print('img.dtype=', img.dtype)

# 0402.py
#img = img.flatten()
#print('img.shape=', img.shape)

# 0403.py
#img[100, 200] = [255, 0, 0]
#img[100:400, 200:300] = [255, 0, 0]  # 컬러일 경우 세 가지 값을 배열로 묶어서 저장

# 0405.py
# 0403.py와 동일, 표현법만 다름 
img[100:400, 200:300, 0] = 255
img[100:400, 200:300, 1] = 0
img[100:400, 200:300, 2] = 0


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

## np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
#img=img.astype(np.int32)
#print('img.dtype=',img.dtype)

#img=np.uint8(img)
#print('img.dtype=',img.dtype)
