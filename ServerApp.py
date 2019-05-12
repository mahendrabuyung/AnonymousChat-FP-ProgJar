import socket
import sys
import os
from Client import Client
from threading import Thread

serverSend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRecv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverRecv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT_RECV = 3000
PORT_SEND = 3010
IP_ADDRESS = '127.0.0.1'
MAX_BUFFER = 2048

serverRecv.bind((IP_ADDRESS, PORT_RECV))
serverSend.bind((IP_ADDRESS, PORT_SEND))

serverRecv.listen(1000)
serverSend.listen(1000)

listClients = []
publicGroups = ['public']

try:
   while True:
        client = Client(serverRecv.accept(),serverSend.accept())
        listClients.append(client)
        client.setEnv(listClients)
        client.start()
        #print(listclients)
except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")