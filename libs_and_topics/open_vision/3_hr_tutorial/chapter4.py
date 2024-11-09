import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # zeros is black
print(img.shape)
print(img)

# selects all pixels and changes to blue
img[:]= 255,0,0

# selects some pixels and changes to blue
img[100:200, 100:200]= 255,0,0

# (0,0) is origin, (300,300) es the end, (0,255,0) is color, 3 is thickness
cv2.line(img,(0,0),(300,300),(0,255,0),3)
# this makes a line to the end of the image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# (400,50) is the center and 30 is the radius
cv2.circle(img,(400,50),30,(255,255,0),5)

# (300,200) is the origin, 1 is the scale, 3 is thickness
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)
cv2.waitKey(0)