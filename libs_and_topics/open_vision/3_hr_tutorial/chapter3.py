import cv2
import numpy as np

img = cv2.imread("E:/OneDrive/Documents/GitHub/notes/python/libs_and_topics/open_vision/3_hr_tutorial/resources/lambo.png")
print(img.shape)

# the origin of limits is the upper left 
# x goes forward
# y does down
# on cv2 functions (123, 45, 3) width, height, color depth

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

# cropping selects a range in the matrix of pixels
# on matrix functions (width, height)
# from pixel:to pixel
imgCropped = img[46:119,352:495]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)