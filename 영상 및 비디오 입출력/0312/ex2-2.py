import cv2 # OpenCV 라이브러리 import

imageFile = './data/lena.jpg'   # 영상 파일 이름

img = cv2.imread(imageFile) # cv2.imread(imageFile, cv2.IMREAD_COLOR)

cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
