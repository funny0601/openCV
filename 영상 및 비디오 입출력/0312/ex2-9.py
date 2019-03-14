import cv2, pafy # pafy 라이브러리 import

url = 'https://www.youtube.com/watch?v=sDtTLWKSYUQ'
# 크림히어로즈 동영상 url 
video = pafy.new(url)

print('title = ', video.title)
# title =  고양이 진짜 어디까지 들어갈 수 있을까?
print('video.rating = ', video.rating)
# video.rating =  None
print('video.duration = ', video.duration)
# video.duration =  00:07:52
best = video.getbest(preftype='webm') # 'mp4','3gp'
print('best.resolution', best.resolution)
# best.resolution 640x360

cap=cv2.VideoCapture(best.url)

while(True):
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame',frame)
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
    
cv2.destroyAllWindows()
