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
fragRec = ""; # used to store part of a JSON record when the msg is fragmeneted
while cont: #while the client has not sent the Disconnect signal
    msg = c.recv(4096)
    if(msg == "Disconnecting"): #session ended
        cont = False
        print(msg)
    elif (msg[0]=='{'): #the msg is (presumably) a JSON record
        temp=Marker(0,0,'NA')
        msg = msg.strip("\n ' '") #trim trailing whitespace
        records = msg.split('\n') #turn line delimited JSON records into list of JSON records
        if (fragRec != ""): #If fragRec is in use
            if(records[0][0] == '{'):
               print "error" #this happens if a JSON record is not truncated
               print "fracRec: " +fragRec
               print "record: " +records[0]
            else:
                records[0] = fragRec + records[0] #reassemble JSON records
                fragRec = "" #fragRec is no longer in use

        if(records[-1][-1]!= '}'):
            fragRec = records.pop() #if the last recoords is not complete store it for later use
        for i in records:
            if (i[0] == '{'):
                markerList.append(temp.jsonLoad(i))
                print markerList[-1].jsonDump()
        
c.close()
