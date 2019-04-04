# 0511.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

#1
src = cv2.imread('../data/fruits.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)


#음영 원래값에서 v값만 equlize된 이후에 어떤 결과가 보일까?????^ㅠ^
v2=cv2.equalizeHist(v)
#바로 결과 확인하기 어려우니까..equlize된 v2를 구함
hsv2=cv2.merge([h,s,v2])
#화면에 보여주기위해서
dst=cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
cv2.imshow('equalize', dst)

#2
roi = cv2.selectROI(src)
print('roi =', roi)
roi_h = h[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
hist = cv2.calcHist([roi_h], [0], None,[64], [0, 256])

#print(hist)
plt.plot(hist,  color='r')
binX=np.arange(64)*4
plt.plot(binX, hist, color='b')
plt.show()


##roi_h가 대상이 되는 이미지..64개의 막대그래프를 이용해서 0에서 256까지 포함하겠다.
##256개/4......... 0,1,2,3을 묶어서 하나로...... 4개씩 묶어서 하나로......
backP= cv2.calcBackProject([h.astype(np.float32)], [0], hist,[0, 256],scale=1.0)
##h라고 하는 영역에 대해서 특정영역에대한 히스토그램을 가지고 backprojection하겠다.
##h라고 하는 색이 들어가야되는데 막대그래프의 실제 값을 넣어준다.


##minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(backP)
##T = maxVal -1 # threshold

#3
hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)
##sort는 정렬해주는 함수이다. hist를 정렬한다. hist는 앞에서 구한 것.(Roi..)
##hist에는 색마다 막대그래프가 있는데 색마다 정렬하면 제일 큰 값이 앞에 있을 것이다.

k = 1 
T = hist[k][0] -1 # threshold

#print(hist[0][0])
#print(hist[1][0])


##0번째 해당하는 막대말고 2번째 해당하는 막대보다 하나 작은값
##threadholding보다 큰 값은 화이트 작은값은 블랙으로 주는게 원래였는데..두번째 큰값보다 하나 작은 값을 기준으로..
##앞에서 부터 큰 두개값만 선호하는 값이니까 화이트로 표현해주고 나머지는 블랙으로 표현하겠다..

print('T =', T)
ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)

cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
