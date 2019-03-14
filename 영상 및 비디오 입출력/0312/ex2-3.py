import cv2 # OpenCV 라이브러리 import
from matplotlib import pyplot as plt # matplotlib.pyplot 라이브러리 import

imageFile = '../data/lena.jpg' # 영상 파일 이름

#imgBGR = cv2.imread(imageFile) # cv2.IMREAD_COLOR
imgBGR = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE) 

imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(6, 6))
plt.subplots_adjust(left=0.1, right =0.9, bottom=0, top=1)
#plt.axis('off') #x축, y축을 보여주지 않음

#plt.imshow(imgBGR) # <- cv2.imshow(imgBGR)
#plt.imshow(imgRGB)
plt.imshow(imgBGR, cmap = "gray", interpolation='bicubic')
#interpolation 중간색 색칠하는 속성.. 보관.. 
#color map = cmap 의 속성을 gray로 저장해줘야 GRAYSCALE 로 출력 가능
plt.savefig('../data/lena0314.jpg')
plt.show()

