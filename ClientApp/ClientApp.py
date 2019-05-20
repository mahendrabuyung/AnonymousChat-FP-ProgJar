import socket
import Response as Res
import Request as Req
import threading
import queue 
from ftplib import FTP
import os
from random import choice
import string

serverSend = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverRecv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverFTP  = FTP()

IP_ADDRESS = '127.0.0.1'
PORT_RECV = 3010
PORT_SEND = 3000
PORT_FTP = 3020
MAX_BUFFER = 2048

#-----------User Default 
USER_NAME = "Anonymous" #defaule username
USER_FTP  = "" 
TOKEN_FTP  = "" 
LIST_GROUP = []




reqQueue = queue.Queue()
resQueue = queue.Queue()




#------------------------------------------Server
#Connect To FTP
def connectFTP(IP_ADRESS,PORT,user,token):
    serverFTP.connect(host=IP_ADRESS,port=PORT)
    serverFTP.login(user,token)

newRes = None
#Listen Message
def recvForever():
    while True:
        newRes = serverRecv.recv(2048)
        newRes = Res.decode(newRes)
        resQueue.put(newRes)
        # if newRes.code == Res.INITIATILION_RESPONSE :
        #     initialization(newRes)
        # elif newRes.code == Res.RECV_MESSAGE_RESPONSE:
        #     print('GET MESSAGE')
        # elif newRes.code == Res.RECV_FILE_RESPONSE:
        #     print('GET FILE')
        #     file_response(newRes)
        # elif newRes.code == Res.UPDATE_RESPONSE :
        #     print('Will UPDATE TKINTER')
        # elif newRes.code == Res.FEEDBACK_RESPONSE:
        #     print('Will FEEDBACK RESPONSE')
        

#Send Message
def sendForever():
    while True:
        if reqQueue.empty() == queue.Empty:
            continue
        order = reqQueue.get()
        serverSend.sendall(order)
        print("qquee done")


recv = threading.Thread(target=recvForever)#getEveryResponse
send = threading.Thread(target=sendForever)#sendEveryResponse


def run(address, port_send, port_recv, port_ftp):
    IP_ADDRESS = address
    PORT_SEND = port_send
    PORT_RECV = port_recv
    PORT_FTP = port_ftp
    serverSend.connect((IP_ADDRESS,PORT_SEND))
    serverRecv.connect((IP_ADDRESS,PORT_RECV))
    register()
    recv.start() 
    send.start()


#------------------------------------------Server done


#-----------Free Function call in sendfile
def randstring():
    all_char = string.ascii_letters + string.digits
    random = "".join( choice(all_char) for x in range(30))
    return random
#-----------Free Function done

#-----------------------Send Request----------------#

#--->Khusus FTP
def sendFTP(filepath,random):
    ftp_connect()
    req_file = open(filepath,"rb")
    serverFTP.storbinary("STOR "+random,req_file)
    req_file.close()
    ftp_close()
#-----FTP done

def register(name="Anonymous",pic=""):
    request = Req.Request(100)
    content = {}
    USER_NAME = name
    content['name']=USER_NAME
    content['profil']=pic
    content['message']='Melakukan Register Awal'
    request.content = content
    reqQueue.put(request.encode())

def changeName(name):
    request = Req.Request(102)
    content = {}
    content['newname']=name
    request.content = content
    reqQueue.put(request.encode())

def addGroup(group):
    request = Req.Request(103)
    content = {}
    content['newgroup']=group
    content['message']='Permintaan Tambah Group'
    request.content = content
    reqQueue.put(request.encode())

def removeGroup(group):
    request = Req.Request(104)
    content = {}
    content['delgroup']=group
    content['message']='Permintaan destroy Group'
    request.content = content
    reqQueue.put(request.encode())

def sendMessage(message,toGroup ='public',info=None):
    request = Req.Request(201)
    content = {}
    content['sender']=USER_NAME
    content['toGroup']=toGroup
    content['message']=message
    content['info']=info
    request.content = content
    reqQueue.put(request.encode())

def sendFile(file,message=None,toGroup='public',info=None):
    request = Req.Request(202) 

    title,extension = os.path.splitext(file)
    randomName = randstring()+extension
    OriginName = title+extension
    sendFTP(file,randomName)
    
    content = {}
    content['sender']=USER_NAME
    content['toGroup']=toGroup
    content['message']=message
    content['file']=OriginName
    content['filename']=randomName
    content['info']=info
    request.content = content
    reqQueue.put(request.encode())



def logout():
    request = Req.Request(500)
    reqQueue.put(request.encode())

#-----------------------Send Request done----------------#

#-----------------------Recaive Response----------------#
#---->Khusuf FTP
def downloadFTP(file,filename):
    ftp_connect()
    get_file = open("cache/"+file,'wb')
    serverFTP.retrbinary("RETR "+filename,get_file.write,)
    get_file.close()
    ftp_close()
#---->FTP Done

def initialization(response):
    USER_FTP =  response.content['userftp']
    TOKEN_FTP = response.content['tokenftp']
    print("User : ",USER_FTP)
    print("Token : ",TOKEN_FTP)
    

def Update(response):
    USER_NAME  = response.content['name']
    LIST_GROUP = response.content['listgroups']
    USER_FTP   = response.content['ftpUser']
    TOKEN_FTP  = response.content['ftpToken']

def message_response(response):
    sender  = response.content['sender']
    message = response.content['message']
    toGroup = response.content['toGroup']

def file_response(response):
    sender   = response.content['sender']
    message  = response.content['message']
    file     = response.content['file']
    filename = response.content['filename']
    toGroup  = response.content['toGroup']
    downloadFTP(file,filename)
    print("download :",file)


def ftp_connect():
    connectFTP(IP_ADDRESS,PORT_FTP,USER_FTP,TOKEN_FTP)

def ftp_close():
    serverFTP.quit()

def logout():
    serverFTP.quit()
#-----------------------Recaive Response done----------------#



