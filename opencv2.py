import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow("mask")
cv2.createTrackbar("L - H", "mask", 0, 179, nothing)
cv2.createTrackbar("L - S", "mask", 0, 255, nothing)
cv2.createTrackbar("L - V", "mask", 0, 255, nothing)
cv2.createTrackbar("U - H", "mask", 179, 179, nothing)
cv2.createTrackbar("U - S", "mask", 255, 255, nothing)
cv2.createTrackbar("U - V", "mask", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "mask")
    l_s = cv2.getTrackbarPos("L - S", "mask")
    l_v = cv2.getTrackbarPos("L - V", "mask")
    u_h = cv2.getTrackbarPos("U - H", "mask")
    u_s = cv2.getTrackbarPos("U - S", "mask")
    u_v = cv2.getTrackbarPos("U - V", "mask")
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()