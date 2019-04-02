# 0502.py
import cv2
import numpy as np
src = cv2.imread('./srcThreshold.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)

ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 자체 계산한 제일 좋은 임계값 계산
cv2.imshow('dst',  dst)
print('ret=', ret)
# 그래도 좋은 결과가 나오지 않을 수 있음

dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
cv2.imshow('dst2',  dst2)
# 51: 블럭 사이즈, 7: 평균값을 그대로 사용하기 어려워서 7 정도의 보정값을 줌
# 산술 평균

dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)
cv2.imshow('dst3',  dst3)
# 가우시안 평균
# 항상 좋은 것은 아니지만 이 사진의 경우에는 더 좋은 결과가 나왔음

dst4 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 7)
cv2.imshow('dst4',  dst4)
# 작은 블록들, 잡음들이 처리가 잘 되지만 속도가 오래 걸릴 수 있음

cv2.waitKey()    
cv2.destroyAllWindows()
