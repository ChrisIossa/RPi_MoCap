#import cv2
#import numpy as np
import datetime
import os.path
#import enableLightRing
#import disableLightRing
from Marker import Marker


class MotionCapture:

    def __init__(self):
        self.show_video = True
        self.show_fps = True
        self.show_markers = False
        self.show_cords = True
        self.show_marker_count = True

        self.marker_color = (0, 255, 0)
        self.threshold_value = 130
        self.max_value = 255

        self.fps_counter = 0
        self.start_time = None
        self.current_fps = 0

    def display_fps(self, image):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, "FPS: {0}".format(self.current_fps),
                    (25, 25), font, .75, (255, 255, 0), 2)

    def draw_text(self, image, text, location, font_size, color, thickness):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, location, font, font_size, color, thickness)

    def get_gray_scale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # make image gray scale

    def get_threshold_mask(self, gray_image):
        th, dst = cv2.threshold(gray_image, self.threshold_value, self.max_value, cv2.THRESH_BINARY)  # apply filter
        return dst

    def write_image(self, image):
        counter = 1
        while os.path.isfile("image{0}.jpg".format(counter)):
            counter += 1
        cv2.imwrite("image{0}.jpg".format(counter), image)

    def toggle(self, option):
        if option is False:
            return True
        if option is True:
            return False

    def find_markers(self, image):
        gray_img = self.get_gray_scale(image)

        threshold_img = self.get_threshold_mask(gray_img)
        im2, contours, hierarchy = cv2.findContours(threshold_img.copy(),  # Make copy, since findContours() is
                                                    cv2.RETR_EXTERNAL,  # destructive
                                                    cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:  # check if at least 1 marker was found
            for cnt in contours:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

    def start_capture(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 120)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        fps = cap.get(cv2.CAP_PROP_FPS)
        # Set Time
        self.start_time = datetime.datetime.now()
        while True:

            self.fps_counter += 1
            ret, frame = cap.read()
            #frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            self.current_fps = int(self.fps_counter / (datetime.datetime.now() - self.start_time).total_seconds())
            if self.show_markers:
                self.find_markers(frame)
            if self.show_fps:
                self.draw_text(frame, str(fps),(int(frame.shape[:2][1]*.9),20), 0.75, (0,0,255), 2)
                self.display_fps(frame)
            if self.show_video:
                cv2.imshow("Video", frame)
            # Key events
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):         # Program Exit
                cap.release()
                break
            if key == ord('s'):
                self.write_image(frame)
            if key == ord('f'):
                self.show_fps = self.toggle(self.show_fps)
            if key == ord('m'):
                self.show_markers = self.toggle(self.show_markers)
            if key == ord('e'):
                enableLightRing.enable()
                #exec(open("./enableLightRing.py").read())
            if key == ord('d'):
                disableLightRing.disable()
                #exec(open("./disableLightRing.py").read())

    def start2(self):
        print("calling")
        while True:
            ret, frame = self.cap.read()
            self.find_markers(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

'''
if __name__ == '__main__':
    print("calling")
    vid = VideoCapture()
    vid.start_capture()
'''