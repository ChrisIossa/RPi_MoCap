import socket               # Import socket module
import datetime
import json
import hashlib
from Marker import Marker


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Create a socket object
host = '__IP_ADDRESS__'             # IP address used for this service
port = __PORT_NUM__                 # Reserve a port for your service.
cameraCount = __CAMERA_COUNT__      # Number of cameras used for this session.
print(host)
s.bind((host, port))                # Bind to the port
s.listen(5)                         # Now wait for client connection.
connections = {}
for i in range (0, cameraCount):    # Connect to each camera in sequence
    c, addr = s.accept()            # Establish connection with camera.
    connections [addr] = c          # Store the camera socket in a dictionary with the IP address as the key
    print('Got connection from')
    print(addr)
    # TODO: Assign Camera Label here
    # TODO: Calibrate Camera here
    # TODO: Send capture start signal here or camera start time here (Requires synchronizination of system time)

markerList = [] # List of markers

while cameraCount != 0:                     # While there are still cameras connected
    for k,v in connections.iteritems():     # Poll each camera in sequence
        v.settimeout(30.0)                  # Set timeout for poll
        try:
            msg = v.recv(4096)              # Listen for any message on socket
        except timeout:
            print "Read timed out"          # Nothing in socket
        v.settimeout(None)
        if(msg == "Disconnecting"):         # Camera disconnected
            cameraCount--                   # One less camera connected
            print(msg)
            v.close()                       # Close the socket
        elif (msg=="Dumping"):              # Camera wishes to dump data
            v.send("OK")                    # Acknowledge
            theirHash=v.recv(40)            # Get the hash of marker GUIDs
            print theirHash     
            myHash = hashlib.sha1()         # Prepare SHA1 has to store hash of recived marker GUIDs
            stillRecv = True        
            jsonFile = ""                   # String that mimics jsonFile
            while (stillRecv):
                chunk = v.recv(4096)        # Read 4096 bytes from socket
                jsonFile += chunk           # Add it to the JSON file
                if(jsonFile[-1]==chr(4)):   # If the last character of the chunk is EOT
                    stillRecv=False         # EOF
            jsonFile = jsonFile.strip("\n ' '")     # Remove whitespace characters from start and end of string
            records = jsonFile.split('\n')  # Turn line delimited JSON objects into list of JSON objets
            for i in records:               # For each JSON Object
                if(i[0] != '{'):            # If the first character is not a opening curly brace
                    print "Error: " + i     # Print out the record
                if (i[-1] != '}'):          # If the last character is not a closing curly brace
                    print "Error: " + i     # Print out the record
                else:                       # Otherwise
                    temp=Marker(0,0,'NA')   # Make a temporary marker
                    markerList.append(temp.jsonLoad(i))     # Deserialize the marker from JSON, store it in temp, and append it to the marker list.
                    myHash.update(str(temp.GUID))           # Update the SHA1 hash with the GUID of the newly inserted marker
                    print(markerList[-1].jsonDump())        # Print the newly recived marker
            print ("My Hash {0}".format(myHash.hexdigest()))# Print out the hash the host generated
            print ("Their Hash {0}".format(theirHash))      # Print out the hash sent from the camera
            if(myHash.hexdigest() == theirHash):            # Compare both hashes
                print ("Match")                             
            else:
                print ("Mismatch, resend")                  
                markerList = []             # Clear marker list
                
