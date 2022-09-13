import socket
import os
import tqdm
 





VERSION_SERVER = "8.0.2"
filename = "bego.txt"
filesize = os.path.getsize(filename)
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8804))
sock.listen()

while True:
    connect, addr = sock.accept()
    data = connect.recv(1024).decode()
    VERSION_CLIENT = str(data)
    if VERSION_SERVER == VERSION_CLIENT:
        print("Same version, no updates available")
    else:
        print("Update required")
        file = open(filename, "r")
        data = file.read()
        connect.send(filename.encode())
        connect.recv(BUFFER_SIZE).decode()
        connect.send(data.encode())
        file.close()
        print("File send")
        connect.close()
    sock.close()
        
        
        
        
        
        
        
        
""" connect.send((f"{filename}{SEPARATOR}{filesize}".encode()))
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        open(filename,"rb").read(BUFFER_SIZE)
        f = open(filename,"rb").read(BUFFER_SIZE)
        connect.sendall(f)
        progress.update(len(f))
        data = connect.recv(1024).decode()
        print(data)
        connect.close()"""
        
        
""""with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                sock.sendall(bytes_read)
                progress.update(len(bytes_read))
                data = connect.recv(1024).decode()
                print(data)
            connect.close()"""
                


