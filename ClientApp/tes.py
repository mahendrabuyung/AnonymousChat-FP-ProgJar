from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer  # <-
from pyftpdlib.authorizers import DummyAuthorizer
import threading

authorizer = DummyAuthorizer()
def run():
    authorizer.add_user('user', '12345', 'store',perm='elradfmw')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('127.0.0.1', 2121), handler)
    server.serve_forever()


def adduser():
    while True:
        k = input()
        authorizer.add_user(k, '12345', '.')

run = threading.Thread(target=run)
add = threading.Thread(target=adduser)

run.start()
add.start()

