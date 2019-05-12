import socket
import sys
import os
from Client import Client
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT_CHAT = 3000
IP_ADDRESS = '127.0.0.1'
MAX_BUFFER = 2048

server_socket.bind((IP_ADDRESS, PORT_CHAT))
server_socket.listen(1000)

clientsGroup = {}
index = 0
a = []
try:

    #while True:
        print(a)
        p = Client(server_socket.accept())
        a.append(p)
        print(a)
        p.start()
        #p.join()
        while p.is_alive():
            print ('------------')
            print(p.getMessageLast())
            print(p.getMessageNow())
            print ('------------')
        
        print(a)

        #del p

except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")
