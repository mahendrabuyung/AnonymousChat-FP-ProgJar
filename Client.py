import threading
from random import randint
from datetime import datetime

MAX_BUFFER = 2048

class Client(threading.Thread):
    val = randint(1,1000)
    messageRecv = ""
    messageTime = ""
    messageLast = ""
    messageNow = ""
    idle = False
    

    def __init__(self,socket_accept):
        self.connection = socket_accept[0]
        self.address = socket_accept[1]
        self._stop_event = threading.Event()
        threading.Thread.__init__(self)
    
    def setAkun(self,name,index):
        self.name = name
        self.index = index

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
                self.messageRecv = message.decode()
                self.messageNow = message.decode()
                self.sendMessage('masuk')
                
                print("--done--")
            except:
                del self
                return

    def __del__(self):
        print (self.address," dropped")