import cv2
import utils.textdetection as textDetect
import utils.cannyDetection as canny


image = cv2.imread("Images/4.jpg")

# Saving a original image and shape


orig = image.copy()
# TODO detect text boxes inside a frame/image using EAST  --Done
# TODO canny detection

textBoxes = textDetect.image_processing(image, orig)
edge = canny.cannyDetct(image)

print(textBoxes)
