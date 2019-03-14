import cv2 # OpenCV 라이브러리 import
from matplotlib import pyplot as plt # matplotlib.pyplot 라이브러리 import

imageFile = '../data/lena.jpg' # 영상 파일 이름

imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap = "gray", interpolation='bicubic')
plt.show()
