import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')
# 얼굴의 특징이 미리 학습된 파일들을 가지고 오겠다. (사람 정면 얼굴)

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')
# 파일이 없다면 오류 띄움

cap = cv2.VideoCapture('../data/mcem0_sa1.mp4') # 얼굴 인식할 동영상 가져오기
scaling_factor = 0.5

while True:
    ret, frame = cap.read()

    if not ret:
            break
    # frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    # 스케일링하면 사이즈 조절됨
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # cascade 적용을 위해서 gray 영상으로 변환

    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5) # xml읽어들인 객체의 영상에서 찾아진 얼굴의 사각형 범위
    # 찾은 얼굴의 개수만큼 여러개 생김

    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3) # 그 범위에 대해서 원래 이미지 frame에 사각형 초록색으로 그리기
        # 이 값들을 이용해서 사각형을 그림
    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
