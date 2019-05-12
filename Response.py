import pickle

#response kode
TESTING  = 999
INITIATILION_RESPONSE  = 110
CREATE_GROUP_RESPONSE  = 112
SEND_MESSAGE_RESPONSE  = 211
SEND_FILE_RESPONSE     = 212
UPDATE_RESPONSE        = 300

class Response :
    def __init__(self,code=999):
        self.code = code
    
    def content(self,content):
        self.content = content

    def encode(self):
        return pickle.dumps(self)

def decode(object):
    return pickle.loads(object)