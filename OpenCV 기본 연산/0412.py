# 0412.py
import cv2
src = cv2.imread('./data/lena.jpg')

b, g, r = cv2.split(src)
dst = cv2.merge([b, g, r]) # cv2.merge([r, g, b])

print(type(dst))
print(dst.shape)
cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
