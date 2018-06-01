import socket               # Import socket module
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostbyname(socket.gethostname()) # Get local machine name
print(host)
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from')
    print(addr)
    c.send(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    c.close()                # Close the connection
