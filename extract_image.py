import cv2
c = 1
cap = cv2.VideoCapture(0)

while(c<=60):
    ret, frame=cap.read()
    cv2.imwrite('pic%d.jpg'%c,frame)
    c+=1



