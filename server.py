import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 4700 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'
#Start listening on socket
s.listen(2)
conn0 , addr0 = s.accept()
print 'Connected with server' , addr0
conn1 , addr1 = s.accept()
print 'Connected with server' , addr1

print 'Socket now listening'
 
#now keep talking with the client
while (conn1 and conn0):
	#wait to accept a connection - blocking call
	data=conn0.recv(1024)
	conn1.send(data)
	data=conn1.recv(1024)
	conn0.send(data)	    

conn1.close()
conn0.close()
s.close()
