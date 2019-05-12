import socket
import Response as Res
import Request as Req
import threading


serverSend = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverRecv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_ADDRESS = '127.0.0.1'
PORT_RECV = 3010
PORT_SEND = 3000
MAX_BUFFER = 2048

serverSend.connect((IP_ADDRESS,PORT_SEND))
serverRecv.connect((IP_ADDRESS,PORT_RECV))



def recvForever():
    while True:
        myRes = serverRecv.recv(2048)
        myRes = Res.decode(myRes)
        print(myRes.content)

def sendForever():
    while True:
        myReq = Req.Request(201)
        mes = str(input())
        myReq.content = {'message':mes}
        serverSend.sendall(myReq.encode())


recv = threading.Thread(target=recvForever)
send = threading.Thread(target=sendForever)

recv.start()
send.start()
recv.join()
send.join()



