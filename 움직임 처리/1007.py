# 1007.py
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
          mouse_status = 1    # 마우스 버튼 다운
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

cap = cv2.VideoCapture('ball.wmv')
if (not cap.isOpened()): 
     print('Error opening video')    
height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
roi_mask   = np.zeros((height, width), dtype=np.uint8)
term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS, 10, 1) # 추적에 사용되는 매개변수 : criteria.maxCount, criteria.epsilon 
# max_iter: 추적 반복 횟수
# 주어진 오차가 1보다 작을 때 까지 10번 반복
#3 
t = 0
while True:
     ret, frame = cap.read()
     if not ret: break
     t+=1
#     print('t=',t)
#3-1
#     frame2 = frame.copy() # CamShift
     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # HSV 영상으로 변환
     mask = cv2.inRange(hsv, (0., 60., 32.),(180., 255., 255.)) # S,V의 일부 영역 제외(어둡고 흐릿한 영역)
##     cv2.imshow('mask',mask)
     
#3-2
     if mouse_status==2:      # 마우스 드래깅
          x1, y1, x2, y2 = roi
          cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
          
#3-3
     if mouse_status==3:      # 마우스 버튼 업
          print('initialize....')
          mouse_status = 0    # 마우스 초기화
          x1, y1, x2, y2 = roi
          mask_roi = mask[y1:y2, x1:x2]
          hsv_roi  =  hsv[y1:y2, x1:x2]
          
          hist_roi = cv2.calcHist([hsv_roi],[0],mask_roi,[16],[0,180]) # hsv의 관심영역에서 0번째 채널, 즉 h에 대해 히스토그램 계산
          cv2.normalize(hist_roi,hist_roi,0,255,cv2.NORM_MINMAX) # 히스토그램을 0~255로 정규화
          track_window = (x1, y1, x2-x1, y2-y1)  # 추적창
          tracking_start = True

#3-4
     if tracking_start:
          backP = cv2.calcBackProject([hsv],[0],hist_roi,[0,180],1) # h에 대해 역투영 계산
          backP &= mask       # mask로 이진화
          cv2.imshow('backP',backP)
          
#3-5: meanShift tracking
#          ret, track_window = cv2.meanShift(backP, track_window, term_crit) # 역투영&이진화 영상에 대해 meanShift 실행
#          x,y,w,h = track_window
#          cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

#3-6: camShift tracking
          track_box, track_window = cv2.CamShift(backP, track_window, term_crit) # 역투영&이진화 영상에 대해 CamShift 실행
          x,y,w,h = track_window
          cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)    # 추적창은 Green사각형
          cv2.ellipse(frame, track_box, (0, 255, 255), 2)  # 추적 상자는 노란타원
          pts = cv2.boxPoints(track_box)
          pts = np.int0(pts) # np.int32
          dst = cv2.polylines(frame,[pts],True, (0, 0, 255),2)   # 추적 상자는 Red사각형

#     cv2.imshow('tracking',frame)             # meanShift
     cv2.imshow('tracking',frame) # CamShift

     key = cv2.waitKey(25)
     if key == 27:
          break
     
if cap.isOpened(): cap.release();
cv2.destroyAllWindows()
