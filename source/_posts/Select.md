---
title: Select
date: 2017-12-07 08:54:59
tags:
categories:
    - [UNIX, SystemCall]
---

`select()` allows a program to monitor multiple file descriptors, waiting util one or more of the file descriptors become ready for I/O operation. A file descriptor is considered ready if it is possible to perform the corresponding I/O operation without blocking.

The system call `select()` is defined like this:
```c
int select(int nfds, fd_set *readfds, fd_set *writefds, fd_set *errorfds, struct timeval *timeout);
```
- nfds: each of these three different fd sets will have their own fd numbers. The maximum number plus one will be passed to select.
- readfds: fds to be checked for being ready to read.
- writefds: fds to be checked for being ready to write.
- errorfds: fds to be checked for error conditions pending.
- specifies a maximum interval to wait for selection to complete.

### Programming in python
[official documentation](https://docs.python.org/3/library/select.html#select.select)

### Edge triggering and level triggering

### select and epoll(kqueue)

### poll and epoll

epoll use a `bitmap` to monitor all fds, thus the maxmim size of fds epoll can monitor is limted to 1024(?). In addtion, epoll only monitor active socket.

### A GOOD PALCE FOR LEARNING UNIX
[turoialspoint](http://www.tutorialspoint.com/unix_system_calls/index.htm)

