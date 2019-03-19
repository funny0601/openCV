# 0312.py
import numpy as np
import cv2

def onChange(pos): # 트랙바 핸들러
    global img
    r = cv2.getTrackbarPos('R','img') 
    g = cv2.getTrackbarPos('G','img')
    b = cv2.getTrackbarPos('B','img')                   
    img[:] = (b, g, r)
    cv2.imshow('img', img)

img = np.zeros((512, 512, 3), np.uint8) # 검은색 바탕으로 시작 
cv2.imshow('img',img)

# 트랙바 생성
cv2.createTrackbar('R', 'img', 0, 255, onChange)
cv2.createTrackbar('G', 'img', 0, 255, onChange)
cv2.createTrackbar('B', 'img', 0, 255, onChange)

# 트랙바 위치 초기화
#cv2.setTrackbarPos('R', 'img', 0)
#cv2.setTrackbarPos('G', 'img', 0)
cv2.setTrackbarPos('B', 'img', 255)

cv2.waitKey()
cv2.destroyAllWindows()
