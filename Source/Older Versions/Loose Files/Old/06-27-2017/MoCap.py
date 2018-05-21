validImports = None
cameraInitialized = None
cameraCaptureStarted = None

# Make sure all required files are imported
try:
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
        try:
            vid.start_capture()
        except:
            print("Could not start camera capture feed")
            cameraCaptureStarted = False
        else:
            cameraCaptureStarted = True

        # If camera capture feed started successfully, output success message
        if cameraCaptureStarted:
            print("Camera capture feed started")
    

# Otherwise, don't bother starting up camera
else:
    print("Could not load modules. Aborting camera operation")


# Marker testing
newMarker = Marker(123, 32, "A")
newMarker.printCoords()
newMarker.printLabel()