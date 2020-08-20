import cv2
import utils.textdetection as textDetect
import utils.cannyDetection as canny

import numpy as np

# import cv2
from matplotlib import pyplot as plt

image = cv2.imread("Images/13.jpg")

# Saving a original image and shape

image2 = image.copy()
orig = image.copy()
# TODO detect text boxes inside a frame/image using EAST  --Done
# TODO canny detection

textBoxes = textDetect.image_processing(image, orig)
edge = canny.cannyDetct(image)

print(textBoxes)


# convert image to gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.int0(corners)

# we iterate through each corner,
# making a circle at each point that we think is a corner.
for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)

plt.imshow(image), plt.show()


# img2 = cv2.imread('arrow.jpg', cv2.IMREAD_COLOR)

# Reading same image in another variable and
# converting to gray scale.
img = cv2.imread('"Images/13.jpg"', cv2.IMREAD_GRAYSCALE)

# Converting image to a binary image
# (black and white only image).
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

# Detecting shapes in image by selecting region
# with same colors or intensity.
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Searching through every region selected to
# find the required polygon.
for cnt in contours:
    area = cv2.contourArea(cnt)

    # Shortlisting the regions based on there area.
    if area > 400:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

        # Checking if the no. of sides of the selected region is 7.
        if len(approx) == 7:
            cv2.drawContours(image2, [approx], 0, (0, 0, 255), 5)

# Showing the image along with outlined arrow.
cv2.imshow("image2", image2)

# Exiting the window if 'q' is pressed on the keyboard.
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()

