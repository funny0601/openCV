import cv2
import numpy as np
import matplotlib as plt

cap = cv2.VideoCapture('./vtest.avi')

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size=', frame_size)

count = 0

while True:
    retval, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    count += 1

    if not retval:
        break

    cv2.imshow('frame', frame)

    if count ==1:
        roi = cv2.selectROI('frame', frame)  # 특정영역 선택
        print('roi =', roi)

        roi_h = h[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

    else:
        print('enter')

        hist = cv2.calcHist([roi_h], [0], None, [64], [0, 256])
        backP = cv2.calcBackProject([h.astype(np.float32)], [0], hist, [0, 256], scale=1.0)

        hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN + cv2.SORT_DESCENDING)
        k = 1
        T = hist[k][0] - 1  # threshold
        print('T =', T)

        ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)
        dst = np.uint8(dst)
        cv2.imshow('frame', dst)

    key = cv2.waitKey(25)
    if key == 27:  # esc
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()