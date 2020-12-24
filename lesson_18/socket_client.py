import socket
import time

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    s.send(b'Hello!')
    data = s.recv(1024)
    print(data)
    time.sleep(3)

