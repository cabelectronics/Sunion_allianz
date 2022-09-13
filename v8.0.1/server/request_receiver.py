from re import sub
import socket
import subprocess
import os

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
CLIENT_VERSION_file = open('cl_version.txt', 'r')
CLIENT_VERSION = CLIENT_VERSION_file.read()

try:

    # Send data
    print('sending {!r}'.format(CLIENT_VERSION))
    sent = sock.sendto(CLIENT_VERSION, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
    if data == b'0000000070':
        print('Starting send_receiver.py')
        #subprocess.call('send_server.exe', creationflags=0x08000000)
        #For evaluation porpuses:
        path = os.getcwd()

        os.system('python '+ str(path)+'/send_receiver.py')

    elif data == b'0000000080':
        print('Correct Version')
        sock.shutdown()
        #Start main.exe

finally:
    
    print('closing sockett')
    sock.close()
    #Restart program