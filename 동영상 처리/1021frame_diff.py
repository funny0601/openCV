import cv2
import numpy as np
from matplotlib import pyplot as plt

def frame_diff1(prev_frame, cur_frame):
    return cv2.absdiff(cur_frame, prev_frame)

def frame_diff2(prev_frame, cur_frame, next_frame):
    diff_frames1 = cv2.absdiff(next_frame, cur_frame)
    diff_frames2 = cv2.absdiff(cur_frame, prev_frame)
    return cv2.bitwise_and(diff_frames1, diff_frames2)

def get_frame(cap):
    ret, frame = cap.read()
    if ret :
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    else :
        return []

if __name__=='__main__':
    cap = cv2.VideoCapture('KBS-Special-2011-10-09.mp4')
    
    prev_frame = get_frame(cap) 
    cur_frame = get_frame(cap) 
    next_frame = get_frame(cap)
    n = cap.get(cv2.CAP_PROP_FRAME_COUNT) # 동영상 총 프레임 수
    diffv = [] # 차영상의 값을 저장

    cv2.imshow("Keyframe0", cur_frame)

    i=0

    while True: # 매 프레임 마다 도는 중
        diff = frame_diff1(prev_frame, cur_frame) # 앞의 영상과 내 영상의 차이를 구함 (차영상)
        #diff = frame_diff2(prev_frame, cur_frame, next_frame)
        cv2.imshow("Difference", diff)
        diffv.append(np.sum(diff)) # 배열안에 있는 값을 다 더함 , 모든 픽셀 값의 합, 차영상의 값

        if np.sum(diff)>10000000:
            cv2.imshow("Keyframe"+str(i),cur_frame)

        prev_frame = cur_frame
        cur_frame = next_frame 
        next_frame = get_frame(cap)
        if next_frame == [] :
            break
        i = i+1

        key = cv2.waitKey(10)
        if key == 27:
            break

    plt.title('Difference')
    plt.plot(diffv, color='r')
    plt.show()

    cv2.destroyAllWindows()
