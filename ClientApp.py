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

USER_NAME = "Anonymous"

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

recv = threading.Thread(target=recvForever)
send = threading.Thread(target=sendForever)

recv.start()
send.start()
#recv.join()
#send.join()

while True:
    raw = str(input())
    order = Res.Response(201)
    order.content({'message':raw})
    reqQueue.put(order.encode())


def initialization(name="Anonymous",pic=None):
    request = Req.Request(100)
    content = {}
    USER_NAME = name
    content['name']=USER_NAME
    content['profil']=pic
    content['message']='Melakukan Register Awal'
    request.content = content
    return request.encode()

def createGroup(name,info=None,mes):
    request = Req.Request(102)
    content = {}
    content['owner']=USER_NAME
    content['name']=name
    content['info']=info
    content['message']='Melakukan Register Group'
    request.content = content
    return request.encode()
