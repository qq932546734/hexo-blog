---
title: Event Driven Concurrency
date: 2017-12-07 09:49:35
tags:
categories:
    - [Python, Basics]
---

### Multiple processing
- Different process have separate address space and variables/context.
- methods unitlized for IPC include: File, Socket, Queue, Pipe

### Mutliple threading
- shared memory space and variables/context between threads
- communication is generally simpler
- you don't have to worry about the switch between different threads, it's a task managed by the kernel
- You still need to deal with race condition.

### Event driven

Imaging there are 100 function/request you want to call to a server. All of these function will be implemented as coroutine. Although we execute these coroutine sequentially(maybe the order is not guranteed), once we hit a blocking the coroutine will return the control and proceeding with the next coroutine function. 

Thus, we are not waiting for any of these fuction to finish and singal us their finished state, we are continuously processing on these coroutine and move forward once we got blocked, which means the fd related to that coroutine is not ready. As a conclusion, despite the name of `event driven`, the main process is not just waiting for a singal notifing their completion, instead, the main process keeps checking their states (in a special way).


