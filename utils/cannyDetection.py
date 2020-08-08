# OpenCV program to perform Edge detection in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2

# np is an alias pointing to numpy library
import numpy as np


image = cv2.imread("4.jpg")


def cannyDetct(image):
    canny = cv2.Canny(image, 100, 200)
    ksize = (5, 5)

    # Using cv2.blur() method
    # canny = cv2.blur(canny, ksize)
    # ret, canny = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Original", canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return canny


# a = cannyDetct(image)
# print(a.shape)
