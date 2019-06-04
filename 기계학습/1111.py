#1111.py
import cv2
import numpy as np

#1
ann = cv2.ml_ANN_MLP.load('./mnist/ann-minist_2layer_BP.train')
##ann = cv2.ml_ANN_MLP.load('./mnist/ann-minist_2layer_100RPROP.train')
##ann = cv2.ml_ANN_MLP.load('./mnist/ann-minist_3layer_50RPROP.train')

#2
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(dst, (x, y), 10, (255, 255, 255), -1)
    cv2.imshow('dst', dst)
    
dst  = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
cv2.imshow('dst',dst)
cv2.setMouseCallback('dst', onMouse)
    
mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
font = cv2.FONT_HERSHEY_SIMPLEX  
x_img = np.zeros(shape=(28, 28), dtype=np.uint8)    # 입력이미지(28*28)
#3
while True:
    key = cv2.waitKey(25)    
    if key == 27: 
        break;
    elif key == ord('r'):  # 화면 클리어
        dst[:,:] = 0
        cv2.imshow('dst',dst)
    elif key == ord(' '):
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(gray, mode, method)
        # 윤곽선 검출
        for i, cnt in enumerate(contours):
#3-1    # 모든 윤곽선에 대해서 ..
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(dst, (x, y), (x+width, y+height), (0,0,255), 2)
            cx, cy = x + width/2, y + height/2
            if width > height:
                r = width/2
            else:
                r = height/2            
##            (cx,cy),r = cv2.minEnclosingCircle(cnt)
            cx, cy, r= int(cx), int(cy), int(r)
            img = gray[cy-r:cy+r, cx-r:cx+r]
            img = cv2.resize(img, dsize=(20, 20),interpolation=cv2.INTER_AREA) # 양 옆에 4 정도의 테두리를 준다. 그래서 20+4+4 크기가 된다
            x_img[:,:] = 0
            x_img[4:24, 4:24] = img     # 입력이미지에 숫자 넣기
            x_img = cv2.dilate(x_img, None, 2)
            x_img = cv2.erode(x_img, None, 4)
            cv2.imshow('x_img', x_img)
#3-2
            x_test = np.float32(x_img.flatten()) # 2차원 영상을 신경망을 위한 1차원 배열로
            _, res = ann.predict(x_test.reshape(-1, 784)) # 입력이미지에 대한 신경망 결과, 10개의 숫자에 대한 확률을 반환
            print('res=', res)
            y_predict = np.argmax(res, axis = 1) # 10개의 숫자에 대한 결과값 중 가장 큰 값을 갖는 숫자
            print('y_predict=', y_predict)
            digit = int(y_predict[0])
            cv2.putText(dst, str(digit), (x, y), font, 3, (255,0,0), 5)
        
        cv2.imshow('dst',dst)
cv2.destroyAllWindows()
