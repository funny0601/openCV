#동영상 처리의 기본 
import cv2

##cap = cv2.VideoCapture(0) # 0번 카메라 (카메라가 1대일 경우 보통 0을 사용) 
cap = cv2.VideoCapture('../data/vtest.avi') # 동영상 파일 이름

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

while True:
    retval, frame = cap.read() # 1개의 프레임 캡처
    if not retval: # 동영상이 끝나서 프레임을 더 이상 불러올 수 없을 때 
        break
    cv2.imshow('frame',frame) # 읽어들인 프레임을 화면에 보여준다 
    key = cv2.waitKey(25) # 25 밀리세컨드 기다렸다가 key를 넣어준다  
    if key == 27: # 키가 27일 경우 = Esc
        break
    
if cap.isOpened(): # 읽은 동영상이 있다면 release 해주어야 한다
    cap.release()
    
cv2.destroyAllWindows()
