import socket

# 내 IP 및 포트, 보낼 용량
IP = '192.168.50.167'
PORT = 28283
SIZE = 1024
ADDR = (IP,PORT)

server_socket = socket.socket()
server_socket.bind(ADDR)
server_socket.listen()
print('started')

client_socket, client_addr = server_socket.accept()
msg = client_socket.recv(SIZE)
msg = str(msg.decode())
client_socket.close()

print(msg)