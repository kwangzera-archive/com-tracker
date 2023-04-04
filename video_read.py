# import the opencv library
import cv2
import time
from matplotlib import pyplot as plt

# define a video capture object
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
# print(cv2.VideoCapture)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))


# cap.set(cv2.CAP_PROP_EXPOSURE, -8.0)
print(cap)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()