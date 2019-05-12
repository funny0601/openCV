import cv2
import pafy

mouth_cascade = cv2.CascadeClassifier('./data/haarcascade_mcs_mouth.xml')

lip_mask = cv2.imread('./data/lip5.png')
h_mask, w_mask = lip_mask.shape[:2]

url = 'https://www.youtube.com/watch?v=B0abXq6bff4'
video = pafy.new(url)
best= video.getbest(preftype='webm')
cap=cv2.VideoCapture(best.url)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter('lip5_mask_final.MP4', 0x7634706d, 25, frame_size, isColor=True)

if mouth_cascade.empty():
	raise IOError('Unable to load the mouth cascade classifier xml file')

while True:
    ret, frame = cap.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.3,11)

    for (x,y,w,h) in mouth_rects:
        w = int(w*2.1)
        h = int(h*0.7)
        x = int(x - 0.10*w)
        y = int(y - 0.15*h)
        # cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

        frame_roi = frame[y:y + h, x:x + w]  # 얼굴에 해당하는 부분 자르고
        face_mask_small = cv2.resize(lip_mask, (w, h), interpolation=cv2.INTER_AREA)
        # 마스크를 크기에 맞게 자르고
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)

        ret, mask = cv2.threshold(gray_mask, 150, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)
        masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
        frame[y:y + h, x:x + w] = cv2.add(masked_face, masked_frame)

        break

    cv2.imshow('Mouth Detector', frame)
    out.write(frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
