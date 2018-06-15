import socket               # Import socket module
import datetime
import json
from Marker import Marker

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = '169.254.114.139'    # Get local machine name
print(host)
port = 54321                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()        # Establish connection with client.
print('Got connection from')
print(addr)
cont = True
markerList = []
while cont: #while the client has not sent the Disconnect signal
    msg = c.recv(4096)
    if(msg == "Disconnecting"): #session ended
        cont = False
        print(msg)
    elif (msg=="Dumping"):
        c.send("Ready")
        stillRecv = True
        while (stillRecv):
            msg=c.recv(4096)
            msg = msg.strip("\n ' '") 
            if(msg[0]=='{'):
                temp=Marker(0,0,'NA')
                msg = msg.strip("\n ' '") #trim trailing whitespace
                #records = msg.split('\n') #turn line delimited JSON records into list of JSON records      
                markerList.append(temp.jsonLoad(msg))
                print markerList[-1].jsonDump()
                c.send(str(markerList[-1].GUID))
                msg = c.recv(4096)
                if (msg=="OK"):
                    #print msg
                    c.send("Ready")
            elif(msg=="Done"):
                    c.send(str(len(markerList)))
                    msg = c.recv(4096)
                    if (msg == "Equal"):
                        print msg;
                        stillRecv=False
                
                
                    
                    
            
        
c.close()
