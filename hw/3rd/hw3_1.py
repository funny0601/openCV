import cv2, pafy  # pafy 라이브러리 import
import numpy as np

url = 'https://www.youtube.com/watch?v=dogNvT_gnvg&list=WL&index=14&t=80s'
video = pafy.new(url)
best = video.getbest(preftype='webm')

cap = cv2.VideoCapture(best.url)

while (True):
    retval, frame = cap.read()
    original = np.copy(frame);
    if not retval:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100)  # 에지 검출
    lines = cv2.HoughLines(edges, rho=1, theta=np.pi / 180.0, threshold=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print('lines.shape=', lines.shape)

    count = 0
    for line in lines:
        if(count>1):
            break
        rho, theta = line[0]
        c = np.cos(theta)
        s = np.sin(theta)
        x0 = c * rho
        y0 = s * rho
        x1 = int(x0 + 1000 * (-s))
        y1 = int(y0 + 1000 * (c))
        x2 = int(x0 - 1000 * (-s))
        y2 = int(y0 - 1000 * (c))
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        count = count+1

    cv2.imshow('original', edges)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27:  # Esc
        break

cv2.destroyAllWindows()






