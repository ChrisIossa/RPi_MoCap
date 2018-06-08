import socket               # Import socket module
import datetime
import json
from Marker import Marker

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = '10.151.137.10'    # Get local machine name
print(host)
port = 54321                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()        # Establish connection with client.
print('Got connection from')
print(addr)
cont = True
markerList = []

while cont:
    msg = c.recv(4096)
    if(msg == "Disconnecting"):
        cont = False
        print(msg)
    elif (msg[0]=='{'):
        temp=Marker(0,0,'NA')
        markerList.append(temp.jsonLoad(msg))
        print markerList[-1].jsonDump()
        
c.close()
