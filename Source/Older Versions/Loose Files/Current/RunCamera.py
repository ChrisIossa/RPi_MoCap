# Global vars
validImports = None
cameraInitialized = None
cameraCaptureStarted = None


# Make sure all required files are imported
try:
    import datetime
    from MotionCapture import MotionCapture
    from Marker import Marker
    import disableLightRing
    import enableLightRing
    import RPi.GPIO as GPIO
except ModuleNotFoundError as e:
    print(e)
    validImports = False
else:
    validImports = True
    

# If all modules were imported, attempt to start camera
if validImports:
    print("Initializing camera...")

    # Attempt to initialize the camera object
    try:
        vid = MotionCapture()
    except:
        print("Could not initialize camera")
        cameraInitialized = False
    else:
        cameraInitialized = True

    # If the camera was successfully initialized, attempt to start the capture feed
    if cameraInitialized:
        print("Camera initialized")

        print("Attempting to start camera capture feed...")
        vid.startCapture()
        '''
        try:
            vid.startCapture()
        except:
            print("Could not start camera capture feed")
            cameraCaptureStarted = False
        else:
            cameraCaptureStarted = True
            '''

# Otherwise, don't bother starting up camera
else:
    print("Could not load modules. Aborting camera operation")


# Marker testing
'''
markerList = []
marker1 = Marker(123, 321, "A", "1")
marker1.printCoords()

for i in range (1, 10):
    markerList.append(Marker(111, 222, "A", i))


marker1.printTimeStamp()

marker2 = Marker(123, 333, "A", "2")
marker2.printTimeStamp()


for marker in markerList:
    marker.printTimeStamp()
'''

