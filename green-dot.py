import cv2
import numpy as np  
# load image
img = cv2.imread("tank.jpg")
# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# set lower and upper color limits
lower_val = np.array([58,204,219])
upper_val = np.array([101,255,255])
# Threshold the HSV image 
mask = cv2.inRange(hsv, lower_val, upper_val)
# remove noise
kernel =  np.ones((5,5),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# find contours in mask
im2, contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw contours
for cnt in contours:
    cv2.drawContours(img,[cnt],0,(0,0,255),2)
#show image
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 