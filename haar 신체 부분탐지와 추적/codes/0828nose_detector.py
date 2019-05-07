import cv2
import numpy as np
import pafy

nose_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_mcs_nose.xml')

url = 'https://www.youtube.com/watch?v=CW25i2oiTvw'
video = pafy.new(url)
best= video.getbest(preftype='webm')
cap=cv2.VideoCapture(best.url)


if nose_cascade.empty():
	raise IOError('Unable to load the nose cascade classifier xml file')

# cap = cv2.VideoCapture("../../data/mcem0_sa1.mp4")
ds_factor = 0.5

while True:
    ret, frame = cap.read()
#    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    # parameter 값에 따라서 달라진다
    for (x,y,w,h) in nose_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        break

    cv2.imshow('Nose Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
