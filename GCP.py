import cv2
import numpy as np
Lower = (133, 100, 100)
Upper = (255, 255, 255)


img=cv2.imread('for_assignment/DSC02426.JPG')
img = cv2.resize(img, (1000, 1000))
kernel = np.ones((15,15), np.float32)/225
#smoothed = cv2.filter2D(img,-1,kernel)
#blurred = cv2.GaussianBlur(img, (11, 11), 0)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img, Lower, Upper)
edges = cv2.Canny(mask.copy(), 50, 150, apertureSize = 3)
i, j = edges.shape
print (i)
print (j)
#blurred = cv2.GaussianBlur(mask, (11, 11), 0)
'''
mask = cv2.dilate(mask, None, iterations = 2)
mask = cv2.erode(mask, None, iterations = 2)
'''
cv2.imshow('frame', mask)


 
