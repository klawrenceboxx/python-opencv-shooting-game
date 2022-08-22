#creating the webcam/ building a basic application

#imports the opencv library
import cv2

#accesses our camera for opencv capture, where 0 means the default camera
cap = cv2.VideoCapture(0)


while True:

    #captures the video frame by frame
    _, frame = cap.read()

    #flips the camera
    frame = cv2.flip(frame, 1)

    #displays the frame, "frame" will become the title of the window
    cv2.imshow("frame", frame)

    #let's us break out of the code using the esc key
    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()


