import cv2

# read images
img = cv2.imread("E:/OneDrive/Documents/GitHub/notes/python/libs_and_topics/open_vision/3_hr_tutorial/resources/lena.png")
print(type(img))


# show image
cv2.imshow("Image", img)
cv2.waitKey(0) # argument is milliseconds to show image. 0 is infinite


# import video
cap = cv2.VideoCapture("E:/OneDrive/Documents/GitHub/notes/python/libs_and_topics/open_vision/3_hr_tutorial/resources/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): # shows video until q is pressed
        break


# import from webcam
cap = cv2.VideoCapture(1) # use 1 if you only have one, otherwise use can number
# set resolution
cap.set(3, 640) # 3 is the id for width
cap.set(4, 480) # 4 is the id for height
# set brightness 
cap.set(10, 100) # 4 is the id for height 100 is percent


while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): # shows video until q is pressed
        break