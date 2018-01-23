---
title: Web Components
date: 2017-12-17 14:37:24
tags: [WSGI, middleware]
categories:
    - [Python, Basics]
    - [Web, Basics]
---

There are many web frameworks in python, such as Tornado, Django and flask. They all implement some common web components. This post is decicated to have a close look at these components and try to find out the differences of their implementation.

When the server received a request, the server handles it by producing a environment dictionary and a start_response function, then passing them to call WSGi application. The control is passed to the web framework/application, which firstly do some calculation then generate a response status and response headers. After that, the WSGI application begin to produce iterable data. The data will finally be send to client by the server. The reason why the produced data by the application should be iterable is for the convenience of middleware. In this way, the data could be processed by the middleware in a easier way.

- WSGI application are callable python objects
- the application has to start a response using the function provided and return an iterable where each yielded item means writing and flushing.
- the WSGI environment is like a CGI environment just with some addtional keys that are either provided by the server or a middleware.
- you can add middlewares to your application by wrapping it.

### WSGI Application

The standard for WSGI application is simple: 
```py
def application(env, start_response):

    start_response(`404`, response_headers)

    for data in iterable:
        # send data to client
```
`env` is a dictionary. `start_response` is a function, which takes two arguments, a standard HTTP status string such as `200` and a response_headers (a list of standard HTTP response headers.) It returns an iterable data.(not HTTP response, which should be handled during the calling of `start_response`) 

- framework: build the headers, call `start_response`, build the return data.
- server: server both the header and the data up via HTTP.

### WSGI middleware
Our WSGI application is a callable which can be run by just calling it. Middleware is nothing more than a wrapper around the WSGI application which does something else before or after the WSGI application get called. 

### Example code
```py
def simple_app(env, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

#### MIDLLE WARE
class Upperware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, env, start_response):
        for data in self.wrapped_app(env, start_response):
            return data.upper()

#### run
serve(simple_app)

wrapped_app = Upperware(simple_app)
serve(wrapped_app)
```

### Setting Nginx
```py
# this specifies that there is a WSGI server running on port 8000
upstream app_server_djangoapp {
    server localhost:8000 fail_timeout=0;
}

# Nginx is set up to run on the standard HTTP port and listen for requests
server {
  listen 80;

  # nginx should serve up static files and never send to the WSGI server
  location /static {
    autoindex on;
    alias /srv/www/assets;
  }

  # requests that do not fall under /static are passed on to the WSGI
  # server that was specified above running on port 8000
  location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_redirect off;

    if (!-f $request_filename) {
      proxy_pass http://app_server_djangoapp;
      break;
    }
  }
}
```


### WSGI and CGI
> WSGI runs the python interpreter on web server start, either as part of the web server process (embeded mode) or as a separate process (daemon mode), and loads the script into it. Each request results in a specific function in the script being called, with the request environment passed as argument to the function. CGI runs the script as a separate process each request and use environment variables, stdin and stdout to `communiate` with it.

CGI: common gateway interface, which was designed as a standard about how to send requests and how to response to requests. It defines what fields will be included in the `environment variable` which will be passed to the `CGI scripts`. Also, it confines the way of how to response the result. By convention, `cgi-bin` will be the directory from where the script will fetch the documents. 

WSGI: it's a similar standard designed for server writen in python. The `cgi scripts` in CGI becomes `application` here. But WSGI application accept the same arguments as `CGI scripts`, environment variables.
Except for the variables, it also accept a function which called `start_response`, which might be used to trigger the application. (I am not sure that function's purpose)


### Server and RequestHandler
