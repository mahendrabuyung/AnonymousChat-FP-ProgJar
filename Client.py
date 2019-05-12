import threading
from random import randint
from datetime import datetime
import Response as Res
import Request as Req
from Response import Response
MAX_BUFFER = 2048

class Client(threading.Thread):
    listfriends = []
    
    def __init__(self,socketRecv,socketSend):
        self.connectionRecv = socketRecv[0]
        self.addressRecv = socketRecv[1]
        self.connectionSend = socketSend[0]
        self.addressSend = socketSend[1]

        threading.Thread.__init__(self)
        self.messageTime = ""
        self.messageLast = ""
        self.messageNow = ""
        self.myGroup = "public"
    
    def setAkun(self,name):
        self.name = name
    
    def addGroup(self,group):
        self.myGroups.append(group)

    def getAkun(self,name):
        return [self.name,self.index]
    
    def setEnv(self,friends = []):
        self.listfriends = friends
    
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
                
                # if newRequest.kode == 201:
                #     message = newRequest.content['message']
                #     self.messageLast = message                
                #     self.message = message
                #     print("-------------------------new send")
                #     print(message)
                #     self.broadcast(message)
                #     print("--done--")
                # elif newRequest.kode == 102:
                #     newname = newRequest.content['newname']
                #     print(newname)
                #     print("-------------------------pepega send")
                #     self.name = newname
                #     self.selfbroadcast("name changed to"+ newname)
                #     print("--Kappa--")
                message = newRequest.content['message']
                self.messageLast = message
                self.message = message
                print("-------------------------new send")
                print(message)
                # print(newRequest.kode)
                self.broadcast(message)
                print("--done--")
            except:
                self.listfriends.remove(self)
                del self
                return 
                
    
    def ReplyRequest(self,request):
        content = request.content
        if(request.kode == 100):
            self.name = content['name']
        elif(request.kode == 102):
            self.name = content['newname']
        elif(request.kode == 103):
            self.group = content['newgroup']
        elif(request.kode == 201):
            self.broadcast('tes')

    def broadcast(self,messege,toGroup='public'):
        #bugging------------------
        print(self.listfriends)
        newResponse = Res.Response(211)
        newResponse.content({'message':'kukembalikan '+messege,"toGroup":toGroup})

        for friend in self.listfriends:
            if friend.is_alive():
                if self.myGroup in friend.myGroup:
                    if friend == self :
                        print('self')
                        newResponse.content['messege'] = 'ping'
                        friend.sendMessage(newResponse.encode())
                    else :
                        print('other')
                        friend.sendMessage(newResponse.encode())
        print("-------------------------end send")
    

    def selfbroadcast(self, message):
        newResponse = Res.Response(211)
        newResponse.content({'message':+message})
        for friend in self.listfriends:
            if friend.is_alive():
                if self.myGroup in friend.myGroup:
                    if friend == self:
                        print('changesomething')
                        friend.sendMessage(newResponse.encode())
                


    def __del__(self):
        print (self.addressRecv," dropped")
        print (self.addressSend," dropped")
        return
    