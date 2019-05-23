import threading
from random import randint
from datetime import datetime
import Response as Res
import Request as Req
from Response import Response
from ftplib import FTP
MAX_BUFFER = 2048

class Client(threading.Thread):
    listfriends = []
    listfriends_ftp = []
    
    def __init__(self,socketRecv,socketSend):
        self.connectionRecv = socketRecv[0]
        self.addressRecv = socketRecv[1]
        self.connectionSend = socketSend[0]
        self.addressSend = socketSend[1]
        self.profilPic = ""

        threading.Thread.__init__(self)
        self.messageLast = ""
        self.messageNow = ""
        self.myGroup = []
        self.myGroup.append("public")
        self.tripcode = None

    def setAkunFTP(self,ftp):
        self.userftp     = ftp[0]
        self.passwordftp = ftp[1]
    
    def getAkunFTP(self):
        return [self.userftp,self.passwordftp]
    
    def setEnv(self,friends = [],friends_ftp=None):
        self.listfriends = friends
        self.listfriends_ftp = friends_ftp
    
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
        self.messageNow = ""
        return message

    def successMessage(self):
        newResponse = Res.Response(410)
        newResponse.content={'status':'success'}
        return newResponse.encode()
    
    def failedMessage(self):
        newResponse = Res.Response(410)
        newResponse.content={'status':'failed'}
        return newResponse.encode()
    
    def run(self):
        while True :
            try:
                print("--run--")
                print("client active  : ",self.listfriends)
                print("")
                newRequest = self.connectionRecv.recv(2048)
                newRequest = Req.decode(newRequest) 
                
                print(newRequest.code)
                if newRequest.code == 202: #Permintaan Broadcast File
                    message = newRequest.content['message']
                    file = newRequest.content['file']
                    filename = newRequest.content['filename']
                    self.messageLast = message                
                    self.messageNOW = message
                    print("-------------------------new send------------------")
                    print(message)
                    self.broadcast(message,file,filename)
                    print("--done--")

                elif newRequest.code == 201: #Permintaan Broadcast
                    message = newRequest.content['message']
                    targetgroup = newRequest.content['toGroup']
                    self.messageLast = message                
                    self.messageNOW = message
                    print("-------------------------new send------------------")
                    print(message)
                    self.broadcast(message, toGroup=targetgroup)
                    print("--done--")

                elif newRequest.code == 102: #Permintaan ganti nama
                    print("-------------------------Change Name-------------")
                    if(self.name!=None):
                        oldName = self.name
                    else:
                        oldName = ""
                    newname = newRequest.content['newname']
                    self.name = newname
                    print('dari :',oldName)
                    print('to :',self.name)

                    newResponse = Res.Response(310)
                    content = {}
                    content['message'] = "Name changed to "+ self.name
                    newResponse.content = content
                    self.sendMessage(newResponse.encode())
                    
                    print("--done name--")

                elif newRequest.code == 103: #Permintaan tambah group
                    content = newRequest.content
                    self.messageLast = content['message']
                    self.messageNOW = content['message']
                    self.myGroup.append(content['newgroup'])
                    print("-------------------------new send------------")
                    print(self.myGroup)
                    self.sendMessage(self.successMessage())
                    print("--done--")

                elif newRequest.code == 104: #Permintaan hapus group
                    content = newRequest.content
                    self.messageLast = content['message']
                    self.messageNOW = content['message']

                    print("-------------------------new send------------")
                    print(self.myGroup)
                    print(content['delgroup'])
                    checkflag = True
                    for i in self.myGroup:
                        if i == content['delgroup']:
                            checkflag = False
                            self.myGroup.remove(content['delgroup'])
                            print("qwert")
                            self.sendMessage(self.successMessage())

                    if checkflag == True:
                        self.sendMessage(self.failedMessage())
                    print(self.myGroup)
                    print("--done--")
                
                elif newRequest.code == 100: #Permintaan insisiasi
                    content = newRequest.content
                    self.name = content['name']
                    self.profilPic = content['profil']
                    print(content['message'])
                    self.sendMessage(self.successMessage())

                    newRes = Res.Response(110)
                    content = {}
                    content['userftp']  = self.userftp
                    content['tokenftp'] = self.passwordftp
                    newRes.content = content
                    self.sendMessage(newRes.encode())
                    print("--done--")

                elif newRequest.code == 500:
                    self.listfriends.remove(self)
                    del self

            except:
                self.listfriends.remove(self)
                del self
                return 

    def broadcast(self,message,file=None,filename=None,toGroup='public'): 
        #fungsi ini bertugas melakukan broadcasting pesan atau file


        newResponse = Res.Response(211)
        content = {}
        content['sender'] = self.name
        content['message'] = message


        if(file!=None):
            newResponse.code = 212
            content['file']      = file
            content['filename']  = filename

        content['toGroup'] = toGroup

        newResponse.content = content
        for friend in self.listfriends:
            if friend.is_alive():
                if toGroup in friend.myGroup:
                    if friend == self :

                        newResponse2= Res.Response(211)
                        content2 = {}
                        content2['sender'] = "YOU"
                        content2['message'] = message
                        content2['toGroup'] = toGroup
                        newResponse2.content = content2
                        self.sendMessage(newResponse.encode())
                    else :
                        friend.sendMessage(newResponse.encode())



    def __del__(self):
        print("----------------------dropped------------------------")
        self.listfriends_ftp.remove_user(self.userftp)
        print (self.name," Recaive adress")
        print (self.addressRecv," Recaive adress")
        print (self.addressSend," Send adress")
        print("----------------------dropped------------------------")
        return
    