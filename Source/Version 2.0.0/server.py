import socket               # Import socket module
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = '169.254.114.139'    # Get local machine name
print(host)
port = 54321                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print('Got connection from')
print(addr)
    
while True:
    msg = c.recv(4096)
    print(msg)
c.close();

