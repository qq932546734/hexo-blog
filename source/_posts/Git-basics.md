---
title: Git basics
date: 2017-11-23 09:48:08
tags:
---

Even if you are just a new programmer, you know something about git becuase it is an essential tool for version control. We may be familar with those commands we used on a daily base, while the things happening under the hood is beyond our knowledge. This post is intended to cover some basic information we may want to know about git.
<!-- more -->
## Basics
### configuration file
There are three potential configuration file that will be loaded for git. 
1. `/etc/gitconfig`: due to its location, this configuration will be applied to every user if file does exist. You can specifically read from or write to this configuration file with `git config --system`
2. `~/.gitconfig` or `~/.config/git/config`: applied to the current user. This corresponds to `git config --global`
3. configuration file in the Git directory (inside the .git directory) of whatever repository you are currently using. 

Each configuration overrides its previous one

To set your identity: 
```
$ git config --global user.name 'ted'
$ git config --global user.email 'ted@lengendgh.top'
```
With option `--global`, the setting will be wirtten to the the second level configuration file. Without any option, the setting will only be applied to the current project.

You can also config which editor to use for inputing commit message. It defaults to the system deafult editor, such as vim.
```
$ git config --global core.editor vim
```
To list your settings, `git config --list`. See a specific setting, `git config user.name`

### Help with git command
Several options is available for this need.
```
$ git help <verb>
$ man git-<verb>
$ git <verb> -h
```

### Some confusing concepts
1. what does `git add` do?
Add files to stage area, no matter they are untracked or modified. 


## Introduction
[link](http://chimera.labs.oreilly.com/books/1230000000561/ch01.html)

A Git project is represented by a 'repository', which contains the complete history of the project from its inception. Each snapshot of the project content
(collections of files and directories) is called a `commit`. It contains the following information:

- Tree: a project content snapshot, A structure of nested files and directories representing a complete state of the porject.
- author identification: name, email adress, date
- committer identification: inforation about the one who commit to the repostory
- commit message: comment on the changes
- parent commit(s): indicating the immediately preceding states of the project content. Root commit has no parent commit. merge commit has multiple parent commits.


## Branches

- tip of branch: the latest commit on that branch.
- from time to time, you wil l merge serveral branches (often two).
- remote-tracking branches/ tracking branch: 
- 'detached HEAD' state: any checkout of a commit that is not the name of your branches will get you a detached HEAD.
- Branch is defined as all points reachable in the commit graph from the named commit (the tip of the branch). While it is implemented as refering to the tip of that branch.


> The author is the person who originally wrote the patch, whereas the committer is the person who last applied the patch. So, if you send in a patch to a project and one of the core members applies the patch, both of you get credit — you as the author and the core member as the committer.

## The object store




## Commands

```
// create a new branch
$ git checkout -b <new_branch> 
// switch to another branch
$ git checkout <another_branch>
// detached HEAD state
$ git checkout <non-existing-branch>
// jump to another commit
$ git checkout <commit-hash/branch-name/tag-name>

// remove staged file
$ git rm -r --cache <file>
// add item to .gitignore
$ echo "<file_or_folder>" >> .gitignore

// after eidting your code, just commit it with automatically stage
$ git commit -am "message"
// -a means to stage files which have been staged before, this won't stage any untracked files.


```

### Git diff
`git diff` will show changes that have not been staged, `git diff --staged` will show changes that have been staged and will be committed.

### Git log
`git log --oneline` will show each commit in oneline, which is concise.


## Questions

1. If I commit multiple time in my local repository and push to the remote repository after the last commit, will all of these commit show in the remote repository?

2. what does `checkout` mean and what that commmand does?

3. Git only suit for text file?

I don't know exactly, but I had a test with a keynote file. After I make some subtle modification on that file and then make a commit, I find the commit message shows no line insertion and deletion. Only `one file changed`. Then the storage space of the repository increases by the size of the file. Hence, I think for file other than text type, it just sotre multiple changed files, which is not the purpose git was designed for.

4. Imaging a situation where you store lots of files with git. Now you have built lots of different versions/commits. One practice you do in a daily bases is to fetch certain file of the designated version. If your version-oriented query happens very often, I suppose the repository has to checkout between different commits which will change the state of almost all files. What if each time I only want to fetch a single file and do this very frequently? Is git a good option for version control at this situation?
