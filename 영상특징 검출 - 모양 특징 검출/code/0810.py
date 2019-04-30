# 0810.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/circles.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

#2
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(bImage, mode, method)

dst = src.copy()
cv2.drawContours(dst, contours, -1, (255,0,0), 3) # 모든 윤곽선

#3
for cnt in contours:
    M = cv2.moments(cnt, True)
##    for key, value in M.items():
##        print('{}={}'.format(key, value))

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(dst, (cx, cy), 5, (0,0,255), 2)

cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
