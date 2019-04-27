import cv2, pafy  # pafy 라이브러리 import
import numpy as np

url = 'https://www.youtube.com/watch?v=dogNvT_gnvg&list=WL&index=14&t=58s'
video = pafy.new(url)
best = video.getbest(preftype='webm')

cap = cv2.VideoCapture(best.url)

while (True):
    retval, frame = cap.read()
    original = np.copy(frame)
    if not retval:
        break

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blur_img = cv2.GaussianBlur(gray_img, ksize=(3,3), sigmaX = 10.0)
    canny_img = cv2.Canny(blur_img, 70, 210)
    height, width = frame.shape[:2]  
    vertices = np.array(
        [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
        dtype=np.int32)

    color3 = (255, 255, 255)
    color1 = 255
    mask = np.zeros_like(canny_img)  
    if len(canny_img.shape) > 2: 
        color = color3
    else:  
        color = color1

 
    cv2.fillPoly(mask, vertices, color)

    ROI_image = cv2.bitwise_and(canny_img, mask)
    lines = cv2.HoughLinesP(ROI_image, 1, 1* np.pi/180, 30, np.array([]), minLineLength=10,
                            maxLineGap=20)

    line_img = np.zeros((ROI_image.shape[0], ROI_image.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_img , (x1, y1), (x2, y2), (0, 0, 255), 2)
    result = cv2.addWeighted(original, 1, line_img, 1, 0)

    cv2.imshow('original', original)
    cv2.imshow('ROI_image', ROI_image)
    cv2.imshow('frame', canny_img )
    cv2.imshow('result', result)
    key = cv2.waitKey(25)
    if key == 27:  # Esc
        break

cv2.destroyAllWindows()






