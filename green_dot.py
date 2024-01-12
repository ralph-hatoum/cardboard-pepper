import cv2
import numpy as np  

BOUNDS = ((27,13,228),(85,139,255))


def green_dot_finder(img):
    img = cv2.imread("image_data.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    lower_val = np.array([27,13,228])
    upper_val = np.array([85,139,255])
    mask = cv2.inRange(hsv, lower_val, upper_val)
    kernel =  np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    contours, im2 = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    output = len(contours) > 0
    for cnt in contours:
    # print(cnt)
        cv2.drawContours(img,[cnt],0,(0,0,255),2)
    #show image
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

    return output


print(green_dot_finder("image_data-cropped.jpg"))
# load image
# img = cv2.imread("img2.jpg")
# # convert to HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# # set lower and upper color limits
# # lower_val = np.array([58,204,219])
# # upper_val = np.array([101,255,255])
# lower_val = np.array([27,13,228])
# upper_val = np.array([85,139,255])
# # Threshold the HSV image 
# mask = cv2.inRange(hsv, lower_val, upper_val)
# # remove noise
# kernel =  np.ones((5,5),np.uint8)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# # find contours in mask
# contours, im2 = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # draw contours
# print(contours)
# output = len(contours) > 0
# print("box in image :",output)
# for cnt in contours:
#     # print(cnt)
#     cv2.drawContours(img,[cnt],0,(0,0,255),2)
# #show image
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

# img = cv2.imread("img3.jpg")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# mask = cv2.inRange(hsv, lower_val, upper_val)
# kernel =  np.ones((5,5),np.uint8)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# contours, im2 = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# output = len(contours) > 0
# print("box image :",output)

# for cnt in contours:
#     # print(cnt)
#     cv2.drawContours(img,[cnt],0,(0,0,255),2)
# #show image
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 