import cv2
import numpy as np

img = cv2.imread("dataset/1.jpg")
# minimum value of blue pixel in BGR order
BLUE_MIN = np.array([200, 0, 0], np.uint8)
# maximum value of blue pixel in BGR order
BLUE_MAX = np.array([255, 50, 50], np.uint8)

dst = cv2.inRange(img, BLUE_MIN, BLUE_MAX)
no_blue = cv2.countNonZero(dst)
print('The number of blue pixels is: ' + str(no_blue))
cv2.namedWindow("opencv")
cv2.imshow("opencv", img)
cv2.waitKey(0)
