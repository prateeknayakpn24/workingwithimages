import cv2

img = cv2.imread("lena.jpg", 0)
print(img)
cv2.imshow("photo",img)
k=cv2.waitKey(0) & 0xFF

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("lean_copy.png",img)
    cv2.destroyAllWindows()
    cv2.imshow('new image',img)
    cv2.waitKey()
    cv2.destroyAllWindows()