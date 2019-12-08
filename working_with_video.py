import cv2
c=0

video = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi',fourcc,60.0,(int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)),int(video.get(cv2.CAP_PROP_FRAME_WIDTH))))


while(video.isOpened()):
    ret, frame=video.read()
    if ret == True:

        output.write(frame)


        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



video.release()
output.release()
cv2.destroyAllWindows()