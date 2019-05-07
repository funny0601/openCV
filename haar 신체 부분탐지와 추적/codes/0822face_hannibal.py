import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')
# xml을 읽어서 얼굴을 검출할 수 있는 분류기를 만듬

face_mask = cv2.imread('../data/mask_hannibal1.png')
h_mask, w_mask = face_mask.shape[:2]
# 가면에 해당되는 영상을 저장

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')
# xml을 찾을 수 없을 경우, path위치를 잘 정해주라는 경고 띄움

cap = cv2.VideoCapture("../data/mcem0_sa1.mp4")
scaling_factor = 0.5

# 동영상 처리
while True:
   ret, frame = cap.read()
   if not ret :
        break
#    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# dectectMultiScale의 첫번째 인자는 그레이 스케일이기 때문에
   face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
   # 검출된 정보를 face_rects에 저장
   # 여러개가 저장되어 있을 수 있기 때문에 for문으로 돌림
   for (x,y,w,h) in face_rects:
        # 사각형이 있다면, (면적을 가지고 있다면)
        if h > 0 and w > 0:
            # 코 밑부분에 들어가는 마스크인데,
            # 얼굴 전체를 표시하는 게 안 맞아서 그냥 크기 조절용

            #x = int(x + 0.1*w)
            y = int(y + 0.4*h) # y의 위치를 약간 내림
            # w = int(0.8 * w)
            h = int(0.75 * h) # 길이도 약간 줄임

            frame_roi = frame[y:y+h, x:x+w] #얼굴에 해당하는 부분 자르고
            face_mask_small = cv2.resize(face_mask, (w, h), interpolation=cv2.INTER_AREA)
            # 마스크를 크기에 맞게 자르고
            gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_mask, 150, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)
            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)

   cv2.imshow('Face Detector', frame)

   c = cv2.waitKey(1)
   if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
