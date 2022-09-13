import socket
import os
import socketserver
import tqdm


VERSION_CLIENT = "8.0.1"
SEPARATOR = "<SEPARATOR>"
filename = "asier.txt"
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8804))


while True:
    sock.send(bytes(VERSION_CLIENT.encode()))
    sock.recv(BUFFER_SIZE).decode()
    file = open(filename, "w")
    sock.send("Filename received.".encode())
    data = sock.recv(BUFFER_SIZE).decode()
    file.write(data)
    file.close()
    print("File received")
    sock.close()
    
    
    """received = sock.recv(BUFFER_SIZE).decode()
    file, filesize = received.split(SEPARATOR)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {file}", unit="B", unit_scale=True, unit_divisor=1024)
    open(file,"wb")
    f = open(file,"wb")
    data = sock.recv(1024).decode()
    bytes_read = sock.recv(BUFFER_SIZE)
    f.write(bytes_read)
    progress.update(len(f))
    print(data)
connect.close()"""




    """ with open(file, "wb") as f: 
        while True:
            bytes_read = sock.recv(BUFFER_SIZE)
            if not bytes_read: 
                print("finished") 
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
        data = sock.recv(1024).decode()
        print(data)

        sock.close()
                """
