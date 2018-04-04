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

6. Image is converted into hsv scale.
