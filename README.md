# Problem-Statement
We have been given a photo in that there can be a strip of white colored L shape. There is a point called GCP which is the inner corner of L-shape.
We have to detect the location of GCP if it is present in the photo.
This problem led me to learn different ways of approaching the problem and led me to learn new methods of computer vision. Here I will tell you step by step the procedure approached by me

1. A photo was selected in the given folder/for/assignment.

2. Image is blurred so as to remove noice. For blurring we are using inbuilt PyrMeanshift  blurring as I found it best against manually making a kernel or using gaussian blur. This method led to the best mask creation in color range .py. Below is a photo of this filtering.

![image](https://user-images.githubusercontent.com/32903329/38299997-47dada22-3819-11e8-8c5d-4e93e27cea0d.png)

3. Initially, I planned to brighten the image in the initial steps but that led to detection of unwanted pixels in the mask.

4. Also, whole code was proceeded by initially recizing the image but that plan was abolished as it didnt lead to correct contour detections.

5. Now the lower and the upper bound is set for the image We found these values with help of colorRange.py

6. Image is converted into hsv scale. Below is the effect
![image](https://user-images.githubusercontent.com/32903329/38300459-751c6c48-381a-11e8-8c55-1b1dcb52f750.png)

7.  HSV image is fed to inbuilt inrange function to the find the suitable mask of the image. Using this we are able to seperate out white values from the image. Below is the mask of the image

![image](https://user-images.githubusercontent.com/32903329/38300637-eb348582-381a-11e8-9996-601c24ca0d19.png)

8. Now rather than processing on the whole image we have to find the regions of concerned white area of the image and process on that area alone.

9. For finding out the concerned area we will be using findcontours in built open cv function.

10. Here we will be checking if there is a contour detected.  If no contour is detected than obviously there is no GCP in the given image. If there is a contour then we can proceed further.

11. Contours detected are sorted. We have bound the contours in a rectangular box. Contour mask is selected and the roi is determined. Image of the contour is also stored. Mask is thresholded to remove noices. Below is the image of thresholded mask after contour detection.

![segmentno2](https://user-images.githubusercontent.com/32903329/38301902-8b6d3384-381e-11e8-8503-a1d0262ca50b.jpg)


12. ROI is resized now

12. We have increased the roi than the initial contour detected for better visualisation purposes.  Contours are again deteceted and the the centre of the contour will be our GCP. Below is the image of GCP of image detected.

![capture](https://user-images.githubusercontent.com/32903329/38302093-23c5ffb2-381f-11e8-8ad8-39681fe82ce6.PNG)
