import socket
import sys
import os
import string
from random import choice
from Client import Client
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer

serverSend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRecv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverRecv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT_RECV = 3000
PORT_SEND = 3010
PORT_FTP  = 3020
IP_ADDRESS = '127.0.0.1'
MAX_BUFFER = 2048

serverRecv.bind((IP_ADDRESS, PORT_RECV))
serverSend.bind((IP_ADDRESS, PORT_SEND))

serverRecv.listen(1000)
serverSend.listen(1000)

listClients = []
publicGroups = ['public']
listusersftp = DummyAuthorizer()

#-----------Free Function
def randstring():
    all_char = string.ascii_letters + string.digits
    random = "".join( choice(all_char) for x in range(30))
    return random
#-----------Free Function done


def runFTP():
    try:
        handler = FTPHandler
        handler.authorizer = listusersftp
        serverFTP = ThreadedFTPServer((IP_ADDRESS,PORT_FTP),handler)
        serverFTP.serve_forever()
    except:
        print("FTP cannot Run")
        return

def adduserFTP(user,password):
    try:
        listusersftp.add_user(user,password, 'files', perm='elradfmw')
    except:
        print("Cannot add User :",user)
        return


#Ftp dijalankan sebagai thread agar userftp bersifat dinamis(dapat ditambah)
FTPForever = Thread(target=runFTP)

try:
    #FTP mulai
    FTPForever.start()
    while True:
        client = Client(serverRecv.accept(),serverSend.accept())
        listClients.append(client)

        #randomisasi userlogin dan password
        userFTP = randstring()
        passwordFTP = randstring()

        #penambahan user ke server FTP
        adduserFTP(userFTP,passwordFTP)


        # handler = FTPHandler
        # handler.authorizer = listusersftp
        # listusersftp.validate_authentication(userFTP, passwordFTP, handler)


        #set Environment for kliens -> tetangga yang aktif
        client.setEnv(listClients,listusersftp)

        #set akun FTP dan password yang nanti akan disend ke clientapp
        client.setAkunFTP((userFTP,passwordFTP))
        client.start()

except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")


