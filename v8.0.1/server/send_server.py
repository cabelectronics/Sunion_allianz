from socket import *
import os

CHUNKSIZE = 1_000_000

sock = socket()
sock.bind(('',8709))
sock.listen(1)

while True:
    print('Waiting for a client...')
    client,address = sock.accept()
    print(f'Client joined from {address}')
    with client:
        for path,dirs,files in os.walk('server'):
            for file in files:
                filename = os.path.join(path,file)
                relpath = os.path.relpath(filename,'server')
                filesize = os.path.getsize(filename)

                print(f'Sending {relpath}')

                with open(filename,'rb') as f:
                    client.sendall(relpath.encode() + b'\n')
                    client.sendall(str(filesize).encode() + b'\n')

                    # Send the file in chunks so large files can be handled.
                    while True:
                        data = f.read(CHUNKSIZE)
                        if not data: break
                        client.sendall(data)
        print('Done.')