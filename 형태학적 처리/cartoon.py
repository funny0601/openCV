import cv2
import numpy as np

### 웹툰처럼 보이게 하기 ###

#img = cv2.imread('./lena.jpg')
#cv2.imshow('src', img)

cap = cv2.VideoCapture('./vtest.avi')
while True:
    ret, img = cap.read()
    if ret:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이로 색상 변경
        img_gray = cv2.medianBlur(img_gray, 7) # 잡음 제거

        edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 5)
        ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV) # 흰 바탕에 검은 줄
        #kernel = np.ones((6, 6), np.uint8) # cv2.MORPH_RECT : 정사각형 구조
        # 사각형 사이즈 커질수록 선 자체가 두꺼워 짐
        #mask = cv2.erode(mask, kernel, iterations= 5) # 선이 더 두껍게 나옴

        img_sketch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        ## 값 설정 ##
        sigma_color=5
        sigma_space=7
        size=5

        img_bi = cv2.bilateralFilter(img, size, sigma_color, sigma_space) # 경계 유지

        dst = cv2.bitwise_and(img_bi, img_bi, mask = mask)

        #cv2.imshow('Sketch', img_sketch)
        #cv2.imshow('Sketch', img_bi) # 뽀샵 효과
        cv2.imshow('Sketch', dst)
        key = cv2.waitKey(40) # 매개변수 안의 값은 영상 속도와 관련이 있음
        if key == 27:  # esc
            break
    else:
        break

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()