---
title: Nginx Cookbook
date: 2017-11-05 10:33:31
tags:
---
### How to determine the location of configuration files?  
Use `nginx -h`. By the time it tells you how to use command `nginx` with various arguemnts, it also shows you some important information, such as `prefix path` and `default configuration file location`. Usually, the confinguration file is named *nginx.conf* and placed in directory */usr/local/nginx/conf* (), */etc/nginx* (CentOS) or */usr/local/etc/nginx* (MacOS).

### Configuration

```
use nginx
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen 80;
        server_name 47.95.233.200;
        root /home/deployer/note_on_github/qq932546734.github.io;
    
        
        location / {
            #proxy_set_header Host $http_host;
            #proxy_set_header X-Real_IP $remote_addr;
            #proxy_pass http://127.0.0.1:8000;
        }
    }



    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /home/deployer/note_on_github/qq932546734.github.io;
        #/usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2 default_server;
#        listen       [::]:443 ssl http2 default_server;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers HIGH:!aNULL:!MD5;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        location / {
#        }
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}
```
Settings are divided into simple directive and block directive. A simple directive consists of the name and parameters separated by spaces and ends with a semicolon; while block diretive is similar to simple directive but the arguments are replace by brace-surrounded collections of simple directive. Block directive containing block directives is called context. The outmost context (where simple directives reside) is the `main` context. Thus contexts like `http` and `event` are in the main context.

### rules for nginx to choose which file to serve  
If there are several matching location blocks nginx selects the one with the longest prefix.

### Send signal to nginx
```
$ nginx -s <signal>
```
where signal can be 
* stop: fast shutdown (ignoring requested being processed)
* quit: graceful shutdown (wait until finishing current requests)
* reload: reloading the configuration file
* reopen: reopening the log files

> Note: pay attention to user privileges, consider to execute these commands prefixed with sudo

### Some basics about Nginx

> nginx has one master process and several worker processes. The main purpose of the master process is to read and evaluate configuration, and maintain worker processes. Worker processes do actual processing of requests.

The nginx master process id is written to file `/var/run/nginx.pid` or `/usr/local/nginx/logs/nginx.pid`. By killing nginx master process, the server will be shut down gracefully.



> nginx employs event-based model and OS-dependent mechanisms to efficiently distribute requests among worker processes. The number of worker processes is defined in the configuration file and may be fixed for a given configuration or automatically adjusted to the number of available CPU cores.

* event-based model:

# Test nginx after you change the configuration
`nginx -t` will test the settings and show the syntax error if any.

[For reference](http://nginx.org/en/docs/beginners_guide.html)
