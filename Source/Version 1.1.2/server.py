import socket               # Import socket module
import datetime
import json
import zlib
import hashlib
from Marker import Marker


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = '192.168.0.100'    # Get local machine name
port = 12345                # Reserve a port for your service.
cameraCount = 1
print(host)
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
connections = {}
for i in range (0, cameraCount):
    c, addr = s.accept()        # Establish connection with client.
    connections [addr] = c
for k,v in connections.iteritems():
    print('Got connection from')
    print(k)
cont = True
markerList = []
while cont: #while the client has not sent the Disconnect signal
    msg = c.recv(4096)
    if(msg == "Disconnecting"): #session ended
        cont = False
        print(msg)
    elif (msg=="Dumping"):
        c.send("OK")
        theirHash=c.recv(40)
        print theirHash
        myHash = hashlib.sha1()
        stillRecv = True
        jsonFile =""
        while (stillRecv):
            chunk=c.recv(1024)
            jsonFile += chunk
            if(jsonFile[-1]==chr(4)):
                stillRecv=False
        jsonFile = jsonFile.strip("\n ' '")
        print "JSON File: " +jsonFile
        records = jsonFile.split('\n') #turn line delimited JSON records into list of JSON records      
        for i in records:
            if(i[0] != '{'):
                print i
            if (i[-1] != '}'):
                print i
            else:
                temp=Marker(0,0,'NA')
                markerList.append(temp.jsonLoad(i))
                myHash.update(str(temp.GUID))
                print(markerList[-1].jsonDump())
        print ("My Hash {0}".format(myHash.hexdigest()))
        print ("Their Hash {0}".format(theirHash))
        if(myHash.hexdigest() == theirHash):
            print ("Match")
        else:
            print ("Mismatch, resend")
            markerList = []
                
                    
                    
            
        
c.close()
