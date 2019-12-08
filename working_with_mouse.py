import cv2
img=cv2.imread('lena.jpg')
cv2.imshow('image',img)

def click_event(event ,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(x)+','+str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,0,0),1)
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_COMPLEX
        text_color=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,text_color,(x,y),font,0.5,(255,0,0),1)
        cv2.imshow('image',img)


cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()






