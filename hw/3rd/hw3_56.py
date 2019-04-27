
import cv2, pafy
import numpy as np

url = 'https://www.youtube.com/watch?v=c46LnQ38LRQ'
video = pafy.new(url)
best = video.getbest(preftype='webm')

cap = cv2.VideoCapture(best.url)

while (True):
    retval, frame = cap.read()
    original = np.copy(frame)
    if not retval:
        break

    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray1", gray1)
    gray2 = cv2.GaussianBlur(gray1, ksize=(3, 3), sigmaX=10.0)
    cv2.imshow("gray2", gray2)
    ret, binary = cv2.threshold(gray2, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)
    edges = cv2.Canny(binary, 50, 200)
    cv2.imshow("edges", edges)
    circles1 = cv2.HoughCircles(edges, method=cv2.HOUGH_GRADIENT,
                                dp=1, minDist=50, param2=15, minRadius=0, maxRadius=50)
    for circle in circles1[0,:]:
        cx, cy, r  = circle
        cv2.circle(frame, (cx, cy), r, (0,0,255), 2)

    cv2.imshow('original', edges)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27:  # Esc
        break

cv2.destroyAllWindows()
