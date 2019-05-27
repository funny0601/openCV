# 1005.py
import cv2
import numpy as np

#1
roi  = None
drag_start = None
mouse_status = 0  # 마우스 초기화
tracking_start  = False
def onMouse(event, x, y, flags, param=None):
     global roi
     global drag_start
     global mouse_status
     global tracking_start   
     if event == cv2.EVENT_LBUTTONDOWN:
          drag_start = (x, y)
          mouse_status = 1         # 마우스 버튼 다운
          tracking_start = False
     elif event == cv2.EVENT_MOUSEMOVE:
          if flags == cv2.EVENT_FLAG_LBUTTON:
               xmin = min(x, drag_start[0])
               ymin = min(y, drag_start[1])
               xmax = max(x, drag_start[0])
               ymax = max(y, drag_start[1])
               roi = (xmin, ymin, xmax, ymax)
               mouse_status = 2    # 마우스 드래깅
     elif event == cv2.EVENT_LBUTTONUP:
          mouse_status = 3         # 마우스 버튼 업

#2          
cv2.namedWindow('tracking')
cv2.setMouseCallback('tracking', onMouse)

cap = cv2.VideoCapture('checkBoard3x3.avi')
if (not cap.isOpened()): 
     print('Error opening video')
     
height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) # 프레임과 동일한 크기를 만들어서
roi_mask   = np.zeros((height, width), dtype=np.uint8) # 0으로 초기화 된 배열
#검은색 프레임 하나 만들기

params = dict(maxCorners=16,qualityLevel=0.001,minDistance=10,blockSize=5) # cv2.goodFeaturesToTrack를 위한 특징검출 매개변수
term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS,10,0.01) # cv2.cornerSubPix를 위한 코너 검출 매개변수 : criteria.maxCount, criteria.epsilon
params2 = dict(winSize= (5,5), maxLevel = 3, criteria =  term_crit) # cv2.calcOpticalFlowPyrLK를 위한 추적 매개변수 

#3 
t = 0
while True:
     ret, frame = cap.read()
     if not ret: break
     t+=1
#     print('t=',t)
     imgC = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 그레이 변환
     imgC = cv2.GaussianBlur(imgC, (5, 5), 0.5) # 불필요한 잡음에 의해 optical flow가 계산되지 않게 막으려고
     
#3-1
     if mouse_status==2: # 마우스 드래깅
          x1, y1, x2, y2 = roi
          cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
          
#3-2          
     if mouse_status==3: # 마우스 버튼 업
          print('initialize....')
          mouse_status = 0 # 마우스 초기화
          x1, y1, x2, y2 = roi # 구한 roi영역 꼭짓점을 넣어준다
          roi_mask[:,:] = 0
          roi_mask[y1:y2, x1:x2] = 1
          p1 = cv2.goodFeaturesToTrack(imgC,mask=roi_mask,**params) # 추적을 위한 특징 p1 검출
          if len(p1)>=4:      # 특징점이 4개 이상인 경우
               p1 = cv2.cornerSubPix(imgC, p1, (5,5),(-1,-1), term_crit) # 특징점 p1 위치 미세화
               rect = cv2.minAreaRect(p1)         # 위치 미세화된 특징점 p1의 최소사각형 -> 추적 사각형
               box_pts = cv2.boxPoints(rect).reshape(-1,1,2)
               tracking_start = True
             #트랙킹할 점들만 찾아놓은 상태
               
#3-3               
     if tracking_start:
          p2,st,err= cv2.calcOpticalFlowPyrLK(imgP,imgC,p1,None,**params2) # 이전영상 -> 현영상으로 optical flow 계산
          p1r,st,err=cv2.calcOpticalFlowPyrLK(imgC,imgP,p2,None,**params2) # (optical flow가 구해진) 현영상 -> 이전영상으로 역 optical flow 계산
          # optical flow 잡음에 민감할 수도 있으니 한 번에 계산하면 오차가 있을 수도 있으니 정말 optical flow가 맞는지 확인하는 과정을 거친다
          # 거꾸로 지금 영상에서 이전 프레임에 해당되는 역 optical flow 계산을 하게 된다
          d = abs(p1-p1r).reshape(-1, 2).max(-1)       # 둘의 차이 계산
          stat = d < 1.0  # 두 차이가 1보다 작은 경우만
          good_p2 = p2[stat==1].copy()  # OF에서 good_p2(추적 점)를 선택
          good_p1 = p1[stat==1].copy()  # 이전영상의 good_p2에서 good_p1을 선택
          for x, y in good_p2.reshape(-1, 2):
               cv2.circle(frame, (x, y), 3, (0,0,255), -1) # OF를 현영상에 원으로 그림

          if len(good_p2)<4: # OF의 개수가 4보다 작으면 #3-4로 이동
               continue
          H, mask = cv2.findHomography(good_p1, good_p2, cv2.RANSAC, 3.0)  # good+p1에서 good_p2로 변환행렬 계산
          box_pts = cv2.perspectiveTransform(box_pts, H)                   # 추적 사각형에 적용
          cv2.polylines(frame,[np.int32(box_pts)],True,(255,0, 0),2)
          p1 = good_p2.reshape(-1,1,2)  # good_p2를 p1으로 저장

#3-4
     cv2.imshow('tracking',frame)
     imgP = imgC.copy() # 현영상을 이전영상으로 복사
     
     key = cv2.waitKey(25)
     if key == 27:
          break
     
if cap.isOpened():
     cap.release();
cv2.destroyAllWindows()
