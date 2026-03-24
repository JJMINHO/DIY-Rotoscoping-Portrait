import cv2
import numpy as np
import datetime  #현재 시각을 이용하여 이미지를 저장하기 위해 추가

#이미지 읽어들이기(다른 이미지 가공을 원하는 경우 파일명을 변경하여 이미지 가공)
img = cv2.imread('lincecum.jpeg')

#이미지 읽어들이기 실패한 경우
if img is None:
    print("이미지를 찾을 수 없습니다. 파일명을 확인해주세요!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
color = cv2.bilateralFilter(img, 9, 300, 300)
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Cartoon Rendering", cartoon)

key = cv2.waitKey(0)

#입력된 키가 's' 또는 'S'인 경우 저장
if key == ord('s') or key == ord('S'):
    #현재 시간을 '년월일_시분초' 형태의 문자열로 변환
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    #현재 시각을 이용해 이미지 파일이름 지정
    filename = f'cartoon_{now}.jpg'

    cv2.imwrite(filename, cartoon)
    print(f'[{filename}] 사진 변환 후 저장 완료!')

cv2.destroyAllWindows()