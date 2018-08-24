import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX


#handCascade = cv2.CascadeClassifier( "cascade2.xml")
faceCascade = cv2.CascadeClassifier( "haarcascade_frontface.xml")   ## 이 xml 파일에 따라 감지하는 모델이 달라짐!
face_x= 0
face_y = 0
face_w = 0
face_h = 0
state = 0
web_cap = cv2.VideoCapture(0)
 
while True:
    ret, frame = web_cap.read()
    blur = cv2.GaussianBlur(frame,(5,5),0) # BLURRING IMAGE TO SMOOTHEN EDGES
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    retval2,thresh1 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#    hands = faceCascade.detectMultiScale(thresh1,1.1,5)  # 선택한 xml 파일로 분석함 뒤에는 임계치
    faces = faceCascade.detectMultiScale(gray,1.1,5,0,(30, 30))   
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (122, 122, 0), 2)
        cv2.putText(frame, 'Face',(x-5,y-5),font,0.9,(255,0,0),2)        
        face_x = x
        face_y = y
        face_w = w
        face_h = h
        
##    hand = handCascade.detectMultiScale(gray,1.3,5,0,(30, 30))
##    for (x, y, w, h) in hand:
##        cv2.rectangle(frame, (x, y), (x+w, y+h), (122, 122, 0), 2)
##        cv2.putText(frame, 'Hand',(x-5,y-5),font,0.9,(0,255,0),2)
##        print(w)
##        print(h)
##        print(face_w)
##        print(face_h)
##        print("-------------")
##        if w> 70 and  h > 70 and face_w > 150 and (face_h) >150 :
##            point1 = np.float32([[face_x,face_y],[face_x,face_y+face_h],[face_x+face_w,face_y],[face_x+face_w,face_y+face_h]])
##            point2 = np.float32([[0,0],[0,face_w],[face_h,0],[face_w,face_h]])
##            P = cv2.getPerspectiveTransform(point1,point2)
##            frame = cv2.warpPerspective(frame,P,(face_w,face_h))
##            cv2.resize(frame,(400,400))
##            cv2.imshow('hand up', frame)
    cv2.resize(frame,(400,400))
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # When everything is done, release the capture
        web_cap.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        break

