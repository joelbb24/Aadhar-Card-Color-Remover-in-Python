import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = cv2.imread("Aadhaar2.png")
frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_green = np.array([100,66,56])
upper_green = np.array([102,68,58])

green_mask = cv2.inRange(frame_hsv, lower_green, upper_green)

cv2.imshow("Results",green_mask)
cv2.waitKey(0)
