## Brian Riendeau

# Building a web server using python
# A browser client application always triggers the bidirectional connection
# by sending a line of communication to the server through a request like GET or POST.
# the server processes the requests, does its operations and sends the response to the browser (HTML, etc)
# these software applications communicate at some address and port.

from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-r\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n");
    except Exception as exc:
        print("Error:\n");
        print(exc)

    serversocket.close()

print("Access http://localhost:9000")
createServer()
