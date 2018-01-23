---
title: Socket programming
date: 2017-12-10 14:18:55
tags:
categories:
    - [Python, Basics]
---

### In server side
In the server side, one socket is created for listening incomming requests, which is often refered as 'server socket'. Each time when a request comes in, a new socket will be created to handle this request by receiving incoming data. This newly created socket is 'client socket'. Client sockets are normally only used for one exchange (or a small set of sequential exchanges).
- create a socket
    ```py
    serversocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
    ```
- Bind the socket to a local port
    ```py
    serversocket.bind(('localhost', 80))
    # OR 
    serversocket.bind(('127.0.0.1'), 80)
    ```
    But in the above case, this socket is only visible within this machine, which means you can't access it through local network. To fix this:
    ```py
    serversocket.bind((socket.gethostname(), 80))
    # OR, so that the socket is reachable by any address the machine happens to have
    serversocket.bind(('', 80))
    ```
- listen for incoming requests
    ```py
    serversocket.listen(5)
    ```
    The argument indicates how many requests can be queued before refusing outside connections.
- handle incomming reqeusts
    ```py
    while True:
        (clientsocket, address) = serversocket.accept()
        # `client_thread` is a function to create a new thread.
        ct = client_thread(clientsocket)
        ct.run()
    ```
    The serversocket generates a clientsocket by `accept()`. There are three general ways to deal with the client socket. 
    + dispath a thread to hanle it(the example).
    + create a new process to handle it.
    + use `select`. 
     
    In conclusion, the `server socket` only listen for the incoming requests and generate a client socket which will be used by the application to read the request data and send data out.


### In client side
First, we create a socket and connect it to a remote server through IP address and port. After connecting with remote server, this socket is used to send in a request for the text of the page. The same socket will read the reply(in [python official documentation](https://docs.python.org/3.6/howto/sockets.html#creating-a-socket), it say that the socket will be destroied after receiving data from server. That's not true. Actually, as long as the connection lasts, the client socket can always be used for sending and receiving data). Notice that the life cycle of a socket in client side is similar to the `client socket` in server side.:+1:
- Create a socket
- connect to a remote server
- send request

### A simple server and client
- Server side code
    ```py 
    import socket

    s = socket.socket()
    s.bind(('', 80))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        while True:
            data = clientsocket.recv(20)
            if not data:
                break
            print("received data:", data)
            clientsocket.send(data)
    s.close()
    clientsocket.close()

    ```
- client side code
    ```py
    import socket

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1', 80))

    send_message = "This is a long text to be sent to the server".encode()

    clientsocket.send(send_message)

    while True: 
        receive_message = clientsocket.recv(20)
        if receive_message is None:
            break
        print(receive_message)

    ```

### Rethink about my previous confusions
1. what's request?
    Through the above study, we know that the data sent or received by a socket are just some encoded text (Encoding a string is to convert them to bytes with the rule defined by the encoding system, such as utf8). These data is nothing special. An apparent disadvantage of using raw text for communication is the trouble along with interpreting these data. Then comes HTTP. It requires applications to structure their data in a specified form. Thus, the request in python is type of `dict`.
2. the components of wsgi?


### A complete example
```py
import socket
from threading import Thread
from socketserver import ThreadingMixIn
 
class ClientThread(Thread):
 
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ip+":"+str(port)
 
    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print "received data:", data
            conn.send(data)  # echo
 
TCP_IP = '0.0.0.0'
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
 
while True:
    tcpsock.listen(4)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = tcpsock.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)
 
for t in threads:
    t.join()
```

__NOTE__: Ports below 1024 are considered 'privileged' and can only be bound to with an equally privileged user(read: root). So you may have to run this script as root or with `sudo`.

### Different level protocols
When we create a socket, we have to decide its protocol, such as TCP or UDP. This is the internet protocol. After creating that socket, we can use it to send and receive data. But how to interpret these message/text should be agreed between the client and the server. This is also a protocol, which is refereced to as application protocol. Then most common one is HTTP.

### Using internet socket for IPC on one machine
> If you do decide to use AF_INET sockets, bind the “server” socket to 'localhost'. On most platforms, this will take a shortcut around a couple of layers of network code and be quite a bit faster. -[python](https://docs.python.org/3.6/howto/sockets.html#ipc)
