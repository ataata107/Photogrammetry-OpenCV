import cv2
from operator import xor
import numpy as np

def callback(value):
    pass


def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)

    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255

        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


def get_trackbar_values(range_filter):
    values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)

    return values


def main():

    range_filter = 'BGR'
    image=cv2.imread('for_assignment/DSC02426.JPG')                            
    image = cv2.resize(image, (1000, 1000))
    #image = cv2.addWeighted(image,2,np.zeros(image.shape,image.dtype),0,50)
    image = cv2.pyrMeanShiftFiltering(image,31,51)
    setup_trackbars(range_filter)
    frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



    while True:

        
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)

        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        if True:
            preview = cv2.bitwise_and(image, image, mask=thresh)
            cv2.imshow("Preview", preview)
        else:
            cv2.imshow("Original", image)
            cv2.imshow("Thresh", thresh)

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


if __name__ == '__main__':
    main()
