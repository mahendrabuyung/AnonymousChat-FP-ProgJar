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

A = 11
listclients = []
try:
   while True:
        client = Client(server_socket.accept())
        listclients.append(client)
        client.setfriends(listclients)
        client.start()
        print(listclients)

except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")