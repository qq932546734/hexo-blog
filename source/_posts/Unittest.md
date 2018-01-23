---
title: Unittest
date: 2017-11-18 23:24:55
tags:

categories:
    - [Python, Basics]
---

### Difference between unittest and functional test
Functional test test the application from the point of view of the user, while unittest test if from the perspective of the programmer.
Functional test helps you build an application with the right functionality and gurantee that you will never break it; the unittest helps your write code that is clean and bug-free. More importantly, although they seems to be two totally different thing, functional test are actually accomplished with module `unittest` (or its modified version such). Each test inside a functional test is not testing certain function, they are implemented to test one of the application's functionalities.

{% asset_img unit_functinal_test.png %}

#### How to use functional and unit test at the same time?
The functional test should be the ultimate judge of whether our application works or not. When we want to add a function to our application, we write the corresponding functional test. Then to make the functional test pass, we divide it into serveral steps, and write unittest for each step. After satisfy all the unit test, we should be able to satisfy our funcitonal, which means we finished adding this functionality. 

## How to start a test?

```
# execute test modules
$ python -m unittest test_module1 test_module2
$ python -m unittest test_module1.py
$ python -m unittest tests/test_something.py
# execute in verbose module
$ python -m unittest -v tests/test_something.py 

# execute test case
$ python -m unittest test_module.TestClass

# execute test method inside particular test case
$ python -m unittest test_module.TestClass.test_method

# test with test discovery, both of following approaches are equal
$ python -m unittest
$ python -m unittest discover
```
We can also write test execution inside each module so that we can just run each python file with no need to specify `-m unittest`.
```
if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## useful options for test
* -b, --buffer: buffer the output and error, then discard them if passed, or show them as normal if failed;
* -c, --catch: 

## setup and tear down

- `setUp()` and `tearDown()` are to be executed for each test method. 
- If `setUp()` succeeded, `tearDown()` will be run whether the test method succeeded or not.
- `setUpClass()` is called before tests in an individual class run. It has to be marked as a classmethod by `@classmethod`. The same for `tearDownClass()`.
-  `setUpModule()` and `tearDownModule()` should be implemented as functions, as they are executed before or after for each module (python file).

## skipping tests and expected fialures

To skip certain test, the simple senaria is to use the `@unittest.skip(message)` decorator to skip particular test method or test case. There are also many other skip schedules:
1. `skipIf(condition, message)`
2. `skipUnless(condition, message)`. 
3. raise exception `unittest.SkipTest(reason)` if you catch an error and don't want the error make the test fail. 
If a test method is going to fail anyway, mark it as expected failure with `@unittest.expectedFailure`

## assert function available to use

- `assertEqual(first, second, msg=None)`
- `assertNotEqual()`
- `assertTrue(expr, msg=None)`
- `assertFalse(expr, msg=None)`
- `assertIs(first, second, msg=None)`
- `assertIsNot(first, second, msg=None)`
- `assertIsNone(expr, msg=None)`
- `assertIsNotNone(expr, msg=None)`
- `assertIn(first, second, msg=None)`
- `assertNotIn(first, second, msg=None)`
- `assertIsInstance(obj, cls, msg=None)`
- `assertNotIsInstance(obj, cls, msg=None)`

## supress warning and expection

```
with self.assertWarns(SomeWarning):
    # this function will raise a SomeWarning instance
    do_something()

self.assertWarns(SomeWarning, do_something, *args, **kwargs)

with self.assertRaises(SomeException):
    # this function will raise an error
    do_something()

self.assertRaises(SomeException, do_something, *args, **kwargs)
```

## Raise exception intendedly

`self.fail(msg=None)`

# Best Pratices

## Put preparation of resources to setUpClass instead of setUp
If we can make sure that the resource is read only, which means it won't be modified by any test methods, and it will be used by all or almost all test methods, we should consider put it in the `setUpClass()`. This will speed up our test for each run. But be careful, if some test method is going to change the resource and other test methods rely on its state, this approach does not work. It may cause some unexpected result. 

### Tips and Tricks
- When refactoring code, don't change the application's fucntionality. When refactoring test code, don't change the application code. Do do more than one thing at one time.
- In unittest, when we use `self.assertTrue()`, we should provide an second argument to this method which will remind us the purpose of this assertion. If it failed, the error message will be obvious for us to know what's going wrong.





