---
title: socket
date: 2017-12-06 23:23:30
tags:
---
### What's a socket?
Everything in unix is a file and you can read from or write to it through a corresponding file descriptor. The file descriptor is just a integer associated with a file, which could be a network connection, a FIFO, a pipe, a terminal or a real on-the-disk file. Thus to communicate with other program over the internet, the file descriptor will be involved. 

**After we create a socket, it can be used to read and write data. When we use the socket as a server socket, we bind it to a local address(an IP address and a port). The server socket does not receive data or send data directly. Instead, it will create new client socket to receive and send data for each incoming request. Thus, client sockets created by server socket will only be used once(receive once or receive and send data once). In client side, after creating a client socket, we don't bind it to a port(typically, `bind` only get called in server side). We connect this client socket to a remote address. After connecting successfully, the socket will be associated with a random avaiable port. In the case, we say a connection is built. As long as it does not disconnect with the remote server, this client socket can be used multiple times for sending and receiving data.**

In addtion, not all types of socket are designed for communication through the internet, Unix domain socket is used for inter process communication.

Socket provides implementation of `TCP` or `UDP` protocol.(__I am not so sure__)
- SOCK_STREAM: a reliable way which can gurantee the arrival of the data in the original order.
- SOCK_DGRAM: datagram may arrive out of order or may not arrive. It's a connectionless type which means you do maintain an open connection between local and remote port.

### Socket programming
Address family, used for the first argument to `socket()`
- socket.AF_UNIX: Unix domain socket, not networking socket.
- socket.AF_INET: networking socket.
- socket.AF_INET6: networking socket using ipv6.

Socket type, used for the second argument to `socket()`
- socket.SOCK_STREAM: TCP socket.
- socket.SOCK_DGRAM: UDP socket.

### Unix system call concering socket
__Note__: The argument names listed in the following functions are not exactly what the standard system call requires, I do this to give a brief concept about what these functions need. All of details about them can be found in man page, such as `man socket` or `man 2 bind`.

#### socket(domain, type, protocol)
Create a socket with the provided and return a fd associated with this socket.
#### bind(fd, address)
bind a socket given by its associated file descirptor to an address, namely the ip address and port. The address should be local address which you will used to communicate with other node. There are times you don't have to call this but call `connect()` directory because you are not going to use the socket to read or send data. In that cases, a unused port will be assigned automatically to the socket.
#### conncect(fd, address)
Just connect to a remote address. Return -1 if error.
(I am not sure if we have to call `connect()` before we call `listen()` on a newly created socket?)
Of course not since the purpose the `connect()` is connecting to a remote server and send a message.
#### listen(fd, backlog)
This happens in a server side, which will listen for any incoming requests.
#### accept()
This function is blocking if no incoming request.
#### send(bytes) and recv(buffer_size)
Argument for `send()` is bytes. `recv()` is a blocking function, waiting for data to read.
#### setsockopt(level, options, value)



### How does socket work?
> A socket can be referred to by a process (a running computer program) by using a socket descriptor, a type of handle (abstract reference, often represented internally as an integer). A process first requests that the protocol stack create a socket, and the stack returns a descriptor to the process so it can identify the socket. The process then passes the descriptor back to the protocol stack when it wishes to send or receive data using this socket. 
> 
> Sockets are local (specific to one node): they are local resources and cannot be referred to directly by other nodes, unlike ports. Further, sockets are not necessarily associated with a persistent connection (channel) for communication between two nodes, nor is there necessarily some single other endpoint. For example, a datagram socket can be used for connectionless communication, and a multicast socket can be used to send to multiple nodes, or an address range where there may or may not be any nodes to receive data. However, in practice for internet communication, sockets generally have associated addresses and often have a connection.    --wiki

A process which wants to communicate with outside will ask a protocol stack (protocol layer) to create a socket and a number representing the socket (socket descriptor) will be returned to the process. Then if the process can use this socket to send or receive data.

Communication between computers are identified through IP address and port. When an data pack comes in, the TCP/IP will handle it. Data will be processed and send to the specified socket identified by IP address and port. Thus the process (user application) can receive these data.

### Life cycle for a socket
#### In the server side
1. create a socket, you will get socket descriptor.
2. `bind` the socket to a socket address.
3. make the socket `listen` for incomming communication. You can define how many communication can be queued before you call `accept`.
4. accept a connection from a client, this will return a new socket descriptor, which is ready for `send()`` and `rece()`.The old descriptor is still listening for new connections, but this new one is connected to the client.
5. handle the connection and process data.
6. when done, close the connection.

#### In the client side
1. create a socket.
2. `connect` with a remote address.
3. Since the client isn't going to be accept()ing any incoming connections, there's no need for it to listen(). Of course, the client still uses send() and recv() for transferring data. That about sums it up.

### Socket terminology

- Socket Address: only a network/internet socket has socket address, it composed of the ip address and a port number in local node. The process of associating a socket address and a socket is called __binding__.
- Socket descriptor: like file descriptor, which is used to identify the socket/file itself.
- socket pair: I guess this one is only used for IPC. You can get a bidirectional pipe. (__I am not sure__)

### Unix domain socket

> A Unix domain socket or IPC socket (inter-process communication socket) is a data communications endpoint for exchanging data between processes executing on the same host operating system. Like named pipes, Unix domain sockets support transmission of a reliable stream of bytes (SOCK_STREAM, compare to TCP). In addition, they support ordered and reliable transmission of datagrams (SOCK_SEQPACKET, compare to SCTP), or unordered and unreliable transmission of datagrams (SOCK_DGRAM, compare to UDP). The Unix domain socket facility is a standard component of POSIX operating systems.
> 
> The API for Unix domain sockets is similar to that of an Internet socket, but rather than using an underlying network protocol, all communication occurs entirely within the operating system kernel. Unix domain sockets use the file system as their address name space. Processes reference Unix domain sockets as file system inodes, so two processes can communicate by opening the same socket.
> 
> In addition to sending data, processes may send file descriptors across a Unix domain socket connection using the sendmsg() and recvmsg() system calls. This allows the sending processes to grant the receiving process access to a file descriptor for which the receiving process otherwise does not have access. This can be used to implement a rudimentary form of capability-based security. For example, this allows the Clam AntiVirus scanner to run as an unprivileged daemon on Linux and BSD, yet still read any file sent to the daemon's Unix domain socket.  --wiki

### Socket compared with pipe

Socket is a two-way communications pipe, which can be used to communicate in a wide variety of domains.


