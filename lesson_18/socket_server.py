import socket

HOST = '127.0.0.1'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)


while True:
    client_socket, addr = s.accept()

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data)
        client_socket.send(data[::-1])



