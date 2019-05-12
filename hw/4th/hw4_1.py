import cv2
import numpy as np

cap = cv2.VideoCapture('Produce.mp4')  # 동영상 파일 이름

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter('가위바위보_판별기.MP4', 0x7634706d, 25, frame_size, isColor=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, bImage = cv2.threshold(gray, 220, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)
    mask_hand2 = cv2.dilate(bImage, None)

    mode = cv2.RETR_EXTERNAL
    method = cv2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(mask_hand2, mode, method)

    dst = frame.copy()
    cnt = contours[0]
    cv2.drawContours(dst, [cnt], 0, (255, 0, 0), 2)

    dst2 = dst.copy()
    rows, cols = dst2.shape[:2]
    hull = cv2.convexHull(cnt, returnPoints=False)
    hull_points = cnt[hull[:, 0]]
    #cv2.drawContours(dst2, [hull_points], 0, (255, 0, 255), 6)

    # 3

    T = 30  # 10
    defects = cv2.convexityDefects(cnt, hull)
    # print('defects.shape=', defects.shape)

    count = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        dist = d / 256
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        #print(end)
        #print('프레임 한개')
        far = tuple(cnt[f][0])

        if dist > T:
                cv2.circle(dst2, end, 5, [0, 128, 255], -1)
                count = count+1

        #print(count)
        #print('그림 그렸음')

    if(count==0):
        cv2.putText(dst2, "Rock", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    elif(count==2):
        cv2.putText(dst2, "Scissors", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    elif count> 3:
        cv2.putText(dst2, "Paper", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # cv2.line(dst2, start, end, [255, 255, 0], 2)
    # cv2.line(dst2, start, far, [0, 255, 0], 1)
    # cv2.line(dst2, end, far, [0, 255, 0], 1)
    # cv2.circle(dst2, far, 5, [0, 0, 255], -1)
    # cv2.circle(dst2, start, 5, [0, 255, 255], -1)

    cv2.imshow('dst2', dst2)
    out.write(dst2)
    #cv2.imshow("Hands", dst)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
