---
title: 'Django: REST framework'
date: 2018-01-08 17:19:01
tags:
categories:
    - [Python, Django]
---

### Since Django apps are plugable, App is often designed as a package (including a `__init__.py` file) and often locate as a sibling folder of project directory.
```
Project/
├── db.sqlite3
├── firstApp
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── project
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

### `from rest_framework.filters import SearchField, OrderingField`


### REST
- 'GET': retrieve
- 'POST': create
- 'PUT': update, it include two sql operation: fetch the original record(s) and update that record
- 'PATCH': a single operation, such as increment certain field for our target record(s)
- 'DELETE': delete