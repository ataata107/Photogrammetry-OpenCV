import cv2
import numpy as np
Lower = (59, 0, 119)
Upper = (255, 255, 255)


img=cv2.imread('for_assignment/DSC02426.JPG')

#img = cv2.resize(img, (1000, 1000))
#img = cv2.addWeighted(img,2,np.zeros(img.shape,img.dtype),0,50)
blurred = cv2.pyrMeanShiftFiltering(img,21,51)


#img = cv2.GaussianBlur(img, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, Lower, Upper)
#ret,mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
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
    roi = mask[y-2:y+h+20, x-20:x+w+20]
    roi_im= img[y-2:y+h+20, x-20:x+w+20]
    roi_bright=cv2.addWeighted(roi,2,np.zeros(roi.shape,roi.dtype),0,50)
    ret,thresh1 = cv2.threshold(roi,127,255,cv2.THRESH_BINARY)
    kernel = np.ones((15,15), np.float32)/225
    #roi = cv2.filter2D(roi,-1,kernel)
    #roi = cv2.GaussianBlur(roi, (11, 11), 0)
    #roi = cv2.dilate(roi, None, iterations = 2)
    roi = cv2.resize(roi, (100, 100))
 
    # show ROI
    cv2.imshow('segment no:'+str(i),roi)
    #cv2.rectangle(img,(x,y),( x + w, y + h ),(0,255,0),1)
    cv2.waitKey(0)
    
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#edges = cv2.Canny(mask, 50, 50)
i, j = edges.shape
print (i)
print (j)
'''
lines = cv2.HoughLines(roi, 1, np.pi/180, 30)
print(lines)
if lines is not None:
    print (len(lines))
    for line in range(len(lines)):
        for rho,theta in lines[0]:
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
_,contours,hierarchy = cv2.findContours(thresh1.copy(), 1, cv2.CHAIN_APPROX_NONE)
if len(contours) > 0:

    c = max(contours, key=cv2.contourArea)

    M = cv2.moments(c)

 

    cx = int(M['m10']/M['m00'])

    cy = int(M['m01']/M['m00'])

    print(cx,cy)

    cv2.line(roi_im,(cx,0),(cx,720),(255,0,0),1)

    cv2.line(roi_im,(0,cy),(1280,cy),(255,0,0),1)

 

    cv2.drawContours(roi_im, contours, -1, (0,255,0), 1)

 

    if cx >= 120:

        print ("Turn Left!")

 

    if cx < 120 and cx > 50:

        print ("On Track!")

 

    if cx <= 50:

        print ("Turn Right")

 

    else:

        print ("I don't see the line")
'''
corners = cv2.goodFeaturesToTrack(thresh1,3,0.01,17)
corners = np.int0(corners)
print("corn",corners)

for corner in corners:
    print(corner[0])
    x,y = corner[0]
    cv2.circle(roi_im,(x,y), 4, (0,25,0), -1)
'''
#dst = cv2.cornerHarris(roi,2,3,0.04)
#roi_im[dst>0.01*dst.max()]=[0,0,255]
#blurred = cv2.GaussianBlur(mask, (11, 11), 0)
'''
lines = cv2.HoughLinesP(roi,1,np.pi/180,10,80,1)

#Draw lines on input image
if(lines.any() != None):
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(roi_im,(x1,y1),(x2,y2),(0,255,0),2)
'''

#roi = cv2.resize(roi, (100, 100))
cv2.imshow('lapl', thresh1)
#cv2.imwrite('lapl',roi)
cv2.imshow('sobx', roi_im)
#cv2.imshow('edges', edges)
#cv2.imshow('edges', edges)
cv2.waitKey(0)
 
