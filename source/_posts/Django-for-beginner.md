---
title: Django for beginner
date: 2017-11-05 16:21:46
tags:
categories:
    - [Python, Django]
---

```
.
├── db.sqlite3
├── manage.py
├── demo
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── polls
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20171012_0435.py
│   │   └── __init__.py
│   ├── static
│   │   └── polls
│   │       ├── images
│   │       │   └── 2144.jpg
│   │       └── style.css
│   ├── templates
│   │   └── polls
│   │       ├── detail.html
│   │       ├── index.html
│   │       └── results.html
│   └── test.py
├── templates
│   └── admin
│       └── base_site.html
└── test.py

```

# START PROJECT
```shell
# start a project
$ django-admin startproject <project-name>

# run the development server
$ python manage.py runserver
# run the server in a different port other than 8000
$ python manage.py runserver 8080
# make the server listen to all public IP
$ python manage.py runserver 0:8080

# create a new App
$ python manage.py startapp <app-name>
```
# ROUTER
```py
# wirte views
# ./polls/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")

# ./polls/urls.py

from . import views
urlpatterns = [
    url(r"^$", views.index, name="index")
]

# mysite/urls.py

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]

```
`url(regex, view, kwargs)` is powerful. The first argument is expected to be a regular expression for matching url. 
* If it ends with '$', then the second argument of `url` should be a function which returns `HttpResponse`. 
* Else if it ends with '/', the regex will match the given url and then remainer will be pass to the another url patterns for matchning, where the second argument of `url` should be `include(<another_url>)`.    
The keyword arguments will be passed through to the final function which will handle the request. Inside the kwargs, `name` is special in that it enables you refer to this url from elsewhere in django.

# Modles
```py
# ./polls/models.py
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # We can add `class meta` here. There are many defined meta, such as `db_table`, `ordering`, `abstract` and so on.
    ordering = ["-pub_date"]    # descending by filed pub_date
    # The following are the field of this table
    question_text = models.CharField(max_length=200)
    pub_date = models.DataTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=model.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

`Field`s have an optional first positional argument to describe the field. A class in `models.py` represents a table in database, whose name by default is derived from the app name combined with the class name by an underscore. To override the database table name, use the `db_table` parameter in class Meta.

### The structure of Model class
- The class attributes we defined are fields of that table;
- `Field` can be initialized with several settings, such as `default='something'`, `null=True`, `editable=True`
- Some special name are reserved for options, refered as class meta;
- The approach a model class used to determine if a class attribute is a filed of that table is to check out the attribute's type. If the type is one of pulic filed defined in `django.db.models`, the attribute is a field. If the type is `django.db.models.Manager`, the attribute is a manager for this model class. The rest attributes will be tested for `class meta` settings.
- Each class inherits a class attribute from `django.db.models.model`. Its name is default to `objects` and its type is `django.db.models.model.Manager`. Each table class can have more than one manager.
- The `manager` class attribute can be used to subclass in order to add new  or modify functions to deal with database.

### CRUD with model
All of CRUD operations are handled through model class's class attribute, whose name defaults to `objects`. So if you have a table class named `Article`, you should use methods of `Article.objects` to accomplish that.
- c: create a new instance of that modle class and call its `.save()` method;
- r: to retrive all content, call `Article.objects.all()`; to retrive items meeting certain conditions, use `Article.objects.filter()`; or `Article.objects.get()`

### QuerySet
`Item.object.count()` will return its length.

**The difference between `filter()` and `get()`?**

```py
>>> from polls.models import Question, Choice
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="waht's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
>>> Question.object.filter(id=1)
>>> Question.object.filter(question_text__startswith='What')
>>> current_year = timezone.now().year()
>>> Question.objects.get(pub_date__year=current_year)
>>> Question.objects.get(id=2)
>>> Question.object.get(pk=1)
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
>>> q.choice_set.create(choice_text='not much', votes=0)
>>> q.choice_set.create(choice_text='the sky', votes=0)
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> c.question
>>> q.choice_set.all()
>>> q.choice_set.count()
>>> Choice.objects.filter(question__pub_date__year=current_year)
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

### Field options
- `null=True`: 
- `blank=True`
- `default=''`

### Database migrate
- `python manage.py makemigrations`: create the instruction about how to make databases. When we test our code with django `TestCase`, this instruction will be used to create test database for us. The real database will keep intact.
- `python manage.py migrate`: use the default database setting to create the database.

### 
`from django.db.models import Q`


# SETTINGS
### Database setting
All related settings will be accomplised in *mysite/settings.py*.
* ENGINE: 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'.
* NAME: The full path of file `db.sqlite3` if using SQLite. Else this is thte name of database, when `USER`, `PASSWORD` and `HOST` are required.
* For msyql, to set `pymysql` as mysql driver, add this at the begining of `manage.py`.
    ```py
    import pymysql
    pymysql.install_as_MySQLdb()
    ```


### other settings
* TIME_ZONE: local timezone
* INSTALLED_APPS: 'polls.apps.PollsConfig'
### Apply setting
The migrate command checks all the installed applications and create any necessary database table according to the settings.
```shell
# create necessary database for the project
# will be called also when we modified our models.
$ python manage.py migrate

# After change Apps, notify Django and then produce a `migreration` file, which can be executed by database server to make the change
# But this procudure is not necessary
$ python manage.py makemigrations polls
$ python manage.py sqlmigrate polls 0001
```
* To make creating mysql table work smoothly, add the following setting to `DATABASE` setting:
    - `'OPTIONS': { 'init_command': 'SET storage_engine=INNODB' }`
    - after setting this, you have to create the database by yourself. `CREATE DATABASE my_database CHARACTER SET utf8;`
### How to run scripts without setting problems?
1. We can start a shell with `pytho manage.py shell`;
2. Or we can set the `DJANGO_SETTINGS_MODULE` environment variable to `mysite.settings` and then `django.setup()` at the begining of the shell.

Both of the above approachse should be done when the current working directory is where *manage.py* stays.

### Test without creating test database
[link](https://stackoverflow.com/questions/5917587/django-unit-tests-without-a-db)

# Create an admin user
```shell
$ python manage.py createsuperuser
```
To make an app available in the admin index page, register that specific app.
```py
# polls/admin.py
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```





