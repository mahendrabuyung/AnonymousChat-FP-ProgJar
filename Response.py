import pickle

#response kode
INITIATILION_RESPONSE  = 110
RECV_MESSAGE_RESPONSE  = 211
RECV_FILE_RESPONSE     = 212
UPDATE_RESPONSE        = 310
FEEDBACK_RESPONSE      = 410

class Response :
    def __init__(self,code=999):
        self.code = code
    
    def content(self,content):
        self.content = content

    def encode(self):
        return pickle.dumps(self)

def decode(object):
    return pickle.loads(object)