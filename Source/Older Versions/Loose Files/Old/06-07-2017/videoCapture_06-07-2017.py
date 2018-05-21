import numpy as np
import cv2

cap = cv2.VideoCapture(0)


#@staticmethod
def find_markers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # make image gray scale

    thresh = 185  # threshold value, play around with this value to get optimal detection
    max_value = 255
    th, dst = cv2.threshold(gray, thresh, max_value, cv2.THRESH_BINARY)  # apply filter
    im2, contours, hierarchy = cv2.findContours(dst.copy(),  # Make copy, since findContours() is
                                                cv2.RETR_EXTERNAL,  # destructive
                                                cv2.CHAIN_APPROX_SIMPLE)

    marker_count = 0
    if len(contours) > 0:  # check if at least 1 marker was found
        for cnt in contours:
            marker_count += 1
            box_area = cv2.boxPoints(cv2.minAreaRect(cnt))
            p = 3
            padding = np.array([[p, p],  # This is just to draw a rect outline
                                [-p, p],  # outside the marker.
                                [-p, -p],  # set rect = np.int32(box_area)
                                [p, -p]])  # to draw on top of marker.

            new_box = box_area + padding
            rect = np.int32(new_box)
            cv2.drawContours(image, [rect], -1, (0, 255, 0), 1)  # highlight the found marker

    # writing text to keep track of marker count in image.
    width, height = image.shape[:2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, "Markers Found: {0}".format(marker_count),  # marker counter text
                (height - 300, 25), font, .75, (0, 255, 0), 2)


while True:
    ret, frame = cap.read()
    find_markers(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()