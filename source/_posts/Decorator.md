---
title: Decorator
date: 2017-11-12 22:58:28
tags: 
    - python
categories:
    - [Python, Basics]
---

There are two approachs to implement a decorator: function and class.

A function decorator:
```python
def my_decorator(fn):
    def inner():
        do_something_before()
        fn()
        do_something_after()
    return inner
```
A function decorator:
```python
def my_decorator(fn):
    def inner(*args, **kwargs):
        do_something_before()
        fn(*args, **kwargs)
        do_something_after()
    return inner
```
A function decorator which can accept arguments:
```py
def my_decorator(first, second, third):
    def outter(fn):
        def inner(*args, **kwargs):
            do_something_before(first, second, third)
            fn(*args, **kwargs)
            do_something_after(first, second, third)
        return inner
    return outter
```

## A class decorator
```py
class DecaratorClass:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        self.fn(*args, **kwargs)
```






