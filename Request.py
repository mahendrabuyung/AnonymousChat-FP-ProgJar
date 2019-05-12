import pickle

CREATE_GROUP  = 102
DESTROY_GROUP = 103
SEND_MESSAGE  = 201
SEND_FILE     = 202

class Request :
    def __init__(self,kode=201):
        self.kode = kode
    
    def content(self.message,file=None):
        if(file==None):
            self.message = message
        else :
            self.message = message
            self.file = file
    def save(self):
        return pickle.dumps(self)
    def load(self):
        retrun pickle.loads(self)

p = Request