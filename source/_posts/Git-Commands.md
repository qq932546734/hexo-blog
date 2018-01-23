---
title: Git Commands
date: 2017-12-08 14:44:38
tags:
---


- check git remote url: git remote -v

> This will list the urls where to fetch and push, for all branches.p

- to exclude a directory, add `<folder>/` to file `.gitignore`. To remove an already existing file/folder from git index, we need to remove it explictly even we have add them in the `.gitignore` file: `git rm -r --cache <folder>/<file>`