---
title: python related
date: 2017-11-15 16:20:17
tags:
---


## When we have a large list and want to write items in that list into a file, of course, I want to do some modification on these items, so what's the best practice concerning performance? Write line by line or write in one shoot?

## Python character

1. Dynamic characteristic. A variable can refer to different types of data during its life cycle.
2. Although list in python is similar to array in other static languages, list can hold items of different types, which is not allowed in other static languages.
3. Reference and primary compared with mutable and immutable type in python
4. Be careful when using `[a_list] * 5` to produce a new list if items in `a_list` contains reference type.
5. After mporting `sys`, `sys.path` will list all the path which will be searched for modules and packages.

### Any
`any(iterable)`: return true is any of the items is true.


### Memory usage of list and tuple
The `sys` module provide a function `getsizeof()` to inspect the memory usage of objects. But for container type object, it returns only the size fo container itself, while items are not included. The container size is different for `list` and `tuple`. `list` will extend its size periodicaly, while since `tuple` is immutable, its container size is in proportion to the number of its items.

### Key-only parameters and positional-only parameters
- Key-only parameters: `fn(**key_params)`
- positional-only parameters: `fn(*positional_params)`

### How to run a script in background process?
When you close a terminal window, the terminal emulator sends a SIGHUP to the process it is running, your shell. Your shell then forwards that SIGHUP to everything it's running. On your local system, this is the ssh. The ssh then forwards the SIGHUP to what it's running, the remote shell. So your remote shell then sends a SIGHUP to all its processes, your backgrounded program.

There are 2 ways around this.

- Disassociate the backgrounded program from your shell.
    - Use the disown command after backgrounding your process. This will make the shell forget about it.
    - Prefix your command with nohup (nohup $python program.py &). This accomplishes the same thing, but by using an intermediate process. Basically it ignores the SIGHUP signal, and then forks & executes your program which inherits the setting, and then exits. Because it forked, the program being launched is not a child of the shell, and the shell doesn't know about it. And unless it installs a signal handler for SIGHUP, it keeps the ignore action anyway.

- Use logout instead of closing the terminal window. When you use logout, this isn't a SIGHUP, and so the shell won't send a SIGHUP to any of its children.

Additionally you must make sure that your program doesn't write to the terminal through STDOUT or STDERR, as both of those will no longer exist once the terminal exits. If you don't redirect them to something like /dev/null, the program will still run, but if it tries to write to them, it'll get a SIGPIPE, and the default action of SIGPIPE is to kill the process). [link](https://unix.stackexchange.com/questions/134924/i-am-using-why-isnt-the-process-running-in-the-background)


### Metaclass

```py
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if not 'bar' in body:
            raise TypeError('subclass should have method .bar()')
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):

    def foo(self):
        return self.bar()

```

### Confusions

1. immutable and mutable
