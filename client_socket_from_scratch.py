import socket

SERVER_IP = '192.168.50.167'
SERVER_PORT = 28283
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
SIZE = 1024



while True:
    msg = input()

    client_socket = socket.socket()

    client_socket.connect(SERVER_ADDR)
    client_socket.send(msg.encode())
    msg_recv = client_socket.recv(SIZE)


    print(msg_recv.decode())

