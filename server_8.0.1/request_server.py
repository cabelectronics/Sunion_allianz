import socket
import time
import subprocess
import os
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

INCORRECT_VERSION_msg = b'0000000070'
CORRECT_VERSION_msg = b'0000000080'

# Bind the socket to the port
server_address = ('192.168.1.189', 7001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

LAST_VERSION_FILE = open('version.txt', 'r')
LAST_VERSION = str(LAST_VERSION_FILE.read())

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    
    print(data)
    data = data.decode('utf-8')
    print(LAST_VERSION)
    if str(data) == LAST_VERSION:
        print('Correct version:', LAST_VERSION )
        sent = sock.sendto(CORRECT_VERSION_msg, address)
        sock.shutdown()
    else:
        print('Incorrect version:')
        #subprocess.call('send_server.exe', creationflags=0x08000000)
        #For evaluation porpuses:
        path = os.getcwd()
        sent = sock.sendto(INCORRECT_VERSION_msg, address)
        os.system('python '+ str(path)+'/send_server.py')

        
        
