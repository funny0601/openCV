# 0804.py
import cv2
import numpy as np

#1
def findLocalMaxima(src):
    # 지역을 대표할 수 있는 대표값을 찾을 수 있는 함수
    kernel= cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(11,11))
    # morphological 마스크.. 사각형 마스크, 사이즈는 11by 11

    dilate = cv2.dilate(src,kernel)# local max if kernel=None, 3x3
    # 이 마스크로 팽창시켰다. 팽창, 침식은 자기 모습을 유지한다. 0, 1이 아닌 값을 팽창하는 건 최대값으로 해준 것과 동일하다고 볼 수 있다.
    # 11x11안의 제일 큰 값으로 바꿔주겠다. dilate연산 특징
    # 값이 전체적으로 더 큰값으로 바뀐다. 원래 src보다 dilate한 후 영상 값이 전체적으로 커진다.
    # 하지만 바뀌지 않는 값: 자기가 제일 큰 값일 경우는 바뀌지 않는다.

    localMax = (src == dilate)
    # 원래 커서 바뀌지 않는 그 지점에 해당되는 값을 찾겠다.
    # 코너값 중 제일 큰 값을 찾았다!

    erode = cv2.erode(src,kernel) #  local min if kernel=None, 3x3 
    # 원래 있던 값에 대해서 침식도 해주었다.
    # 주변값 중 제일 작은 값으로 바뀌게 된 것임

    localMax2 = src > erode
    # 0으로 싹 다 바뀌었을 것임..
    # 원래 src보다 전체적으로 값이 줄어든다
    # 최솟값보다 큰 값은 모두 true로 바뀌게 된다

    localMax &= localMax2
    # localMax와 localMax2 연산을 and연산시켜준다.
    # true와 true있으면 true
    # 하나라도 false면 false

    points = np.argwhere(localMax == True)
    points[:,[0, 1]] = points[:,[1, 0]] # switch x, y
    return points

#2
src = cv2.imread('./CornerTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
res = cv2.cornerHarris(gray, blockSize=5, ksize=3, k=0.01)
# 주어진 영상을 그레이로 바꾼 8비트짜리 영상, 패치 사이즈 5, 소벨시 이용할 마스크 사이즈 크기 3로 코너 해리스 계산함
# print(res): 계산된 모든 c값을 보여줌

ret, res = cv2.threshold(np.abs(res),0.02, 0, cv2.THRESH_TOZERO)
# 계산된 결과 res를 가지고 thresholding을 해준다. 0.02를 임계값으로 한다
# 그 결과값을 res로 다시 반환해준다
# print(res)

res8 = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
# 리턴값에 대해 normalize시킴, c 값 그 자체로 영상으로 보여줄 수 없음. 8비트로 표현해주어야 하기 때문에
# 화면으로 영상 출력하려고 normalize 시킨 것
# 이 상태에서는 한 점이 아니고 여러 픽셀들이 모여있는 형태임
# 최소 0 최대 255로 영상 stretching
cv2.imshow('res8',  res8)

corners = findLocalMaxima(res)
# normalize되지 않은 값을 가지고 findLocalMaxima 함수 호출

print('corners=', corners)

#3
#corners = np.float32(corners).copy()
corners = corners.astype(np.float32, order='C')
term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS, 10, 0.01)
# 내가 찾은 오차가 0.01보다 작을때까지 반복하겠다

corners2 = cv2.cornerSubPix(gray, corners,(5,5),(-1,-1), term_crit)
# findLocalMaxima로 찾은 코너 값을 세련화, 미세화하는 과정

print('corners2=', corners2)

dst = src.copy()
for x, y in corners2:    
    cv2.circle(dst, (x, y), 3, (0,0,255), 2)
cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
