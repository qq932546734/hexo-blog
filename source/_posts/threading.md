---
title: threading
date: 2017-12-17 17:12:10
tags:
categories:
    - [Python, Modules]
---

### Threading

#### How to use threading.Event?
This is a example from [stackoverflow](https://stackoverflow.com/questions/18485098/python-threading-with-event-object)

```py
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            print "something"
            self.event.wait(120)

# Then you may create a thread and start it in your main thread
timer = TimerClass()
timer.start()
# At this moment, you just created a new thread and something is running on it.
# If you want to stop that thread, just do
timer.event.set()
```
Thus, `Event` is used for controlling the thread from outside.


#### Threading.local


