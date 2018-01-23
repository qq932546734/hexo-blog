---
title: 'Git: git bare repository in local network'
date: 2018-01-11 21:22:27
tags:

categories:
    - [Tools, Git]
---

### Preface
I have always beeing thinking about writing code in my protable computer but run the program in the local server. What confused me is how to sync my code to the server end each time I modify my code. Although `scp` can do this work, but it is hard to use and prone to go wrong. That's when `git` comes to my mind. 

The main idea is create a bare repository in the server and then add it as my remote upstream of existing working program. Each time I committed my code, I push it to the server and then in the server side using `git pull` to pull down the new code. Then run it!


### Procedure

1. create a bare repository on the server.
    ```shell
    cd gitbares
    mkdir myfirstrepository.git
    cd myfirstrepository.git
    git init --bare
    ```
2. git initialize my program and add the remote upstream
    ```shell
    cd <my_programe>
    # See if remtoe upstream is already existing
    git remote -v
    git remote remove <name>
    # add the remote upstream, the default name should be origin
    git remote add origin bnu1@172.16.160.203:~/gitbare/myfirstrepository.git
    # push the repo up
    git push -u origin master
    ```
3. In the server side, clone the repo to use it.
    ```shell
    cd <working_directory>
    git clone <relative_path_to_bare_repo>
    ```

DONE!!!

### details about git clone
When you add a remote repository to your existing repo and push it, if you don't specify which branch to push, by default all branches will be included. Then when you `git clone <rurl>`, by default all branch will be cloned. Even though `git branch` only show the master and `git branch -a` show other branch as remote branch, you can just type `git checkout <branchname>` to switch to another branch as they are local branch(maybe in reality there is no difference).




