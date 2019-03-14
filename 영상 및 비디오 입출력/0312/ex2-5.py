import cv2 # OpenCV 라이브러리 import
from matplotlib import pyplot as plt # matplotlib.pyplot 라이브러리 import

imageFile = '../data/lena.jpg' # 영상 파일 이름

imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6))
#가로, 세로의 길이를 6인치로 설정 
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(imgGray, cmap = 'gray')

plt.axis('tight')
#plt.axis('off')
plt.savefig('../data/0205.png')
plt.show()
