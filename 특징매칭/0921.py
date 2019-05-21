# 0921.py
import cv2
 
#1
cap = cv2.VideoCapture('stitch_videoInput.mp4')
t = 0 
images = []
STEP = 20
while True:
    t += 1
    retval, frame = cap.read()
    if not retval:
        break
    img = cv2.resize(frame, dsize=(640, 480))
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    if t%STEP == 0:
        images.append(img)
        
    cv2.imshow('img',img)
    key = cv2.waitKey(10)
    if key == 27: # Esc
        break

#2
print('len(images)=', len(images))
#stitcher = cv2.createStitcher()
stitcher = cv2.Stitcher.create()
status, dst = stitcher.stitch(images)
if status == cv2.STITCHER_OK:
    cv2.imwrite('video_stitch_out.jpg', dst)
    cv2.imshow('dst',dst)
    cv2.waitKey()

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
