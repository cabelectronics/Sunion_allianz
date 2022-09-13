from re import sub
import socket
import subprocess
import os
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('88.15.63.247', 7001)
CLIENT_VERSION_file = open('version.txt', 'r')
CLIENT_VERSION = CLIENT_VERSION_file.read()

subprocess.call('UIs/Updates/dist/sr_updates/sr_updates.exe', creationflags=0x08000000)

try:

    # Send data
    print('sending {!r}'.format(CLIENT_VERSION))
    sent = sock.sendto(CLIENT_VERSION.encode('utf-8'), server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
    if data == b'0000000070':
        subprocess.call('UIs/Updating/dist/updating/updating.exe', creationflags=0x08000000)
        print('Starting send_receiver.py')
        #subprocess.call('send_server.exe', creationflags=0x08000000)
        #For evaluation porpuses:
        path = os.getcwd()

        os.system('python '+ str(path)+'/send_receiver.py')
        
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif data == b'0000000080':
        print('Correct Version')
        #sock.shutdown()

        subprocess.call('python main.py')
        #Start main.exe
except:
    print('Unable to connect to server')

    
print('closing sockett')

sock.close()
sys.exit()

