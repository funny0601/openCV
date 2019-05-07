import cv2
import numpy as np
import pafy


face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_eye.xml')

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')

if eye_cascade.empty():
	raise IOError('Unable to load the eye cascade classifier xml file')
# 눈은 귀와 달리 왼쪽, 오른쪽이 비슷한 형태를 가지고 있기 때문에 하나의 classifier를 사용

# cap = cv2.VideoCapture('../data/mcem0_sa1.mp4')
url = 'https://www.youtube.com/watch?v=CW25i2oiTvw'
video = pafy.new(url)
best= video.getbest(preftype='webm')
cap=cv2.VideoCapture(best.url)

ds_factor = 0.5

while True:
    ret, frame = cap.read()
    if not ret:
        break
#    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 일단 얼굴을 먼저 찾는다
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # 찾은 얼굴에 대해서 눈을 찾는다
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (x_eye,y_eye,w_eye,h_eye) in eyes:
            # 원으로 그린 것
            center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
            # 가로의 반+ x좌표, 세로의 반 + y좌표
            radius = int(0.3 * (w_eye + h_eye))
            color = (0, 255, 0)
            thickness = 3
            cv2.circle(roi_color, center, radius, color, thickness)

    cv2.imshow('Eye Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()