# Global vars
validImports = None
cameraInitialized = None
cameraCaptureStarted = None


# Make sure all required files are imported
try:
    import datetime
    import re
    import argparse
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

# Command Line Parameters

parser = argparse.ArgumentParser()
parser.add_argument('integers', type=int, nargs='1', choices = range(255), help='value for the threshold')
parser.add_argument('ipaddress', nargs = '1', help='ip address of the camera')
parser.add_argument('port', type=int, nargs = '1', help = 'the port number')
parser.add_argument('label', nargs ='1', help = 'the name/label of the camera')
parser.add_argument('frame_freq', type=int, nargs='1', help='the frequency of frames to be sent')
parser.add_argument('-s', '--send', nargs ='1', help='determine if frequency of frames is displayed or not', action='store_true')

args = parser.parse_args()

#assigning values
thresholdValue = args.integers
temp = args.ipaddress
temp = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$") #ip address input validation
if temp:
    ipAddress = re.group()
port = args.port
label = args.label
frames = args.frame_freq

#printing values
print("Values given are: ")
print("Threshold -- " + thresholdValue)
print("IP Address -- " + ipAddress)
print("Port Number -- " + port)
print("Label Name -- " + label)
if args.send:
    print("Frame Frequency -- " + frames)
    

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
