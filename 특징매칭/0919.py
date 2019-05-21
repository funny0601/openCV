# 0919.py
import cv2

src1 = cv2.imread('stitch_image1.jpg')
src2 = cv2.imread('stitch_image2.jpg')
src3 = cv2.imread('stitch_image3.jpg')
src4 = cv2.imread('stitch_image4.jpg')

#stitcher = cv2.createStitcher()
stitcher = cv2.Stitcher.create()

status, dst2 = stitcher.stitch((src1, src2))
status, dst3 = stitcher.stitch((dst2, src3))
status, dst4 = stitcher.stitch((dst3, src4))

cv2.imshow('dst2',  dst2)
#cv2.imshow('dst3',  dst3)
#cv2.imshow('dst4',  dst4)

status, dst = stitcher.stitch((src1, src2, src3, src4))
#cv2.imwrite('stitch_out.jpg', dst)
#cv2.imshow('dst',  dst)

cv2.waitKey()
cv2.destroyAllWindows()
