import cv2, pafy
import numpy as np

# 1. 동공(눈동자) 검출 코드

cap = cv2.VideoCapture('eyes.mp4')  # 동영상 파일 이름

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter('eyes_circle.MP4', 0x7634706d, 25, frame_size, isColor=True)

while (True):
    retval, frame = cap.read()
    original = np.copy(frame)
    if not retval:
        break

    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray1", gray1)
    # gray2 = cv2.GaussianBlur(gray1, ksize=(3, 3), sigmaX=0.0)
    # cv2.imshow("gray2", gray2)
    # ret, binary = cv2.threshold(gray2, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # cv2.imshow("binary", binary)
    # edges = cv2.Canny(binary, 50, 100)
    # cv2.imshow("edges", edges)
    circles1 = cv2.HoughCircles(gray1, method=cv2.HOUGH_GRADIENT,
                                dp=1, minDist=77, param2=25, minRadius=42, maxRadius=62
                                )
    i = 0
    for circle in circles1[0, :]:
        cx, cy, r = circle
        if (i >= 1):  # 동공을 둘러싸고 있는 원 한 개만 나오게 하기 위해서
            continue
        cv2.circle(frame, (cx, cy), r, (0, 0, 255), 2)
        i = i + 1
        print(r)

    # cv2.imshow('original', original)
    # cv2.imshow('gray1', gray1)
    # cv2.imshow('gray2', gray2)
    # cv2.imshow('binary', binary)
    # cv2.imshow('edges', edges)
    cv2.imshow('frame', frame)
    out.write(frame)

    key = cv2.waitKey(25)
    if key == 27:  # Esc
        break

if cap.isOpened():  # 읽은 동영상이 있다면 release 해주어야 한다
    cap.release()

out.release()
cv2.destroyAllWindows()

# 2 각종 동전 분류

# 3coin1.png, 3coin2.png, 3coin3.png, 3coin4.png까지는 같은 소스코드를 사용했습니다.

list = ['3coin1.png', '3coin2.png', '3coin3.png', '3coin4.png']
url = './3coins/'

for i in list:
    src1 = cv2.imread(url + i)
    gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray1", gray1)
    gray2 = cv2.GaussianBlur(gray1, ksize=(3, 3), sigmaX=10.0)
    #cv2.imshow("gray2", gray2)
    ret, binary = cv2.threshold(gray2, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow("binary", binary)
    edges = cv2.Canny(binary, 50, 200)
    #cv2.imshow("edges", edges)
    circles1 = cv2.HoughCircles(edges, method=cv2.HOUGH_GRADIENT,
                                dp=1, minDist=50, param2=15, minRadius=30, maxRadius=80)

    for circle in circles1[0, :]:
        cx, cy, r = circle
        cv2.circle(src1, (cx, cy), r, (0, 0, 255), 2)
    cv2.imshow('src1', src1)
    # cv2.imwrite("./3coin4_hough.png", src1)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 3coin5.png 동전 분류용 소스코드

src1 = cv2.imread('./3coins/3coin5.png')
gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray1", gray1)
gray2 = cv2.GaussianBlur(gray1, ksize=(5, 5), sigmaX=4.0)
#cv2.imshow("gray2", gray2)
ret, binary = cv2.threshold(gray2, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow("binary", binary)
edges = cv2.Canny(binary, 50, 200)
#cv2.imshow("edges", edges)
circles1 = cv2.HoughCircles(edges, method=cv2.HOUGH_GRADIENT,
                            dp=1, minDist=50, param2=20, minRadius=30, maxRadius=75)

for circle in circles1[0, :]:
    cx, cy, r = circle
    cv2.circle(src1, (cx, cy), r, (0, 0, 255), 2)
cv2.imshow('src1', src1)
# cv2.imwrite("./3coin5_hough.png", src1)
cv2.waitKey()
cv2.destroyAllWindows()

# 3coin6.png 동전 분류용 소스코드

src1 = cv2.imread('./3coins/3coin6.png')
gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray1", gray1)
gray2 = cv2.GaussianBlur(gray1, ksize=(3, 3), sigmaX=0.0)
#cv2.imshow("gray2", gray2)
binary = cv2.adaptiveThreshold(gray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 7)
#cv2.imshow('dst3', binary)
edges = cv2.Canny(binary, 100, 200)
#cv2.imshow("edges", edges)
circles1 = cv2.HoughCircles(edges, method=cv2.HOUGH_GRADIENT,
                            dp=1, minDist=60, param2=17, minRadius=18, maxRadius=40)

for circle in circles1[0, :]:
    cx, cy, r = circle
    cv2.circle(src1, (cx, cy), r, (0, 0, 255), 2)
cv2.imshow('src1', src1)
# cv2.imwrite("./3coin6_hough.png", src1)
cv2.waitKey()
cv2.destroyAllWindows()
