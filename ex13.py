import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([100,50,50])
	upper_blue = np.array([150,255,255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	res = cv2.bitwise_and(frame,frame, mask= mask)

	kernel = np.ones((15,15),np.float32)/225
	smoothed = cv2.filter2D(res,-1,kernel)
	blur = cv2.GaussianBlur(res,(15,15),0)
	median = cv2.medianBlur(res,15)
	bilateral = cv2.bilateralFilter(res, 15,75,75)



	cv2.imshow('Original',frame)
	cv2.imshow('Gaussian Blurring',blur)
	cv2.imshow('Averaging',smoothed)
	cv2.imshow('Median Blur',median)
	cv2.imshow('bilateral Blur', bilateral)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()