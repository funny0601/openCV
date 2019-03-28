# 0416.py
import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg')

rows, cols, channels = src.shape
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  45, 0.5 )
M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )
# 회전에서 -θ는 반대방향으로 세타(θ)만큼 회전을 의미,
# -부호는 반대방향을 의미한다.

#dst1 = cv2.warpAffine( src, M1, (rows, cols))
#dst2 = cv2.warpAffine( src, M2, (rows, cols))

#cv2.imshow('dst1',  dst1)
#cv2.imshow('dst2',  dst2)


#Horizontal 대칭
#src_points=np.float32([[0,0],[cols-1,0],[0,rows-1]])#[x,y]
#dst_points=np.float32([[cols-1,0],[0,0],[cols-1,rows-1]])


#Vertical
#src_points=np.float32([[0,0],[cols-1,0],[0,rows-1]])#[x,y]
#dst_points=np.float32([[0,rows-1],[cols-1,rows-1],[0,0]])


#affineM=cv2.getAffineTransform(src_points,dst_points)
#img_sym=cv2.warpAffine(src,affineM,(cols,rows))


src_points = np.float32([[0,0], [0,rows-1], [cols/2,0],[cols/2,rows-1]])
#dst_points = np.float32([[0,50], [0,rows-51], [cols/2,0],[cols/2,rows-1]])
dst_points = np.float32([[0,100], [0,rows-51], [cols/2,0],[cols/2,rows-1]])  #조금더 찌그러지게..

affineM=cv2.getPerspectiveTransform(src_points,dst_points)
img_sym=cv2.warpPerspective(src,affineM,(cols,rows))


cv2.imshow('dst3', img_sym)

cv2.waitKey()    
cv2.destroyAllWindows()
