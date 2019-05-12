import threading
from random import randint
from datetime import datetime
MAX_BUFFER = 2048

class Client(threading.Thread):
    listfriends = []
    
    def __init__(self,socket_accept):
        self.connection = socket_accept[0]
        self.address = socket_accept[1]
        threading.Thread.__init__(self)
        self.messageRecv = ""
        self.messageTime = ""
        self.messageLast = ""
        self.messageNow = ""
        self.group = []
    
    def setAkun(self,name):
        self.name = name
    
    def setfriends(self,friends):
        self.listfriends = friends

    def tambahGroup(self, name):
        self.group.append(name)

    def getAkun(self,name):
        return [self.name,self.index]
    
    def sendMessage(self,message):
        try:
            self.connection.send(message.encode())
            print ('send Message')
        except:
            
            print(self.address,'failed send message')
    
    def getMessageLast(self):
        return self.messageLast
    
    def getMessageNow(self):
        message = self.messageNow
        
        return message
    
    def run(self):
        while True :
            try:
                print("--run--")
                message = self.connection.recv(2048)
                self.messageLast = message.decode()
                self.messageNow = message.decode()
                print(self.getMessageLast())
                print(self.listfriends)
                self.sendMessage(self.getMessageLast())
                self.broadcast(self.getMessageLast())
                
                print("--done--")
            except:
                del self
                return

    def broadcast(self,messega):
        for i in self.listfriends:
            if i.is_alive() == True :
                i.sendMessage(messagee)
                print('send done to ',i.address)
    
    def __del__(self):
        print (self.address," dropped")
    