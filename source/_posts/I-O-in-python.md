---
title: I/O in python
date: 2017-12-28 09:33:25
tags:
categories:
    - [Python, Basics]
---

### Best pratice of reading file
```py
# f is file object, an iterator.
with open('data.txt', encoding='utf8') as f:
    While True:
        line = f.readline()
        if not line:
            break
        print(line.rstrip())

# A more concise approach
with open('data.txt', encdoing='utf8') as f:
    for line in f:
        print(line.rstrip())
```
