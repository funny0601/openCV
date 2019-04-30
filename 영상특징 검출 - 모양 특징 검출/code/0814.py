# 0814.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/hand.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
lowerb = (0, 40, 0)
upperb = (20, 180, 255)
bImage = cv2.inRange(hsv, lowerb, upperb)

mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(bImage, mode, method)

dst = src.copy()
##cv2.drawContours(dst, contours, -1, (255,0,0), 3)
cnt = contours[0]
cv2.drawContours(dst, [cnt], 0, (255,0,0), 2)

#2
dst2 = dst.copy()
rows,cols = dst2.shape[:2]
hull = cv2.convexHull(cnt)
cv2.drawContours(dst2, [hull], 0, (0,0,255), 2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()
cv2.destroyAllWindows()
