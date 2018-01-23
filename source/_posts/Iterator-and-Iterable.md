---
title: Iterator and Iterable
date: 2017-12-28 08:56:09
tags:
categories:
    - [Python, Basics]
---

### The difference between `Sequence`, `Iterator` and `Iterable`
(A class having implemented `__iter__()` or `__getitem__()` is a sequence.)?
A `Iterable` will be called by `iter()` to produce an `Iterator`. As a priciple of `Iterable` protocol, each time we call `iter()` on `Iterable` a new, independent `iterator` should be created. Thus, a `Iterable` class should only implement `__iter__()` method, not `__next__()`, which means an `iterable` should never be a `iterator` at the same time. A good example from the book "Fluent Python":
```py
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):   
        return SentenceIterator(self.words)   

class SentenceIterator:

    def __init__(self, words):
        self.words = words   
        self.index = 0 
    def __next__(self):
        try:
            word = self.words[self.index]   
        except IndexError:
            raise StopIteration()   
        self.index += 1   
        return word   

    def __iter__(self):   
        return self
```
Although only `__next__()` is required for a formal `Iterator`, python `iterator` also has `__iter__()` method which return `self` due to the convention that an `iterator` should be iterable. Thus calling `iter()` on an `Iterator` will return the iterator itself, which is exactly the same object.

##### Iterator protocol
`__iter__()`: return the iterator object. 
`__next__()`: return the next element 

#### Sequence protocol
`__getitem__(index)`: return the element is the position of `index`

##### Caller function
- `next()` 
    + argument: an iterator
    + process: the iterator argument's `__next__()` method will be called 
    + return: the next element
- `iter()` 
    + argument: a sequence(?) 
    + process: the sequence argument's `__iter__()` method will be called
    + return: an iterator
    + explanation: this function is used to create an interator, not to travese a sequence. Since the minimal requirement for an interator is `__next__()` method, thus many `__iter__()` method return `self`.

##### For statement
`for` statement firstly call `__iter__()` method(or `__getitem__()`), which will return an iterator. Then `__next__()` method of the iterator will be called until a `StopIteration` error raised.

### Generator
A generator is produced by calling a function which has `yield` in its body. We ofter name that function as generator function or generator factory. In summary, calling a generator function return a generator object, while calling `next()` on a generator produces a value.

There are at least two kinds of generator object, one returned by calling generator function, one called generator expression and similar to list comprehension. Both of them can be called by `next()` function and works almost the same. Differenc only shows on their forms.

**NOTICE**: a return statement in a generator will raise a `StopIterator` error.
```py
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:   
            yield word   
        return   
```

### Lazy version Generator
```py
import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text

    # ...

    # Generator function version
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

    # Generator expression version
    def __iter__(self):
        return (match.group for match in RE_WORD.finditer(self.text))
```

### Advantage of using Iterator
- Saving resource: there is no need to keep all data in memory while we can still get the next item each time.













