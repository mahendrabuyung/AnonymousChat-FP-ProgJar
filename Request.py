import pickle

#request Kode
TESTING  = 999
INITIATILION_REQUEST  = 100
CREATE_GROUP_REQUEST  = 102
DESTROY_GROUP_REQUEST = 103
SEND_MESSAGE_REQUEST  = 201
SEND_FILE_REQUEST     = 202
LOGOUT_REQUEST       = 500

class Request :
    def __init__(self,code=999):
        self.code = code
    
    def content(self,content):
        self.content = content

    def encode(self):
        return pickle.dumps(self)

def decode(object):
    return pickle.loads(object)