import cv2                  # OpenCV 라이브러리 import

imageFile = '../data/lena.jpg'  # 영상 파일 이름

img = cv2.imread(imageFile) # cv2.IMREAD_COLOR
#img = cv2.imread(imageFile, 1)
#img = cv2.imread(imageFile, cv2.IMREAD_COLOR)

img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE
#img2 = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

#.하나는 현재 위치 
cv2.imwrite('../data/Lena.bmp', img) #확장자에 맞춰서 저장
cv2.imwrite('../data/Lena.png', img)
cv2.imwrite('../data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('../data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])


cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
