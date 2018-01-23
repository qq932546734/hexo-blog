---
title: 'Django: HttpRequest and HttpResponse'
date: 2018-01-14 10:27:24
tags:

categories:
    - [Python, Django]
---

### HttpRequest

#### Attributes
- `POST`: like a dict, methods applying to dict can also used on this object. `request.POST['item']`, `request.POST.get('item', 'default')`
- 


### QuerySet
Most methods of QuerySet return a new QuerySet, which is separated from the original one. This means evaluate one of them won't affect the other.

##### Main method
- filter(**kwargs)
- exclude(**kwargs)
- 