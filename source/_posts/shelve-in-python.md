---
title: shelve in python
date: 2017-06-20 08:37:52
tags:
---
`Shelve` is a handy tool to persist objects in python. Open a file (use the name without its suffix) and treat it as a dictionary, store the target variable with a key in this dicitonary.  

Always remember to close the file before exiting or you may end up losing everything (you can do this use the `with` keyword). Closing the file will synchronous the cached file and file on the disk. 

We can persist many types, even the numpy data type. To get the keys:
```
keys = list(file.keys())
```

I keep encountering this error message:
```
SystemError: Negative size passed to PyBytes_FromStringAndSize
```

Something we should pay attention to:
1. Access the db from multiple threads
2. If you would like to persist a lot of variables in shelve db, you should not store them directly as dictionary. Instead, combine all of the variables into a dictionary, as store the dictionary to shelve db. 
3. The keys should not be chinese character.
4. The values prefer to be built-in type such as list, dict, rather than numpy data type.
5. If two program fetch the shelve db simultaneously, something unexpected are likely to happen.
6. I still failed to figure out what cause the approach to be so unstable.


The most sever problem when dealing with shelve db is its unstability. However, after doing lots of trial and experiments, I found what causes the unstability may be attributed to carelessness. First, I would like to check if the data is usable after each iteration. So I may open another CLI to check the content. But I often forget to close the file, resulting the destruction of the data. Two kinds of action may cause this destruction after running the fetching process.
1. I check the file and then forget to close it, and then just continue the fetching process. 
2. After validate the data and without closing it, I copy this file to backup it. The backup is not valid.


HASH: out of range

