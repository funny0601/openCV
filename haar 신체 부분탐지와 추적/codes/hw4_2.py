import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')
mouth_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_mcs_mouth.xml')

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')
# 파일이 없다면 오류 띄움

cap = cv2.VideoCapture('../data/주디_Trim.mp4') # 얼굴 인식할 동영상 가져오기
scaling_factor = 0.5

while True:
    ret, frame = cap.read()

    if not ret:
            break
    # frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    # 스케일링하면 사이즈 조절됨
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # cascade 적용을 위해서 gray 영상으로 변환

    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5) # xml읽어들인 객체의 영상에서 찾아진 얼굴의 사각형 범위
    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3) # 그 범위에 대해서 원래 이미지 frame에 사각형 초록색으로 그리기
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        mouths = mouth_cascade.detectMultiScale(roi_gray)
        for (mx, my, mw, mh) in mouths:
            cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (255, 0, 0), 2)

    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()



