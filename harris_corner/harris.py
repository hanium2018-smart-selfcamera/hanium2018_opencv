import numpy as np
import cv2 as cv
filename = 'chessboard.png'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#특징점 좌표 추출
dst = cv.dilate(dst,None)
# 임계값 조절 , 이미지에 따라 실험해야함 0.001이상의 값들만 산출
img[dst>0.01*dst.max()]=[0,0,255]      #산출된 특징점 표기
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
