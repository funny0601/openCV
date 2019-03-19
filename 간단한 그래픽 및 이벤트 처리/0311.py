#0311.py
import numpy as np
import cv2

def onMouse(event, x, y, flags, param): # param = [img], param[0] = img
##    global img
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 누르면 
        if flags & cv2.EVENT_FLAG_SHIFTKEY: # shift키도 동시에 누른 상태라면 
            cv2.rectangle(param[0], (x-5, y-5), (x+5, y+5), (255, 0, 0))
        else:
            cv2.circle(param[0], (x, y), 5, (255, 0, 0), 3)
    elif event == cv2.EVENT_RBUTTONDOWN: # 오른쪽 버튼을 누르면 
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)        
    elif event == cv2.EVENT_LBUTTONDBLCLK: # 왼쪽 버튼 더블 클릭 시 
        param[0] = np.zeros(param[0].shape, np.uint8) + 255  # 하얗게 지우겠다  
    cv2.imshow("img", param[0])
    
img = np.zeros((512,512,3), np.uint8) + 255
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, [img])
# 마우스 이벤트가 발생할 때 마다 두 번째 인자의 함수 호출
# [img]: 함수 호출 시 전달되는 매개변수 
cv2.waitKey()
cv2.destroyAllWindows()
