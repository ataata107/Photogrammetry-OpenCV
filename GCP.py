import cv2
import numpy as np
Lower = (59, 0, 119)
Upper = (255, 255, 255)
import cv2
import os
import csv

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return images,filenames
images,filenames  = load_images_from_folder('for_assignment')
print (filenames)
print (len(images))
array =[]

t=0
for im in images:
    filenamei = filenames[t]
    img = im
    blurred = cv2.pyrMeanShiftFiltering(img,21,51)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, Lower, Upper)
    edges = cv2.Canny(mask.copy(), 50, 150, apertureSize = 5)
    th,cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(cnts),"length")
    if len(cnts)>0:
        sorted_ctrs = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[0])
        roi_mask=[]
        roi_im=[]
        thresh1=[]
        for i, ctr in enumerate(sorted_ctrs):
            print (type(i),type(t))
            x, y, w, h = cv2.boundingRect(ctr)
            roi_masks= mask[y-20:y+h+20, x-20:x+w+20]
            roi_ims= img[y-20:y+h+20, x-20:x+w+20]
            #roi_bright=cv2.addWeighted(roi_mask.copy(),2,np.zeros(roi.shape,roi.dtype),0,50)
            ret,thresh1s = cv2.threshold(roi_masks.copy(),127,255,cv2.THRESH_BINARY)
            thresh1s = cv2.resize(thresh1s, (100, 100))
            roi_ims = cv2.resize(roi_ims, (100, 100))
            #roi_mask.append(roi_masks)
            #roi_im.append(roi_ims)
            #thresh1.append(thresh1s)
            #cv2.waitKey(0)
            _,contours,hierarchy = cv2.findContours(thresh1s.copy(), 1, cv2.CHAIN_APPROX_NONE)
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print(cx,cy)
            cv2.line(roi_ims,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(roi_ims,(0,cy),(1280,cy),(255,0,0),1)
            cv2.drawContours(roi_ims, contours, -1, (0,255,0), 1)
            cv2.imshow('lapl', thresh1s)
            cv2.imshow('sobx', roi_ims)
            #cv2.waitKey(0)
            X = x-20+cx-20
            Y = y-20+cy-20
            X = str(X)
            Y = str(Y)
            filenamei = str(filenamei)
            array.append([filenamei,X,Y])
            
        
    
            
            #row = X + "," + Y + "\n"
            #f.write(row)
    #else:
        #array.append(['NaN','NaN'])
        #f = open('csvfile.csv','w')
    print (array)
    t+=1
    
with open('test.csv',"a") as fp:
    
    a = csv.writer(fp)
    data = array
    a.writerows(data)
