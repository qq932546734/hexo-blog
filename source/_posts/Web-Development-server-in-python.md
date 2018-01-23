---
title: 'Web Development: server in python'
date: 2017-12-17 16:09:57
tags:
categories:
    - [Python, Basics]
---

There are several modules designed for web development in python:
- socket
- socketserver
- http
- wsgiref

### What's a socketserver?
From previous posts we know the socket is a node through which to communicate with other node on the Internet. A socketserver in the server side keeps listening to requests(abstract) and handle the requests or relay it to other RequestHandler to deal with. Thus, to instantiate a socketserver, server_address and RequestHandlerClass should be passed in as arguments. Functionality of a socketserver should include start a server (create a socket, bind it to a local port, listen for incoming request), handle request, shutdown the server.

### Request and RequestHanlder

`Request` represent different entity for TCP protocol and UDP protocol. In `TCPServer`, `Request` is a newly created socket, which will be passed to `StreamRequestHandler` for processing. While in `UDPServer`, `Request` is the received data, equal to the return value of `socket.recv()`. Given this difference in `Request`, their `RequestHandler` are also different in implementation.

### socketserver.py
{% asset_img socketserver.png %}
```py



```
