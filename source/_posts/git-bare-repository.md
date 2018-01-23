---
title: git bare repository
date: 2017-11-21 08:49:37
tags:
categories:
    - [Tools, Git]
---
## What's a bare git repository?

There are two way to initialize a git repository: `git init` and `git init --bare`. They end up with different file structure. `git init` creates a subfolder inside repo directory named `.git`, inside which contains all version control related files and folders. `git init --bare` create a bunch of folders and files, which are the same as that inside `.git` folder. In summary, bare repository store git revision history of your repo in the root foler of your repostiry instead of in a `.git` subfolder.  

You may notice that when you create a repository for you local project, you can't share it with others. I mean, you have to push this to github or gitlab and tell others the link to clone that project. And before you push your code to remote server, you have to create a remote repostory on github or gitlab. Here we see the difference: the local repository you created with `git init` and eidt your code is a normal repotiry, it servers as a place for working; the remote repository you created(usually done on a web page) is a bare reposity, it functions as a centralized place for sharing. No one will be able to directly work on a bare repository because there is no 'normal' file there.

Usually, a bare reposity is customarily given a `.git` extension. That explains why the link to a github repostory often ends with `.git`. Since presumably bare repository is assumed to server as the origin repository for some remote users, command like `git status`, `git push` and `git pull` doesn't work on bare repository since it does not have a default remote origin respository.

working/work tree: the normal file and folders we are working on in a local repository.

## setup a git bare repository on your server

Actually, you don't have to setup gitlab on your server in order to use git for version control. A git bare repository on your server can do that as well. 
```bash
Set up the new bare repo on the server:
$ ssh myserver.com
Welcome to myserver.com!
$ mkdir /var/git/myapp.git && cd /var/git/myapp.git
$ git --bare init
Initialized empty Git repository in /var/git/myapp.git
$ exit
Bye!

Add the remote repository to your existing local git repo and push:
$ cd ~/Sites/myapp
$ git remote add origin ssh://myserver.com/var/git/myapp.git
$ git push origin master
```

## The structure of the `.git` directory

|HEAD    | config      | hooks | objects
branches| description | info  | refs

### HEAD
content: `ref: refs/heads/master`
### config
```
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
    ignorecase = true
    precomposeunicode = true
```
### hooks
