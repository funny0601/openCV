import cv2
import numpy as np
import pafy

mouth_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_mcs_mouth.xml')


url = 'https://www.youtube.com/watch?v=CW25i2oiTvw'
video = pafy.new(url)
best= video.getbest(preftype='webm')
cap=cv2.VideoCapture(best.url)


if mouth_cascade.empty():
	raise IOError('Unable to load the mouth cascade classifier xml file')

# cap = cv2.VideoCapture("../data/mcem0_sa1.mp4")
ds_factor = 0.5

while True:
    ret, frame = cap.read()
#    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.3, 11)
        # parameter값을 수정해서 찾을 수 있다

    for (x,y,w,h) in mouth_rects:
        y = int(y - 0.15*h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        break

    cv2.imshow('Mouth Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
