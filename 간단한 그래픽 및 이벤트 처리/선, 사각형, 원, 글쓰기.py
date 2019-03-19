import cv2                  # OpenCV 라이브러리 import
 import numpy as np

imageFile = '../data/lena.jpg'  # 영상 파일 이름

img = cv2.imread(imageFile) # cv2.IMREAD_COLOR
 img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE

img = np.zeros((512, 512, 3), dtype=np.uint8) * 255 #배열 생성 및 초기화
#np.ones()

cv2.line(img, (100, 100), (200, 500), (255, 0, 0), 3)
 cv2.rectangle(img, (150, 100), (250, 450), (0, 255, 0), 2)
 cv2.circle(img, (250, 250), 50, (0, 255, 255), -1)

text = "OPENCV programming"
 cv2.putText(img, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
 #글을 쓸 그림, 텍스트, 시작점, 폰트, 폰트 사이즈, 색상, 두께

#cv2.putText(img, 'OPENCV programming'
 cv2.imshow('Lena color',img)
 #cv2.imshow('Lena grayscale',img2)

cv2.waitKey(0)
 cv2.destroyAllWindows()
