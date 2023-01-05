## Brian Riendeau
#  This is a simple web browser using sockets in python.
## python code is formatted in unicode and must be encoded and sent as utf-8
## we decode the utf-8 we get back back into unicode

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()


