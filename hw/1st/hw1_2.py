import cv2
import numpy as np

click_list=[]
global edge_points

def onMouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        click_list.append((x, y))
        cv2.circle(param[0], (x, y), 5, (0, 255, 0), -1)

        # print(click_list)
        cv2.imshow('Drawing', param[0])

        if len(click_list) == 4: # 모서리 4개의 점을 모두 클릭한 경우
            edge_points = np.float32(
                [list(click_list[0]), list(click_list[1]), list(click_list[2]), list(click_list[3])])

            transform = cv2.getPerspectiveTransform(edge_points, src_points)
            result = cv2.warpPerspective(img, transform, (cols, rows))

            drows, dcols, channel = logo2.shape
            roi = result[0:drows, 0:dcols]

            # 1번째 방법
            # gray = cv2.cvtColor(logo2, cv2.COLOR_BGR2GRAY)
            # ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
            # mask_inv = cv2.bitwise_not(mask)
            # src1_bg = cv2.bitwise_and(roi, roi, mask=mask)
            # src2_bg = cv2.bitwise_and(logo2, logo2, mask=mask_inv)
            # dst = cv2.bitwise_or(src1_bg, src2_bg)

            # 2번째 방법 - 로고가 더 뚜렷하게 나오는 것 같다
            dst = cv2.bitwise_and(roi, logo2)
            result[0:drows, 0:dcols] = dst

            cv2.imshow("result", result)
            #cv2.imwrite('./result.jpg', result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

imageFile='./drawing.jpg'
logoFile='./duksung_symbol2.png'

img = cv2.imread(imageFile)
logo = cv2.imread(logoFile)
logo2 = cv2.resize(logo, dsize=(100, 100))  # 사진 크기 변환
# print(img.shape) # (960, 960, 3)

rows, cols = img.shape[:2]
src_points = np.float32([[0, 0], [0, rows], [rows, cols], [cols, 0]]) # window 창의 모서리 4 부분

cv2.imshow('Drawing', img) # 윈도우 이름, 사진
cv2.setMouseCallback('Drawing', onMouse, [img])
cv2.waitKey(0)
cv2.destroyAllWindows()





