---
title: Git Submodule
date: 2017-11-23 12:08:58
tags:
---



## Questions

1. How to clone a repo with submodules?
    With normal `git clone <url>`, submodules won't be cloned. By adding option `--recursive`, submodules will also be cloned(this require git with version 1.9 or later).
    ```shellsession
    $ git clone --recursive <url>
    // To make multiple clone process run simultaneously, add `-j8`, the number indicates how many cloning can run in parallel
    $ git clone --recursive -j8 <url>
    ```
    Alternatively, we can accomplish this manually after clone:
    ```shellsession
    $ git submodule init
    $ git submoudle update
    // Or in combination
    $ git submodule update --init
    ```
2. How to switch between different commit in the main Repo?
    If we just checkout to another commit in the main Repo, we will find that the submodule will not switch accordingly. So, we have to manually update submodules after we switch to another commit.
    ```shellsession
    $ git submodule update --init
    ```

### How to add submodules
Every submodule must have a URL which refere to its repo. 

### Where to do our modification?
After we clone the parent repo, the submodules are just folders. If you do anything inside these folders, 