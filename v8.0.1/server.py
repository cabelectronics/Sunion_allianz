import socket
import os

VERSION_SERVER = '8.0.2'
filename = 'bego.txt'
filesize = os.path.getsize(filename)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 8192 # send 4096 bytes each time step
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8888  # Port to listen on (non-privileged ports are > 1023)


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
                VERSION_CLIENT = str(data)
                if VERSION_SERVER==VERSION_CLIENT:
                    print("very well manuel")

                else:
                    s.close()
                    break

            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send("hello".encode())
    data = s.recv(1024).decode()

    print(data)




#s.send(f"{filename}{SEPARATOR}{filesize}".encode())
#data = s.recv(1024) 