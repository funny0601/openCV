# 0501.py
import cv2
import numpy as np
src = cv2.imread('./flower.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

def onChange(pos):  # 트랙바 핸들러

    thresh = cv2.getTrackbarPos('V', 'img') # 트랙바를 이용
    #lower = (0, 0, 0)
    #upper = (180, 255, thresh)

    h, s, v = cv2.split(hsv)
    ret, v2= cv2.threshold(v, thresh, 255, cv2.THRESH_BINARY)
    src2 = cv2.merge((h, s, v2))

    #orange = cv2.bitwise_and(hsv, hsv, mask = v2)
    #cv2.imshow('orange', orange)

    src3=cv2.cvtColor(src2, cv2.COLOR_HSV2BGR)
    cv2.imshow('img', src3)

    # 마스크.. bitwise 연산.. 단 아무것도 필요가 없었다..
    #img_mask = cv2.inRange(hsv, lower, upper)
    #img_mask_inv=cv2.bitwise_not(img_mask)
    #cv2.imshow('img_mask', img_mask)
    #cv2.imshow('img_mask_inv', img_mask_inv)
    #result = cv2.bitwise_and(src, src, mask = img_mask_inv)
    #cv2.imshow('src', result)

img = np.zeros((512, 512, 3), np.uint8) # 검은색 바탕으로 시작
cv2.imshow('img',src)

# 트랙바 생성
cv2.createTrackbar('V', 'img', 0, 255, onChange)

# 트랙바의 위치 초기화
cv2.setTrackbarPos('V', 'img', 0)

cv2.waitKey()
cv2.destroyAllWindows()