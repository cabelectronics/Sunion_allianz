import socket
import os

VERSION_CLIENT = '8.0.1'
filename = 'asier.txt'
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 8192 # send 4096 bytes each time step
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8888  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(VERSION_CLIENT, 'utf-8'))
    data = s.recv(1024).decode()

    print(data)
    s.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                
                conn.sendall(data)
                print(data)
    
'''received = s.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)'''

    
print(f"Received {data!r}")
