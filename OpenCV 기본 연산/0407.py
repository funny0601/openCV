# 0407.py
import cv2
 
src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)
# ('src', src, True, False)
# (windowName, img,showCrossair, fromCenter)
# roi = [x, y, w, h]
# 끝나는 점의 좌표: [x:x+w, y:y+h]
print('roi =', roi)

img = src[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
# 특정 영역을 저장 
# src[y:y+h, x:x+w]
# 이미지에 대한 정보는 y의 값이 먼저 오고 x의 값이 나중에 온다

cv2.imshow('Img', img)
cv2.waitKey()
cv2.destroyAllWindows()
