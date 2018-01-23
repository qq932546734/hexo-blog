---
title: Shell Related
date: 2017-11-09 15:40:18
tags:
---
# Shell on MacOS

### How to find which shell are you using?
```
$ finger `whoami` // whoami as a command will show the current user
$ echo $SHELL   //the user's preferred shell, not necessairly the current running shell.
$ echo $0   // The running shell
```

### The difference between login shell and non-login shell

### Which setting files will be loaded when starting a shell program?
profile/env file and rv file (runtime configuration)
#### login shell
`/etc/profile`, `~/bash_profile`, `~/.bash_login`, `~/.profile`
#### non-login shell / non-interactive shell
`~/.bashrc`
> Non-login shells read ~/.bashrc, and non-interactive shells try not to read any files. This is essential because, when running autonomously, a shell's standard streams might be redirected, and aliases or environment variables could confound running scripts. [link](https://coderwall.com/p/u003pa/bash-startup-scripts-on-linux-and-mac-os-x)


# Shell On Linux

> On Linux, by default bash does not load .bash_profile for an interactive session, but it does for a login shell.
> 


### Why there are several virtual console opened when Linux starts?
> A virtual console is a shell prompt in a non-graphical environment, accessed from the physical machine, not remotely. A virtual console is a terminal session that runs in Linux system memory. Multiple virtual consoles can be accessed simultaneously. A graphic terminal is a terminal enumtor. You can think of graphical terminal emulators as CLI terminals 'in the GUI' and virtual console terminals as CLI terminals 'outside the GUI'. To switch to virtual consoles, use keyboard combination `Ctrl+Alt` and function key (F1 through F7). Each virtual consle gets a name, tty(teletypewriter) and its number. There are a bunch of Graphical Terminal Emulation available for linux, such as GNOME Terminal, Konsole Terminal and xterm.

### The components of graphical interface elements
- Client: the application which requires graphical servcies
- Display Server: managing the display and then input devices such as keyboard and mouse.
- Window Manager: adding borders to window and providing featuers to move and manage winodws
- Widgets Library: adding menus and appearance items desktop environment clients

### Man page section areas
1. Executable programs or shell commands
2. System calls
3. Library calls
4. Special files
5. File formats and conventions
6. Games
7. Overviews, conventions and miscellaneous
8. Super user and system administration commands
9. Kernal routines


### Tips
1. `Ctrl+Shift+C` and `Ctrl+Shift+V` are used for copy and paste in GNOME Terminal, respectively;
2. To zoom in and zoom out in terminal, press `Ctrl`/`Command` then click `-` or `+`;
3. `ctrl+F` page up, `Ctrl+B` page down; `j` line down, `k` line up.
4. use `man -k <keyword>` to search for the command if you can remember its whole name
5. 












