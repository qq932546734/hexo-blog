---
title: SublimeLinter Installation trouble shooting
date: 2017-11-09 16:52:36
tags:
---


The confusing documentation sucks!!!

To make linter, such as flake8 for python, eslint for javaScript, funtion well, install packages as following:
1. install `sublimeLinter`;
2. install `sublimeLinter-flake8` for python / `sublimeLinter-contri-eslint` for js.
3. install the linter executable, and add the binary executable's paraent path to the Path environment variable. To find the path for that specific executable, use command `which flake8` or `which eslint` to locate them. 



```
Traceback (most recent call last):
  File "/Users/chengguohua/Library/Application Support/Sublime Text 3/Packages/SublimeLinter/lint/util.py", line 247, in generate_color_scheme_async
    scheme_text = sublime.load_resource(scheme)
  File "/Applications/Sublime Text.app/Contents/MacOS/sublime.py", line 192, in load_resource
    raise IOError("resource not found")
OSError: resource not found
```
This error doesn't represent that sublimeLinter is out of function, although what it indicates is still unknown.