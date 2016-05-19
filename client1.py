
import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 4700                # Reserve a port for your service.

s.connect((host, port))
while True:
	Msg = raw_input('Send Msg:')
	if Msg:
		s.send(Msg)
		Reply = s.recv(1024)
	if Reply:
		print 'Received Msg:' , (Reply)
	
s.close                     # Close the socket when done
