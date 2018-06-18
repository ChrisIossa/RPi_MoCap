# Global vars
validImports = None
cameraInitialized = None
cameraCaptureStarted = None


# Make sure all required files are imported
try:
    import datetime
    from MotionCapture import MotionCapture
    from Marker import Marker
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

# Otherwise, don't bother starting up camera
else:
    print("Could not load modules. Aborting camera operation")
