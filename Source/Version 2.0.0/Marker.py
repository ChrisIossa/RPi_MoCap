# datetime is required to implement timestamps
import datetime
import json
'''
Class for Marker. Stores data pertaining to individual markers
@params x -> X coordinate of the marker
        y -> Y coordinate of the marker
        cameraLabel -> Label name of the camera
        markerIdentifier -> Marker identifier, denoting which marker this current one is
        markerTimestamp -> Timestamp to be given to the marker
'''
class Marker:

    # Default constructor
    def __init__(self, x=0, y=0, cameraLabel="NA", markerIdentifier="NA", markerTimestamp=datetime.datetime.now()):
        self.coords = [x, y]
        self.cameraLabel = cameraLabel
        self.markerIdentifier = markerIdentifier
        self.markerTimestamp = markerTimestamp

    # A little print test containing marker information
    def printTest(self):
        print("Marker {0}{1}: {2}, {3}".format(self.cameraLabel, self.markerIdentifier, self.coords, self.markerTimestamp))
        return "Marker {0}{1}: {2}, {3}".format(self.cameraLabel, self.markerIdentifier, self.coords, self.markerTimestamp)
    
    # silent version of print test
    def returnTest(self):
        return "Marker {0}{1}: {2}, {3}".format(self.cameraLabel, self.markerIdentifier, self.coords, self.markerTimestamp)
        
    # Print the x, y coordinates of the marker
    def printCoords(self):
        print("Marker {0}{1} coordinates: {2}".format(self.cameraLabel, self.markerIdentifier, self.coords))

    # Print the camera label that this marker belongs to
    def printCameraLabel(self):
        print("This marker belongs to: {0}".format(self.cameraLabel))

    # Print the identifying number that marks this marker
    def printMarkerIdentifier(self):
        print("This marker's ID is: {0}".format(self.markerIdentifier))

    # Return this marker's indentifying number
    def getMarkerIdentifier(self):
        return int(self.markerIdentifier)

    # Print the timestamp of the marker
    def printTimeStamp(self):
        print("Marker {0}{1} has a timestamp of: {2}".format(self.cameraLabel, self.markerIdentifier, self.markerTimestamp))
    
    def jsonDump(self):
        d={'Marker ID': self.markerIdentifier, 'Camera': self.cameraLabel, 'Timestamp': str(self.markerTimestamp), 'coords': {'x':  self.coords[0], 'y': self.coords[1]}}
        jsonStr = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
        return jsonStr
        
         



