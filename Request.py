import pickle

#request Kode
INITIATILION_REQUEST  = 100
CREATE_GROUP_REQUEST  = 102
DESTROY_GROUP_REQUEST = 103
SEND_MESSAGE_REQUEST  = 201
SEND_FILE_REQUEST     = 202
DESTROY_REQUEST       = 500

class Request :
    def __init__(self,kode=201):
        self.kode = kode
    
    def content(self,content):
        self.content = content

    def encode(self):
        return pickle.dumps(self)

def decode(object):
    return pickle.loads(object)