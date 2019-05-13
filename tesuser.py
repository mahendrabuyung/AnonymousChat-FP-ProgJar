from ftplib import FTP
import string
import os
from random import choice

ADDRESS_FTP = ('127.0.0.1',21)
serverFTP = FTP()

def randstring():
    all_char = string.ascii_letters + string.digits
    random = "".join( choice(all_char) for x in range(30))
    return random

def connectFTP(IP_ADRESS,PORT):
    serverFTP.connect(host=IP_ADRESS,port=PORT)

def sendFile(filename):
    file,extension = os.path.splitext(filename)
    req_file = open(filename,"rb")

    serverFTP.storbinary("STOR "+randstring()+extension,req_file)
    req_file.close()

def downloadFile(filename):
    file,extension = os.path.splitext(filename)
    get_file = open("cache/"+filename,'wb')
    serverFTP.retrbinary("RETR "+filename,get_file.write,)
    get_file.close()

connectFTP('127.0.0.1',2121)
serverFTP.login("user","12345")
serverFTP.getwelcome()
sendFile("Client.py")
downloadFile("tes.py")



