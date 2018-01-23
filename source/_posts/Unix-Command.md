---
title: Unix Command
date: 2017-11-05 11:47:35
tags:
---

curl

last: show the login history of users.

kill

ps

grep

tail

# Commands used for server Profiling

    ### netstat

    ### iostat

    ### mpstat
```
// print out PATH environment variables
$ SHELL -l -c 'echo $PATH | tr : "\n"'
```
# Daily-using command

- `cd -`: change to the previous working directory; `cd --` working directory piror to previous one

## ps

- `-e`: show all processes, idential to `-A`
- `-f`: display a full format listing

#### Meaning of each column
* UID: User who is responsible for launching the process
* PID: process ID
* PPID: its parent process ID
* C: Core/processor utilization during the lifetime of the process
* STIME: The system time when the process started
* TTY: the terminal device from which the process was launched
* TIME: the cumulative CPU time required to run the process
* CMD: name of the program that was started


## Vim

- <kbd>Ctrl</kbd>+<kbd>F</kbd>: PageDown
- <kbd>Ctrl</kbd>+<kbd>B</kbd>: PageUp
- <kbd>G</kbd>: move to the last line in the buffer
- gg: move to the first line in the buffer
- _num_+<kbd>G</kbd>: go to line _num_


“q to quit if no changes have been made to the buffer data
q! to quit and discard any changes made to the buffer data
w filename to save the file under a different filename
wq to save the buffer data to the file and quit”


### How to transfer files between computers?
1. setp one: use `tar -cf <name.tar> <fileOrDir1> <fileOrDir2>` to archive the target files
2. setp two: use `scp` to copy them.




