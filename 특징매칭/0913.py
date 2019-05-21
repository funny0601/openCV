# 0913.py
import cv2
import numpy as np
#1    
src1 = cv2.imread('book1.jpg') # 'cup1.jpg'
src2 = cv2.imread('book2.jpg') # 'cup2.jpg'
img1= cv2.cvtColor(src1,cv2.COLOR_BGR2GRAY)
img2= cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)

#2-1
orbF   = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orbF.detectAndCompute(img1, None)
kp2, des2 = orbF.detectAndCompute(img2, None)

#3-1
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
	
#3-2
#flan = cv2.FlannBasedMatcher_create() 
#matches = flan.match(np.float32(des1),np.float32(des2))
	
#4  
matches = sorted(matches, key = lambda m: m.distance)
print('len(matches)=', len(matches))
for i, m in enumerate(matches[:3]):
        print('matches[{}]=(queryIdx:{}, trainIdx:{}, distance:{})'.format(
            i, m. queryIdx, m.trainIdx, m.distance))
	
minDist = matches[0].distance
good_matches = list(filter(lambda m: m.distance<4*minDist, matches))
print('len(good_matches)=', len(good_matches))
if len(good_matches) < 5:
    print('sorry, too small good matches')
    exit()
    
dst = cv2.drawMatches(img1,kp1,img2, kp2, good_matches, None, flags=2) #matches 넣게 되면 더 많은 개수를 넣게 됨
# flags = 0 : 모든 매치 표시
# flags = 2 : 일치되는 특성 포인트만 표시
cv2.imshow('dst',  dst)

#5
src1_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches]) # good match에 있는 모든 포인트를 src1_pts에 넣음
src2_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches]) # good match에 있는 모든 포인트를 src2_pts에 넣음

H, mask = cv2.findHomography(src1_pts, src2_pts, cv2.RANSAC, 3.0)#cv2.LMEDS
# 쌍으로 이루어진 좌표를 이용해서 변환행렬을 구한다. 어떤 행렬을 곱하면 모양이 나올것인가 하는 변환행렬을 계산해준다.
mask_matches = mask.ravel().tolist() # list(mask.flatten())
# ravel() : 다차원 배열(array)을 1차원 배열로 평평하게 펴주는 NumPy 함수

#6
h,w = img1.shape
pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
# 이미지1에서의 양 끝 4개의 점을 표현함, 직사각형
pts2 = cv2.perspectiveTransform(pts, H)
# 앞에서 구한 변환행렬을 넣은 것

src2 = cv2.polylines(src2,[np.int32(pts2)],True,(255,0, 0),2)
# 바뀌어진 4개의 점을 가지고 직선 4개를 그린 것
draw_params = dict(matchColor = (0,255,0), singlePointColor = None,
                 matchesMask = mask_matches, flags = 2)
dst2 = cv2.drawMatches(src1, kp1,src2, kp2, good_matches, None, **draw_params)  
cv2.imshow('dst2',  dst2)

cv2.waitKey()
cv2.destroyAllWindows()
