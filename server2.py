import socket
import os

VERSION_SERVER = '8.0.2'
filename = 'bego.txt'
filesize = os.path.getsize(filename)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 8192 # send 4096 bytes each time step
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8888  # Port to listen on (non-privileged ports are > 1023)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))

sock.send("Sent from client...".encode())
print(sock.recv(1024).decode())
sock.close()