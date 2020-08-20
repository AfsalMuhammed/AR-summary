import cv2
import numpy as np
import matplotlib.pyplot as plt
from cv2 import aruco
from itertools import combinations
import math
from PIL import Image


frame = cv2.imread("../images/t7.jpg")


def arucoDetection(img):
    """[detetct aruco markers and returns its co-ordinates]

    Args:
        img ([image]): [source image from the camera]

    Returns:
        [list]: [four corners of each aruco markers]
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters
    )
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    # imageDrawing("1", frame_markers)
    return corners


def imageDrawing(title, image):
    # TODO use cv2 function insted of PIL
    Image.fromarray(image).show()


def textOverlay(image, corners):
    imageClone = image.copy()
    text = cv2.imread("../images/1.jpg")
    pts_text = np.array(
        [
            [text.shape[1] - 1, text.shape[0] - 1],
            [text.shape[1] - 1, 0],
            [0, 0],
            [0, text.shape[0] - 1],
        ]
    )

    print(pts_text)
    print(corners)
    h, status = cv2.findHomography(pts_text, corners)
    # result1 = cv2.warpPerspective(banner, homographyMat, (virtualBillboard.shape[1], virtualBillboard.shape[0]))

    im_out = cv2.warpPerspective(text, h, (image.shape[1], image.shape[0]))
    cv2.fillConvexPoly(imageClone, corners, 0, 16)
    result2 = imageClone + im_out

    imageDrawing("1", result2)


def blurOverlay(image, corners):
    """[creates a blurred overlay over the text]

    Args:
        image ([type]): [description]
        corners ([type]): [description]
    """
    blurred_image = cv2.GaussianBlur(image, (143, 143), 30)
    H, W = image.shape[:2]
    mask = np.zeros(image.shape, dtype=np.uint8)
    channel_count = image.shape[2]
    ignore_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, [corners], ignore_mask_color)
    mask_inverse = np.ones(mask.shape).astype(np.uint8) * 255 - mask
    final_image = cv2.bitwise_and(blurred_image, mask) + cv2.bitwise_and(
        image, mask_inverse
    )
    # imageDrawing("2", final_image)
    return final_image


def cornerCheck(corners):

    # TODO check whether points form a quadrilateral
    print(f"length {len(corners)}")
    points = list(combinations(corners, 2))
    for point in points:
        distance = math.sqrt(
            ((int(point[0][0]) - int(point[1][0])) ** 2)
            + ((int(point[1][0]) - int(point[0][1])) ** 2)
        )
        # print(distance)
    # print(corners)
    return corners


def CornerCalculation(box):
    """[calculates corners of the paper from identified aruco marker boxes]

    Args:
        box ([type]): [description]

    Returns:
        [array]: [description]
    """
    box = box[:4]
    corners = []
    for i in box:
        corners.append(np.sum(i.reshape(4, 2), axis=0) / 4)
    a = np.array(corners, np.int32)

    return a


def detectionBox(image, corners):
    """[return bounding box on detected corners]

    Args:
        image ([img]): [original image]
        corners ([list]): [four corners of the poygon]
    """
    cv2.polylines(image, pts=[corners], isClosed=True, color=(0, 0, 0))
    # imageDrawing("1", image)


def textFromRoi(image, corners):
    # TODO take a snapshot of roi adjust for homography preprocess and do ocr
    pass


def main(frame):
    print(f"frame shape {frame.shape}")
    arcBox = arucoDetection(frame)  # aruco markers detected
    corners = CornerCalculation(arcBox)  # center point of markers calculated
    corners = cornerCheck(corners)  # check for pollygon corners
    detectionBox(frame, corners)  # box is plotted
    blurred = blurOverlay(frame, corners)
    textOverlay(blurred, corners)


main(frame)
