import cv2
import datetime
import numpy as np
import time

#to control the mouse
from pymouse import PyMouse

#function used to resize the window: https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
def image_resize(image, width = None, height = None,  inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None: 
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized


cap = cv2.VideoCapture(0)

m = PyMouse()

last_click = datetime.datetime.now()

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BG2BGR)

    lower_green = np.array([32, 90, 47])
    upper_green = np.array([94, 255, 172])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    lower_purple = np.array([96, 0, 97])
    upper_purple = np.array([149, 187, 241])
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

    #RETR_EXTERNAL will retrieve the extreme outer contour for a color
    #CHAIN_APPROX_SIMPLE will compress the horizontal, vertical and diagonal segments and leav the endpoints only

    countoursGreen, _ = cv2.findCOuntours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #countour contains multiple components hence why we need to loop through them
    for c in countoursGreen:

        #lets us make sure our countour size area is reasonable
        if cv2.countourArea(c) <= 50:
            continue
        x, y, _, _ = cv2.boundingRect(c)
        m.move(x,y)

        #lets us draw the countour
        cv2.drawCountours(frame, countoursGreen, -1, (0, 255, 0), 3)

    countoursPurple, _ = cv2.findCountours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in countoursPurple:
        if cv2.countourArea(c) <= 50:
            continue

        now = datetime.datetime.now()
        diff = now - last_click
        if diff.total_seconds() > 0.5:
            last_click = datetime.datetime.now()
            cv2.drawCountours(frame,countoursPurple, -1, (0, 255, 0), 3)
            x, y = m.position()
            m.click(x,y,1)

    frame = image_resize(frame, width = 400)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
           

cap.realease()
cv2.destroyAllWindows()