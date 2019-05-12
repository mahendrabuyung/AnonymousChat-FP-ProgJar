import socket
import Response as Res
import Request as Req
import threading
import queue 


serverSend = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverRecv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_ADDRESS = '127.0.0.1'
PORT_RECV = 3010
PORT_SEND = 3000
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

def recvForever():
    while True:
        if resQueue.empty() == queue.Empty:
            continue
        myRes = serverRecv.recv(2048)
        myRes = Res.decode(myRes)
        print(myRes.content)

def sendForever():
    while True:
        if reqQueue.empty() == queue.Empty:
            continue
        order = reqQueue.get()
        serverSend.sendall(order)

#-----------------------Send Request----------------#
def register(name="Anonymous",pic=None):
    request = Req.Request(100)
    content = {}
    USER_NAME = name
    content['name']=USER_NAME
    content['profil']=pic
    content['message']='Melakukan Register Awal'
    request.content = content
    return request.encode()

def createGroup(name,info=None):
    request = Req.Request(102)
    content = {}
    content['owner']=USER_NAME
    content['group']=name
    content['message']='Melakukan Register Group'
    content['info']=info
    request.content = content
    return request.encode()

def destroyGroup(name):
    request = Req.Request(103)
    content = {}
    content['owner']=USER_NAME
    content['group']=name
    content['message']='Melakukan Penghapusan Group'
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
    request = Req.Request(201)
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
    USER_FTP =  response.content['ftpUser']
    TOKEN_FTP = response.content['ftpToken']

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





recv = threading.Thread(target=recvForever)#getEveryResponse
send = threading.Thread(target=sendForever)#sendEveryResponse

recv.start() 
send.start() 
#recv.join()
#send.join()

reqQueue.put(register('Sora'))

while True:
    raw = str(input())
    order = Res.Response(201)
    order.content({'message':raw})
    reqQueue.put(order.encode())

