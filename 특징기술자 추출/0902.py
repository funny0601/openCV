# 0902.py
import cv2
import numpy as np

print(cv2.__version__ )
src = cv2.imread('chessBoard.jpg')
gray= cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#1
fastF = cv2.FastFeatureDetector_create() # (threshold=30) # 100 # threshold 값을 80으로 늘리게 되면 키포인트 개수가 줄어들게 된다
# detect할 때 그 계산된 키포인트 값이 80 이상인 애들만 리턴
# 강도가 센 애들만 고를 수도 있다
# threshold = 100 하게 되면 8개만 추출하게 됨
kp = fastF.detect(gray)  # 키포인트 리턴
dst = cv2.drawKeypoints(gray, kp, None, color=(255,0,0)) # 키포인트 그림
print('len(kp)=', len(kp))
cv2.imshow('dst',  dst)

fastF.setNonmaxSuppression(False)	# Keypoints 중복제거를 안함(false) / True
kp2 = fastF.detect(gray)
dst2 = cv2.drawKeypoints(src, kp2, None, color=(0,0,255))
print('len(kp2)=', len(kp2))
#cv2.imshow('dst2',  dst2)

dst3 = src.copy()
points = cv2.KeyPoint_convert(kp)	# Keypoints의 타입이 Point로 변환 / kp2
for cx, cy in points:
    cv2.circle(dst3, (cx, cy), 3, color=(255, 0, 0), thickness=1)
#cv2.imshow('dst3',  dst3)

#2
dst4 = dst.copy()
kp3 = sorted(kp, key=lambda f: f.response, reverse=True) # kp2
cv2.drawKeypoints(gray, kp3[:10], dst4, color=(0,0,255),
                 flags = cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
#cv2.imshow('dst4',  dst4)

#3
kp4 = list(filter(lambda f: f.response>50, kp))
print('len(kp4)=', len(kp4))
#for f in kp2:
#    print(f.response)

dst5 = cv2.drawKeypoints(gray, kp4, None, color=(0,0,255))   
#cv2.imshow('dst5',  dst5)

#4
def distance(f1, f2):    
    x1, y1 = f1.pt
    x2, y2 = f2.pt
    return np.sqrt((x2 - x1)**2+ (y2 - y1)**2)

def filteringByDistance(kp, distE=0.5):
    size = len(kp)
    mask = np.arange(1,size+1).astype(np.bool8) # all True   
    for i, f1 in enumerate(kp):
        if not mask[i]:
            continue
        else: # True
            for j, f2 in enumerate(kp):
                if i == j:
                    continue
                if distance(f1, f2)<distE:
                    mask[j] = False
    np_kp = np.array(kp)
    return list(np_kp[mask])

kp5 = filteringByDistance(kp4, 30)
print('len(kp5)=', len(kp5))
dst6 = cv2.drawKeypoints(gray, kp4, None, color=(0,0,255))
#cv2.imshow('dst6',  dst6)

cv2.waitKey()
cv2.destroyAllWindows()
