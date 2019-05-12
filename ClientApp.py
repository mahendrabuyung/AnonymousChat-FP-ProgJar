import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP_ADDRESS = '127.0.0.1'
PORT_CHAT = 3000
MAX_BUFFER = 2048

server_socket.connect((IP_ADDRESS,PORT_CHAT))
while True:
    mes = str(input())
    server_socket.sendall(mes.encode())
    m = server_socket.recv(1024)
    print(m.decode())