# 0408.py
import cv2
 
src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROIs('src', src, False, True)
print('rects =', rects)

for r in rects:
    cv2.rectangle(src, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)    
##    img = src[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
##    cv2.imshow('Img', img)
##    cv2.waitKey()

cv2.imshow('src', src)
cv2.waitKey()    
cv2.destroyAllWindows()
