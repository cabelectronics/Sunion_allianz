from socket import *
import os
from pathlib import Path


CHUNKSIZE = 1_000_000

# Make a directory for the received files.
#os.makedirs('client',exist_ok=True)

sock = socket()
sock.connect(('81.42.248.10',7001))
with sock,sock.makefile('rb') as clientfile:
    while True:
        raw = clientfile.readline()
        if not raw: break # no more files, server closed connection.

        filename = raw.strip().decode()
        length = int(clientfile.readline())
        print(f'Downloading {filename}...\n  Expecting {length:,} bytes...',end='',flush=True)
        current_path = os.getcwd()
        main_path = Path(os.getcwd())
       
        
        print(str(main_path))
        path = os.path.join(str(main_path),filename)
        os.makedirs(os.path.dirname(path),exist_ok=True)

        # Read the data in chunks so it can handle large files.
        with open(path,'wb') as f:
            while length:
                chunk = min(length,CHUNKSIZE)
                data = clientfile.read(chunk)
                if not data: break
                f.write(data)
                length -= len(data)
            else: # only runs if while doesn't break and length==0
                print('Complete')
                continue
                

        # socket was closed early.
        print('Incomplete')
        break 
