import cv2
import numpy as np
Lower = (59, 0, 119)
Upper = (255, 255, 255)


img=cv2.imread('for_assignment/DSC02407.JPG')

#img = cv2.resize(img, (1000, 1000))
#img = cv2.addWeighted(img,2,np.zeros(img.shape,img.dtype),0,50)
blurred = cv2.pyrMeanShiftFiltering(img,21,51)

kernel = np.ones((15,15), np.float32)/225
#smoothed = cv2.filter2D(img,-1,kernel)
#img = cv2.GaussianBlur(img, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, Lower, Upper)
#mask = cv2.erode(mask, None, iterations = 2)
#mask = cv2.dilate(mask, None, iterations = 2)
edges = cv2.Canny(mask.copy(), 50, 150, apertureSize = 5)
#laplacian = cv2.Laplacian(mask,cv2.CV_64F)
sobelx = cv2.Sobel(mask,cv2.CV_64F,1,0,ksize=9)
sobely = cv2.Sobel(mask,cv2.CV_64F,0,1,ksize=9)
#blurred = cv2.GaussianBlur(img, (11, 11), 0)
# dilation to strengthen the edges
kernel = np.ones((1,1), np.uint8)
# Creating the kernel for dilation
#dilated_image = cv2.dilate(laplacian,kernel,iterations=1)
#ret, threshold = cv2.threshold(laplacian,2,255,cv2.THRESH_BINARY)
th,cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts),"length")
#cv2.drawContours(img,cnts,-1,(0,0,255),2)
sorted_ctrs = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[0])
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
 
    # Getting ROI
    roi = mask[y:y+h, x:x+w]
    roi = cv2.resize(roi, (100, 100))
 
    # show ROI
    cv2.imshow('segment no:'+str(i),roi)
    #cv2.rectangle(img,(x,y),( x + w, y + h ),(0,255,0),1)
    #cv2.waitKey(0)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#edges = cv2.Canny(mask, 50, 50)
i, j = edges.shape
print (i)
print (j)
'''
lines = cv2.HoughLines(roi, 1, np.pi/180, 7)
print(lines)
if lines is not None:
    print (len(lines))
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
             cv2.line(roi,(x1,y1),(x2,y2),(0,0,255),1)
'''

#cv2.imwrite('houghlines3.jpg',img)
corners = cv2.goodFeaturesToTrack(edges,5,0.01,100)
corners = np.int0(corners)
print("corn",corners)

for corner in corners:
    x,y = corners.ravel()
    cv2.circle(mask,(x,y),3,255,-1)

#blurred = cv2.GaussianBlur(mask, (11, 11), 0)




cv2.imshow('lapl', roi)
#cv2.imshow('sobx', sobelx)
#cv2.imshow('edges', edges)
#cv2.imshow('edges', edges)

 
