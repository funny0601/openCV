# 0703.py
import cv2
import numpy as np

src = cv2.imread('../data/rect.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 100)
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180.0, threshold=100)
print('lines.shape=', lines.shape)

for line in lines:
    x1, y1, x2, y2   = line[0]
    cv2.line(src,(x1,y1),(x2,y2),(0,0,255),2)
    
cv2.imshow('edges',  edges)
cv2.imshow('src',  src)
cv2.waitKey()
cv2.destroyAllWindows()
