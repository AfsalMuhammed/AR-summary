import cv2

# TODO detct 4 corners of a paper using aruco markers


from cv2 import aruco


cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        frame, aruco_dict, parameters=parameters
    )
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

    # Display the resulting frame
    cv2.imshow("frame", frame_markers)

    # "Q" to quit the program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
