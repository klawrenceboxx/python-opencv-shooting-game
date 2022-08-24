#Finding color

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

#creates a new window named 'Trackbars'
cv2.namedWindow('Trackbars')

#creates trackbars following the configuration; Trackbar name, referring window name, min value, max value, & call back on change
#Hue maximum is 179, so that is the max value we set it to

cv2.createTrackbar('L - H', 'Trackbars', 0, 179, nothing)

cv2.createTrackbar('L - S', 'Trackbars', 0, 255, nothing)

cv2.createTrackbar('L - V', 'Trackbars', 0, 255, nothing)

cv2.createTrackbar('U - H', 'Trackbars', 179, 179, nothing)

cv2.createTrackbar('U - S', 'Trackbars', 255, 255, nothing)

cv2.createTrackbar('U - V', 'Trackbars', 255, 255, nothing)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    #converts color into HSV (Hue Saturation Value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('L - H','Trackbars')
    l_s = cv2.getTrackbarPos('L - S','Trackbars')
    l_v = cv2.getTrackbarPos('L - V','Trackbars')
    u_h = cv2.getTrackbarPos('U - H','Trackbars')
    u_s = cv2.getTrackbarPos('U - S','Trackbars')
    u_v = cv2.getTrackbarPos('U - V','Trackbars')
  
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower, upper)
    
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #shows all the frames
    cv2.imshow('Frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.realease()
cv2.destroyAllWindows()



#green 32,90,47,94,255,172
#purple 96, 0, 97, 149, 187, 241