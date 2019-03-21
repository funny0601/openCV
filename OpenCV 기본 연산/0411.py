# 0411.py
import cv2
src = cv2.imread('../data/lena.jpg')
print(type(src))
dst = cv2.split(src) # 2차원 배열 3개가 들어가 있는 구조

print(type(dst))
print(type(dst[0])) # type(dst[1]), type(dst[2])

cv2.imshow('blue',  dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red',   dst[2])

dst2 = cv2.merge(dst)
cv2.imshow('merge',   dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
