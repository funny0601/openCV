# 0812.py
import cv2
import numpy as np

#1
src = cv2.imread('./data/banana.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
##bImage = cv2.erode(bImage, None)
bImage = cv2.dilate(bImage, None)
##cv2.imshow('src',  src)
cv2.imshow('bImage',  bImage)

#2
mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(bImage, mode, method)
print('len(contours)=', len(contours))

maxLength = 0
k = 0
for i, cnt in enumerate(contours):
    perimeter = cv2.arcLength(cnt, closed = True)
    if perimeter> maxLength:
        maxLength = perimeter
        k = i
print('maxLength=', maxLength)
cnt = contours[k]
dst2 = src.copy()
cv2.drawContours(dst2, [cnt], 0, (255,0,0), 3)
##cv2.imshow('dst2',  dst2)

#3
area = cv2.contourArea(cnt)
print('area=', area)
x, y, width, height = cv2.boundingRect(cnt)
dst3 = dst2.copy()
cv2.rectangle(dst3, (x, y), (x+width, y+height), (0,0,255), 2)
cv2.imshow('dst3',  dst3)

#4
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int32(box)
print('box=', box)
dst4 = dst2.copy()
cv2.drawContours(dst4,[box],0,(0,0,255),2)
cv2.imshow('dst4',  dst4)

#5
(x,y),radius = cv2.minEnclosingCircle(cnt)
dst5 = dst2.copy()
cv2.circle(dst5,(int(x),int(y)),int(radius),(0,0,255),2)
cv2.imshow('dst5',  dst5)

cv2.waitKey()
cv2.destroyAllWindows()
