import numpy as np
import cv2

img = cv2.imread('opencv-corner-detection-sample.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#convert to gray, then to float32
gray = np.float32(gray)


corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)# image, max corners to detect, quality, and minimum distance between corners.
corners = np.int0(corners)

for corner in corners:

	x,y = corner.ravel()
	cv2.circle(img, (x,y),3,255,-1)

cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()