---
title: Double underscore usage
date: 2017-12-10 13:13:55
tags:
categories:
    - [Python, Basics]
---

### `__all__`
Before we discuss its function, we should know the syntax of `from <module> import *`. By default, `from <module> import *` will import all variables in the module not starting with underscore. But if `__all__` is defined in the module, `import *` from this module will only import variables included in `__all__`. Although `from <module> import *` is not recommended to use in normal case since it may cause variable name conflict, it can be used in combination with setting `__all__` in that module.  

In conclusion, `__all__` only affect the behavior of `from <module> import *`. But variables defined in the module while not inclued in `__all__` can still be imported through the normal import syntax `from <module> import <variable>`.
