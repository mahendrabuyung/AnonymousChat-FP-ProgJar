import pickle

#response kode
INITIATILION_RESPONSE  = 110
CREATE_GROUP_RESPONSE  = 112
DESTROY_GROUP_RESPONSE = 113
SEND_MESSAGE_RESPONSE  = 211
SEND_FILE_RESPONSE     = 212

class Response :
    def __init__(self,kode=211):
        self.kode = kode
    
    def content(self,content):
        self.content = content

    def encode(self):
        return pickle.dumps(self)

def decode(object):
    return pickle.loads(object)