import threading
from random import randint
from datetime import datetime
import Response as Res
import Request as Req
from Response import Response
MAX_BUFFER = 2048

class Client(threading.Thread):
    listfriends = []
    listgroups = []
    
    def __init__(self,socketRecv,socketSend):
        self.connectionRecv = socketRecv[0]
        self.addressRecv = socketRecv[1]
        self.connectionSend = socketSend[0]
        self.addressSend = socketSend[1]

        threading.Thread.__init__(self)
        self.messageTime = ""
        self.messageLast = ""
        self.messageNow = ""
        self.group = []
    
    def setAkun(self,name):
        self.name = name
    
    def getAkun(self,name):
        return [self.name,self.index]
    
    def setEnv(self,friends = [],listgroups = []):
        self.listfriends = friends
        self.listgroups  = listgroups
    
    def sendMessage(self,message):
        try:
            self.connectionSend.sendall(message)
            print ('send Message',self.addressSend)
        except:     
            print('failed send message',self.addressSend)
            
    def getMessageLast(self):
        return self.messageLast
    
    def getMessageNow(self):
        message = self.messageNow
        return message
    
    def run(self):
        while True :
            try:
                print("--run--")
                newRequest = self.connectionRecv.recv(2048)
                newRequest = Req.decode(newRequest) 
                message = newRequest.content['message']
                self.messageLast = message
                self.message = message
                print("-------------------------new send")
                print(message)
                self.broadcast(message)
                print("--done--")
            except:
                self.listfriends.remove(self)
                del self
                return 
                

    def broadcast(self,messege):
        print(self.listfriends)
        newResponse = Res.Response(211)
        newResponse.content({'message':'kukembalikan '+messege})
        for i in self.listfriends:
            if i.is_alive():
                if i == self : 
                    print('self')
                    newResponse.content['messege'] = 'ping'
                    i.sendMessage(newResponse.encode())
                else :
                    print('other')
                    i.sendMessage(newResponse.encode())
        print("-------------------------end send")
    
    def __del__(self):
        print (self.address," dropped")
        return
    