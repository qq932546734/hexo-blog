---
title: Fix autocompletion of python shell
date: 2018-01-13 17:52:09
tags: [autocompletion]
categories:
    [Python, Basics]
---

### Preface
I have got used to 'venv' module for python virtual environment for a long time. But although it works well, I want to try something else to make life easier. I have tried `pipenv` and `vritualenv`, both of them are great, until I meet the auto completion problem. In normal python shell, the auto completion function comes free without any setting. But when using these two modules the autocompletion does not work. `pipenv` works like `npm` for javascript, which provides many useful functions. `virtualenv` is relatively more popular since it has been introduced for a long time. To take advantage of them, we have to solve this problem.

### Solution
Wheneven we start a python shell, the `PYTHONSTARTUP` environment variable will be checked. If this variable is not empty, the referenced file will be executed. So, first, set this variable to a file in `.bash_profile` (on Mac).
```shell
export PYTHONSTARTUP="$HOME/.pythonstartup"
```
Then create the file `.pythonstartup` and add the following code:
```py
import rlcompleter, readline
readline_doc = getattr(readline, '__doc__', '')
if readline_doc is not None and 'libedit' in readline_doc:
    # work for mac
    readline.parse_and_bind('bind ^I rl_complete')
else:
    # for other OS
    readline.parse_and_bind('tab: complete')
print("I am working(this is an indication about autocompletion)")
```


