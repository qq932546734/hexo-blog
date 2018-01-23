---
title: Pipenv
date: 2017-12-06 20:13:40
tags:
    - pipenv
    - virtual environment

categories:
    - [Python, Basics]
---
### What's pipenv?
Virtual envrionment is very useful for python in that it can help us to avoid conflict between different versions of the same package. Also it facilitates us to work on different version of python.

The oldest one should be `virtualenv` package. Then it comes `venv` with python 3.4 (I am not sure) officially. Now a better option emerges, `pipenv`.
It works like `npm`, generating a `Pipfile` as `package.json`. It aims to make up type less.

> Pipenv — the officially recommended Python packaging tool from Python.org, free (as in freedom).


### Installation
1. Install `pipenv` with homebrew
```shell
$ brew isntall pipenv
```
2. cd to your working directory, create your desired-version python virtual environment
```shell
// Install a specified version python
$ pipenv --python 3.5
// Or, just python 2.x or python 3.x
$ pipenv --two
$ pipenv --three
```
3. Then you can install dependecies as normal dependency or development dependency, you can generate a lock file for your virtual env. To enter into the virtual env
```shell
//install dependencies and save them to your Pipfile
$ pipenv install pytest --dev
$ pipenv install tornado
// Enter virtual environment, get ready to work
$ pipenv shell
// which is equal to run a command inside your virtial environment
$ pipenv run python
```
4. Next time when others using you package, they can create the same virtual envronment just as yours
```
// Only install default dependencies
$ pipenv install
// Or install all dependencies including those used in development 
$ pipenv install --dev
```

### Other functions you may need
- remove virtual environment
```shell
$ pipenv uninstall --all
```
- find the location of your virtual environment
```
$ pipenv --venv
// locate python interpreter
$ pipenv --py
```
- output the location of your project
```
$ pipenv --where
```

### Remove virtual envrionment
```
$ pipenv uninstall --all
```

### `Pipfile` and `Pipfile.lock`


