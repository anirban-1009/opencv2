#Grabcut foreground extraction

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (161,79,150,150) #rect = (start_x, start_y, width, height).

cv2.grabCut(img, mask, rect, bgdModel, fgdModel,5,cv2.GC_INIT_WITH_RECT)#First the input image, then the mask, then the rectangle for our main object, the background model, foreground model, the amount of iterations to run, and what mode you are using.

mask2 = np.where((mask == 2) | (mask == 0), 0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()