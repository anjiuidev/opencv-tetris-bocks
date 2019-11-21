# import the packages
import cv2
import numpy as np
import argparse
import imutils

# argument parser construction
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Add the image path.")

args = vars(ap.parse_args())

# loading the image
image = cv2.imread(args['image'])
cv2.imshow("Tetris Image", image)
cv2.waitKey(0)

# convert the image to gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)

# edge detection using Canny method
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Canny/Edged Image", edged)
cv2.waitKey(0)

# Thresholding - Thresholding can be used to remove lighter or darker regions and contours of images.
threshold = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold Image", threshold)
cv2.waitKey(0)

# Detecting and drawing contours
contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
output = image.copy()

# loop over contours
for cnt in contours:
    cv2.drawContours(output, [cnt], -1, (240, 0, 159), 3)
    cv2.imshow("Countour Image", output)
    cv2.waitKey(0)

# draw the total number of contours found in purple
text = "I found {} objects!".format(len(contours))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

# Erosions and dilations
mask = threshold.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

# Masking and bitwise operations
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)