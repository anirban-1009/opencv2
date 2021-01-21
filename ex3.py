import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(200,300),(255,255,255),50)# where, start coordinates, end coordinates, color (bgr), line thickness.


cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)# image, the top left coordinate, bottom right coordinate, color, and line thickness.


cv2.circle(img,(447,63), 63, (0,255,0), -1)# image, the top left coordinate, bottom right coordinate, color, and line thickness.


pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))


cv2.polylines(img, [pts], True, (0,255,255), 3)# where is the object being drawn to, the coordinates, should we "connect" the final and starting dot, the color, and again the thickness.

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()