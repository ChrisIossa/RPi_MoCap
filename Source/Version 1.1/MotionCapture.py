import cv2 #OpenCV
import numpy as np 
import datetime
import os.path
import enableLightRing
import disableLightRing
from Marker import Marker

'''
Class for MotionCapture object. Bulk of the magic is done here, utilizing the openCV library for tracking and displaying.
This class contains functions to convert images to grayscale, utilize the openCV library for tracking whitespace and 
displaying them as markers, denoting with a green box the coordinates.

'''
class MotionCapture:

    # Default constructor. No parameters needed
    def __init__(self):
        self.showVideo = True
        self.showFPS = True
        self.showMarkers = False
        self.showCoordinates = True
        self.showMarkerCount = True

        self.markerCount = 0
        self.markerList = []

        self.markerColor = (0, 255, 0)
        self.thresholdValue = 200
        self.maxThresholdValue = 255

        self.fpsCounter = 0
        self.startTime = None
        self.currentFPS = 0



    '''
    This method will display the frames per second being captured by the camera in the upper left hand corner
    @params image -> What image frame to display the text to
    '''
    def displayFPS(self, image):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, "FPS: {0}".format(self.currentFPS), 
                    (25, 25), font, .75, (255, 255, 0), 2)



    '''
    This method is a blanket method to draw text in a passed in location, given the parameters
    @params image     -> The image frame to display text to
            text      -> The text string to display
            location  -> X, Y coordinate to display the text
            fontSize -> Size of the text's font
            color     -> Color of the text
            thickness -> Thickness of the font
    '''
    def drawText(self, image, text, location, fontSize, color, thickness):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, location, font, fontSize, color, thickness)




    '''
    This method takes in an image still and converts it to grayscale
    @params image -> The image to turn into grayscale
    @return The converted image to grayscale

    '''
    def getGrayScale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # make image gray scale




    '''
    This method will determine if the input grayscale image is within the whitespace threshold. 
    Utilize THRESH_BINARY to convert all pixels to either 0 for white, or 1 for black.
    @params gray_image -> The grayscale image to process
    @return The threshold image after determining the threshold rating for the image

    '''
    def getThresholdMask(self, grayScaleImage):
        th, dst = cv2.threshold(grayScaleImage, self.thresholdValue, self.maxThresholdValue, cv2.THRESH_BINARY)  # apply filter
        return dst



    '''
    This method will write the input image still to hard disk with a unique name, as to not overwrite files.
    @params image -> The image still to write to hard disk
    
    '''
    def writeMethod(self, image):
        counter = 1
        while os.path.isfile("image{0}.jpg".format(counter)):
            counter += 1
        cv2.imwrite("image{0}.jpg".format(counter), image)





    '''
    This method is a blanket method to toggle a boolean value, i.e. a camera setting that is either True or False
    @params option -> The bool value to toggle

    '''
    def toggle(self, option):
        if option is False:
            return True
        if option is True:
            return False




    '''
    This method will locate and process markers on a given image. 
    The processing of markers involves finding them via whitespace, granted by the grayscale thresholding, and 
    bounding a box around them. 
    This will refresh every frame the camera captures. Storing and creation of the markers is also processed here
    @params image -> The image still (frame) to locate markers

    '''
    def findMarkers(self, image):
        grayScaleImage = self.getGrayScale(image)

        binaryThresholdImage = self.getThresholdMask(grayScaleImage)

        # Make copy, since findContours() is destructive
        imageCopy, contourList, hierarchy = cv2.findContours(binaryThresholdImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contourList) > 0:  # check if at least 1 marker was found
            tempCount = 0

            # Start of fresh frame, reset timestamp and number of markers
            i = len(contourList)
            timestamp = datetime.datetime.now()
            
            #print("Fresh frame. deleting markers")
            del self.markerList[:]

            for contour in contourList:
                if tempCount < 20:
                    tempCount += 1
                    rect = cv2.minAreaRect(contour)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
                    x, y, x2, y2 = cv2.boundingRect(contour)
                    centerX = int (x+(x2/2))
                    centerY = int (y+(y2/2))

                    # Draw an identifying label on top of each marker
                    self.drawText(image, "A" + str(len(contourList) - i), (centerX, centerY - 25), .50, (0, 255, 255), 1)

                    # Draw a circle denoting centerpoint of marker
                    cv2.circle(image, (centerX, centerY), 2, (0, 0, 255), -1)

                    try:

                        if (len(self.markerList) == 0):
                            print("Creating first marker")
                        elif (len(self.markerList) < len(contourList)):
                            print("Creating new marker")
                        else:
                            pass
                        temp = Marker(centerX, centerY, "A", len(contourList) - i, timestamp)
                        self.markerList.append(temp)
                        temp.printTest()

                        i = i - 1
                    except:
                        print("Error creating marker object or appending")
                else:
                    print("too many markers in view")

        else:
            del self.markerList[:]



    '''
    This method will control the starting and stopping of video capture from the camera, activation of other class functions, 
    and keypresses while video frame is active and in focus. 

    '''
    def startCapture(self):
        try:
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FPS, 120)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            fps = cap.get(cv2.CAP_PROP_FPS)
        except:
            print("Ran into an issue starting camera feed")
        else:
            print("Camera capture started successfully")
        # Set Time
        self.startTime = datetime.datetime.now()
        while True:

            self.fpsCounter += 1
            ret, frame = cap.read()
            #frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # Deprecated by above line
            self.currentFPS = int(self.fpsCounter / (datetime.datetime.now() - self.startTime).total_seconds())
            if self.showMarkers:
                self.findMarkers(frame)
            if self.showFPS:
                self.drawText(frame, str(fps),(int(frame.shape[:2][1]*.9),20), 0.75, (0,0,255), 2)
                self.displayFPS(frame)
            if self.showVideo:
                cv2.imshow("Video", frame)


            '''
				Keypress events
	    '''
            keyPress = cv2.waitKey(1) & 0xFF
            # Close down the video frame, stop capturing, and disable lightring
            if keyPress == ord('q'):
                disableLightRing.disable()
                cap.release()
                break
            
			# Write a still image from the camera to drive
            if keyPress == ord('s'):
                self.writeMethod(frame)

			# Display the current frames/sec on the video frame
            if keyPress == ord('f'):
                self.showFPS = self.toggle(self.showFPS)
            
			# Display markers in view on the video frame	
            if keyPress == ord('m'):
                self.showMarkers = self.toggle(self.showMarkers)
                print("Show markers set to {0}".format(self.showMarkers))

			# Enable the lightring for the camera (on e key pressed)
            if keyPress == ord('e'):
                enableLightRing.enable()
			# Disable the lightring for the camera (on d key pressed)
            if keyPress == ord('d'):
                disableLightRing.disable()

            # Decrease the threshold of whitelight capture (On Up Arrow Pressed)
            if keyPress == 84:
                self.thresholdValue = self.thresholdValue - 1
                print("Decreasing threshold to {0}".format(self.thresholdValue))

            # Increase the threshold of whitelight capture (On Down Arrow Pressed)
            if keyPress == 82:
                self.thresholdValue = self.thresholdValue + 1
                print("Increasing threshold to {0}".format(self.thresholdValue))

