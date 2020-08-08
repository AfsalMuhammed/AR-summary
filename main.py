import cv2
import utils.textdetection as textDetect

image = cv2.imread("Images/13.jpg")

# Saving a original image and shape


orig = image.copy()
# TODO detect text boxes inside a frame/image using EAST
textBoxes = textDetect.image_processing(image, orig)

print(textBoxes)
