# 0806.py
import cv2
import numpy as np

#1
src = cv2.imread('./CornerTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 영상은 언제나 gray로 바꿔주어야 한다


##K = 5
## 5개일 때는 찾는 것에 차이가 있다

K = 10
## 그럼 두 함수 모두 다 잘 찾아낸다 (harris쓴거랑 안 쓴거랑 둘다..)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=K,
              qualityLevel=0.05, minDistance=10)
# 영상이 주어졌을 때 바로 코너값을 계산해줄 수 있어서 편리하다
# useHarrisDectector 쓰지 않은 것
print('corners.shape=',corners.shape)
print('corners=',corners)

#2
corners2 = cv2.goodFeaturesToTrack(gray, maxCorners=K,
               qualityLevel=0.05, minDistance=10,
               useHarrisDetector=True, k=0.04)
# useHarrisDectector 쓴 것
print('corners2.shape=',corners2.shape)
print('corners2=',corners2)

#3
dst = src.copy()
corners = corners.reshape(-1, 2)
for x, y in corners:    
    cv2.circle(dst, (x, y), 5, (0,0,255), -1)
# 빨강: harris 안 쓴 것
corners2 = corners2.reshape(-1, 2)
for x, y in corners2:    
    cv2.circle(dst, (x, y), 5, (255,0,0), 2)
# 파랑: harris 쓴 것
cv2.imshow('dst',  dst) 
cv2.waitKey()
cv2.destroyAllWindows()
