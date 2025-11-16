import numpy as np
import cv2 as cv
# Setup Video Capture
cap = cv.VideoCapture("WIN_20251115_18_36_28_Pro.mp4")

#Check if video opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read until video is completed
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()