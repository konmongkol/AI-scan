import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0,201,201])
    upper_blue = np.array([36,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        area = w * h
        print(area)
        epsilon = 0.08 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        
        if area > 15000:
            cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
            # print('approx', approx)
            for x in range(0, len(approx)):
                cv2.circle(img, (approx[x][0][0], approx[x][0][1]), 5, (0,0,255), -1)
    # if area > 20000000:
    #     cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
    #     print('approx', approx)
    #     for x in range(0, len(approx)):
    #         cv2.circle(img, (approx[x][0][0], approx[x][0][1]), 30, (0,0,255), -1)
    cv2.imshow('image',img)
    cv2.imshow('hsv',img)
    key = cv2.waitKey(1)
    if key == 27:
        break
        
cap.release()   
cv2.destroyAllWindows()