---
title: vs code
date: 2017-12-06 20:47:57
tags: [Shortcuts]
categorise:
    - [Tools, vscode]
---


### Workspace specific setting 
Inside `.vscode` file are workspace specific settings file.

### Common Shortcuts
- open debug panel: `Command+j`
- format code: `Shift+Option+f`
- command palette: `Shift+Command+p`
- quick open file/ seach file: `Command+p`
- open multiple files form quick open: `right arrow`
- jump to error or warning: `Command+Shift+m`
- change language: `Command+k, then m`
- toggle sidebar: `Command+b`
- zen mode: `Command+k, then z`
- side by side editing: `hold Command, then select file from the sidebar`
- navigate back: `Ctrl+-`
- navigate forward: `Ctrl+Shift+-`
- navigate among the recently opened file: `Ctrl+Tab`
- multi cursor selection: `Option+Command+up_arrow`
- go to symbol in file(such as functions, classes): `Command+Shift+O`
- shrink/expand selection: `Ctrl+Shift+Command+left_arrow/right_arrow`
- code folder: `Option+Command+'['/']'`
- select current line: `Command+i`
- preview markdown: `Shift+Command+v`

### Tips
1. If you want import or link a file that does not exist right now, hold on `Command` then click on that link to create the file in the specified place.


### VS Code for python
#### Set Python Interpreter for VSCode
Open `Command Palette` (Shift+Command+P), type `select interpreter` and a list of python interpreter will show up if you have multiple python installed. Choose one if that's your desired python version. However, in most case python interpreter in your virtual environment won't show up. 

#### Make Test Available
By default, tests(including unittest, pytest, nosetest) are disabled. 
- To enable one of these tests(enable only one test framework at a time), open setting, search `python.unitTest.unittestEnabled` or `python.unitTest.pyTestEnabled` to enable `UnitTest` or `pyTest` respectively. 
After enabling testing, you should instructe vscode where to find your test code. 
- By default, `python.unitTest.unittestArgs` is `["-v", "-s", ".", "-p", "*test*.py"]`, where `-v` represent verbose output; `-s .` means to find test code in the current working directory(the outmost folder); `-p *test*.py` tell how to match test code file. For example, if you test code is inside the `test` folder, change `-s .` to `-s test`.


