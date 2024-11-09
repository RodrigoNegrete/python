# source
# https://www.youtube.com/watch?v=W9oRTI6mLnU

import cv2
import numpy as np
import pytesseract
import os

# link to command in windows installation - > not needed if installed with pip
# pytesseract.pytesseract.tesseract_cmd = path/to/exe

# imgQ = cv2.imread('E:\OneDrive\Documents\GitHub\notes\python\libs\ocr\opencv\Query.png')
imgQ = cv2.imread('Query.png')
cv2.imshow("Output", imgQ)
cv2.waitKey(0) # = is the time to wait to show image

# get image attributes height, width and (channel) - color depth maybe
h, w, c = imgQ.shape
print(imgQ.shape)

# resize image to a third
imgQ = cv2.resize(imgQ, (w//3, h//3))
print(imgQ.shape)

# create detector - ORB
# define features - default 500 and we change to 1000
orb = cv2.ORB_create(1000)
print(orb)

# define keypoints that are unique points in the image and descriptors that are how the computer interprets them
kp1, des1 = orb.detectAndCompute(imgQ, None)

# example with 5000 keypoints
orb = cv2.ORB_create(5000)
kp2, des2 = orb.detectAndCompute(imgQ, None)
imgKp2 = cv2.drawKeypoints(imgQ, kp2, None)
cv2.imshow("KeyPointsQuery", imgKp2)
cv2.waitKey(0) # = is the time to wait to show image

# set path for test images
path = "UserForms"
myPicList = os.listdir(path)
print(myPicList)

# print images with index number
for j, y in enumerate(myPicList):
    img = cv2.imread(path + "/" + y )
    # img = cv2.resize(imgQ, (w//3, h//3))
    cv2.imshow(y, img)
    cv2.waitKey(0)

percent =25 # we will get the 25% best matches

for j, y in enumerate(myPicList):
    img = cv2.imread(path + "/" + y )
    kp2, des2 = orb.detectAndCompute(img, None) # we will rewrite or reuse the variables from the example above to keep consistency with the tutorial
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.match(des2, des1)
    # sort matches based on distance
    matches.sort(key = lambda x: x.distance)
    # extraxt the best matches
    good = matches[:int(len(matches)*(percent/100))]
    # draw marches
    imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good, None, flags = 2) # None is out image, flag is
    # show images
    cv2.imshow(y, imgMatch)
    cv2.waitKey(0)

# find relationship between keypoints from source and test files

for j, y in enumerate(myPicList):
    img = cv2.imread(path + "/" + y )
    kp2, des2 = orb.detectAndCompute(img, None) # we will rewrite or reuse the variables from the example above to keep consistency with the tutorial
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.match(des2, des1)
    # sort matches based on distance
    matches.sort(key = lambda x: x.distance)
    # extract the best matches
    good = matches[:int(len(matches)*(percent/100))]
    # draw marches
    imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good, None, flags = 2) # None is out image, flag is

    # find relationship between keypoints from source and test files
    srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2) # source points
    dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2) # destination points
    M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0) # 5.0 is a parameter default from documentation
    # align form
    imgScan = cv2.warpPerspective(img, M, (w, h))
    # show images
    cv2.imshow(y, imgScan)
    cv2.waitKey(0)