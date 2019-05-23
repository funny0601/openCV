# 0919.py
import cv2

print(cv2.__version__ )
src1 = cv2.imread('stitch_image1.jpg')
src2 = cv2.imread('stitch_image2.jpg')
src3 = cv2.imread('stitch_image3.jpg')
src4 = cv2.imread('stitch_image4.jpg')

#src1= cv2.resize(src1, dsize=(480, 640))
# 영상 너무 작으면 안 될 수도 있다.
# 테스트로 쓰이는 이미지가 많다. 영상을 붙여서 하나로 출력해야해서 ..

#stitcher = cv2.createStitcher() #이제 메소드 이름 아래처럼 바뀜
stitcher = cv2.Stitcher.create()


status, dst2 = stitcher.stitch((src1, src2)) # 결합해서 dst2를 만들고
status, dst3 = stitcher.stitch((dst2, src3)) # dst2에 src3를 결합하고
status, dst4 = stitcher.stitch((dst3, src4)) # dst3에다가 src4를 또 결합해서 dst4를 만든다

cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.imshow('dst4',  dst4)

#status, dst = stitcher.stitch((src1, src2, src3, src4))
#cv2.imwrite('stitch_out.jpg', dst)
#cv2.imshow('dst',  dst)

cv2.waitKey()
cv2.destroyAllWindows()
