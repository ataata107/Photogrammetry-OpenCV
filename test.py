import cv2
import numpy as np
Lower = (91, 0, 182)
Upper = (150, 51, 236)


img=cv2.imread('for_assignment/DSC01798.JPG')
img = cv2.resize(img, (1000, 1000))
kernel = np.ones((15,15), np.float32)/225
#smoothed = cv2.filter2D(img,-1,kernel)
#img = cv2.GaussianBlur(img, (11, 11), 0)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, Lower, Upper)
edges = cv2.Canny(mask.copy(), 50, 150, apertureSize = 3 )
#laplacian = cv2.Laplacian(mask,cv2.CV_64F)
sobelx = cv2.Sobel(mask,cv2.CV_64F,1,0,ksize=9)
sobely = cv2.Sobel(mask,cv2.CV_64F,0,1,ksize=9)
#blurred = cv2.GaussianBlur(img, (11, 11), 0)
# dilation to strengthen the edges
kernel = np.ones((1,1), np.uint8)
# Creating the kernel for dilation
#dilated_image = cv2.dilate(laplacian,kernel,iterations=1)
#ret, threshold = cv2.threshold(laplacian,2,255,cv2.THRESH_BINARY)
#(cnts, _) = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#edges = cv2.Canny(mask, 50, 50)
i, j = edges.shape
print (i)
print (j)
lines = cv2.HoughLines(edges, 1, np.pi/180, 5)
print(lines)
if lines is not None:
#print len(lines)
    for line in range(len(lines)):
        for rho,theta in lines[line]:
            #print (lines)
             a = np.cos(theta)
             b = np.sin(theta)
             x0 = a*rho
             y0 = b*rho
             x1 = int(x0 + 1000*(-b))
             y1 = int(y0 + 1000*(a))
             x2 = int(x0 - 1000*(-b))
             y2 = int(y0 - 1000*(a))
             cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)

#cv2.imwrite('houghlines3.jpg',img)
#corners = cv2.goodFeaturesToTrack(laplacian,5,0.01,10)
#corners = np.int0(corners)
#for corner in corners:
#    x,y = cornel.ravel()
#    cv2.circle(laplacian,(x,y),3,255,-1)

#blurred = cv2.GaussianBlur(mask, (11, 11), 0)
'''
mask = cv2.dilate(mask, None, iterations = 2)
mask = cv2.erode(mask, None, iterations = 2)
'''

#cv2.imshow('lapl', img)
cv2.imshow('sobx', sobelx)
cv2.imshow('edges', edges)
cv2.imshow('mask', mask)

 
