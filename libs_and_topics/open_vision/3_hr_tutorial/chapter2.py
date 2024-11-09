import cv2
import numpy as np

img = cv2.imread("E:/OneDrive/Documents/GitHub/notes/python/libs_and_topics/open_vision/3_hr_tutorial/resources/lena.png")
# kernel is a matrix with given values 5 x 5
# np.ones makes matrix with all ones
# unit8 is insigned integer 8 which means it can take values from 1 to 255
kernel = np.ones((5,5),np.uint8) 

# BGR is used instead of RGB
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # ksize is 7 by 7.. it has to be the same number X by X
imgCanny = cv2.Canny(img,150,200) # shows edges arguments are the threshold
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) # increase the thickness of edges, the iterations are the thickness
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) # erotion is the opposite of dialation

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0) # affects all imgshow