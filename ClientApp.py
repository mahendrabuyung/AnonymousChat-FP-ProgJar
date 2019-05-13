import socket
import Response as Res
import Request as Req
import threading
import queue 
from ftplib import FTP

serverSend = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverRecv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_ADDRESS = '127.0.0.1'
PORT_RECV = 3010
PORT_SEND = 3000
PORT_FTP = 3000
MAX_BUFFER = 2048

#-----------User Default 
USER_NAME = "Anonymous" #defaule username
USER_FTP  = "" 
TOKEN_FTP  = "" 
LIST_GROUP = []

serverSend.connect((IP_ADDRESS,PORT_SEND))
serverRecv.connect((IP_ADDRESS,PORT_RECV))

reqQueue = queue.Queue()
resQueue = queue.Queue()


#-----------------------Send Request----------------#
def register(name="Anonymous",pic=""):
    request = Req.Request(100)
    content = {}
    USER_NAME = name
    content['name']=USER_NAME
    content['profil']=pic
    content['message']='Melakukan Register Awal'
    request.content = content
    return request.encode()

def changeName(name):
    request = Req.Request(102)
    content = {}
    content['newname']=name
    request.content = content
    return request.encode()

def changeGroup(group):
    request = Req.Request(103)
    content = {}
    content['newgroup']=group
    content['message']='Permintaan Ganti Group'
    request.content = content
    return request.encode()

def sendMessage(message,toGroup ='public',info=None):
    request = Req.Request(201)
    content = {}
    content['owner']=USER_NAME
    content['toGroup']=toGroup
    content['message']=message
    content['info']=info
    request.content = content
    return request.encode()

def sendFile(file,message=None,toGroup='public',info=None):
    request = Req.Request(202)
    content = {}
    content['owner']=USER_NAME
    content['toGroup']=toGroup
    content['message']=message
    content['file']=file
    content['info']=info
    request.content = content
    return request.encode()

#-----------------------Recaive Response----------------#
def initialization(response):
    USER_FTP =  response.content['userftp']
    TOKEN_FTP = response.content['tokenftp']

def Update(response):
    USER_NAME  = response.content['name']
    LIST_GROUP = response.content['listgroups']
    USER_FTP   = response.content['ftpUser']
    TOKEN_FTP  = response.content['ftpToken']

def message_response(reponse):
    sender  = response.content['sender']
    message = response.content['message']
    toGroup = response.content['toGroup']

def file_response(reponse):
    sender  = response.content['sender']
    message = response.content['message']
    file    = response.content['file']
    toGroup = response.content['toGroup']

    
def recvForever():
    while True:
        if resQueue.empty() == queue.Empty:
            continue
        newRes = serverRecv.recv(2048)
        newRes = Res.decode(newRes)
        print("code : ",newRes.code," | ",newRes.content)

        if newRes.code == Res.INITIATILION_RESPONSE :
            initialization(newRes)
        elif newRes.code == Res.RECV_MESSAGE_RESPONSE:
            print('GET MESSAGE')
        elif newRes.code == Res.RECV_FILE_RESPONSE:
            print('GET FILE')
        elif newRes.code == Res.UPDATE_RESPONSE :
            print('Will UPDATE TKINTER')
        elif newRes.code == Res.FEEDBACK_RESPONSE:
            print('Will FEEDBACK RESPONSE')

def sendForever():
    while True:
        if reqQueue.empty() == queue.Empty:
            continue
        order = reqQueue.get()
        serverSend.sendall(order)

recv = threading.Thread(target=recvForever)#getEveryResponse
send = threading.Thread(target=sendForever)#sendEveryResponse

recv.start() 
send.start() 
#recv.join()
#send.join()

reqQueue.put(register('Sora'))
#reqQueue.put(changeName('CUCKBOY69'))
while True:
    raw = str(input())
    order = Res.Response(201)
    order.content({'message':raw})
    reqQueue.put(order.encode())

