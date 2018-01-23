---
title: Python format
date: 2018-01-02 10:10:50
tags:
categories:
    - [Python, Basics]
---

```py
'{} {}'.format('one', 'two')
'{} {}'.format(1, 2)
'{1} {0}'.format('one', 'two')

'{:f}'.format(43)
'{:d}'.format(42)

'{:4d}'.format(42)
# '  42'
'{:04d}'.format(2)
# '0042'
'{:6.2f}'.format(3.14159265)
# '  3.14'
'{:06.2f}'.format(3.14159265)
# '003.14'


# Represent %s and %r
'{0!s} {0!r}'.format(CustomClass())
```

### Padding
```py
'%10s' % 'test'
# equal to 
'{:>10}'.format('test')
# '       test'
'{:10}'.format('test')
# 'test       '

'{:_<10}'.format('test')
# 'test_ _ _ _'

'{:^10}'.format('test')
# '_ _ test _ _'
```

### Named placeholder
```py
'{first} {second}'.format(second='something', first=42)
params = {'first': 42, 'second': 'something'}
'{first} {second}'.format(**params)

'{person.name}'.format(person=Person())
'{person[0]}'.format(person=personList)
```

### Datetime
```py
from datatime import datetime

'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))
```









