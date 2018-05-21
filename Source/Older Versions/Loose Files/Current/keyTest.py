import cv2
img = cv2.imread('image1.jpg')
while(True):
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    else:
        print(k)
