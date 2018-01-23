---
title: Custom Class inherited from built-in class
date: 2017-11-19 11:13:49
tags:
---
### Inherit from dict
```
class MyDict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


my = MyDict(a=1, b=2)

print(my['b'])
```