---
title: Vim cheatsheet
date: 2017-11-22 20:00:52
tags:
---


### find your true vim
```
$ which vim
// if it's linked program, to find the original one
$ readlink -f /usr/bin/vim
```

### Basics

> If you start vim without a filename, or if the file doesn't exist, vim opens a 
new buffer area for editing. If you specify an existing file on the command line, 
vim reads the entire file's content into a buffer area, where it is ready for 
editing.

- pageDown (Control+F): move forward one screen of data
- pageUp (Control+B): move backward one screen of data
- G: move to the last line in the buffer
- _num_ G: move to line number _num_
- gg: move to the first line in the buffer

### command line mode

In normal mode, enter colon to switch to command line mode.

- `q`: quit if no changes have been made to the buffer data
- `q!`: quit and force to discard any changes have been made
- `w` _<filename>_: save the buffer data under a different filename
- `wq`: save the file and quit

### INSERT

- `i`: insert text at cursor; `I`: insert text at start of line
- `a`: append text after cursor; `A`: append text after end of line
- `o`: open new line below; `O`: open new line above

### DELETE
- `dd`: whole line; `D`: delete to the end of the line; `dw`: delete word
- `x`: delete character
- `d` + `arrow`: delete in that direction

### CHANGE
- `cw`: change word
- `r`: replace single character
- `C`: change the whole line (delete the whole line and make edition)

### NAVIGATE

- "w/b/e": go to the next word(words are separated by punctuation)
- "W/B/E": go to the next word(words are recognized by space)
- `0`: start of line; `^`: first non-whitespace
- `$`: end of line
- `gg`: start of file; `G`: end of file

### EXIT
`ZZ`: equal to `:wq`
`ls`: list all opened buffer
`ctrl+r`: redo
`u`: undo






### In normal mode
Delete related
- `x`: delete the character at the current cursor position
- `dd`: delete the line at the current cursor position
- `dw`: delete the word at the current cursor position
- `d$`: delete to the end of the line from the current cursor position

- `J`: join the current line and the line after the current line
- `u`: undo the previous edit command
- `a`: append data after the current cursor position
- `A`: append data to the end of the line at the current cursor position
- `r` _char_: replace a single character at the current cursor position with char
- `R` _text_: overwrtes the data at the current cursor position with text, until you press escape

Note: some of these commands allow you to use a numeric modifier to indicate how many times to perform the command.

### copy and paste

Actually, there are two situations for this function in real life practice. The first one is you removed a piece of text and then you can paste it somewhere else, such as deleting a line or a word. The second one is you copy from a piece of text from the buffer and paste it somewhere else. In vim, copy is called 'yank', so the key `y` is used to copy things. You can use `yw`, `y$`, `yd`

Paste is relatively easy. The command p inserts the text after the current cursor position or after the current line.

### search and substitute

`/` search forward; `?` search backward

In normal mode, enter slash, then type what you want to search. If not found, red error message will appear in the bottom. If found, cursor will move to the first match after the current curson position. To continue search, use `n` command for next match, or enter slash and then press enter. Of course, the first approach is recommended.

Compared with searching, command used for substitution is a little more complex. First, you must enter into command line mode (by entering colon). The basic systax is `:s/<old-text>/<new-text>`
1. replace all occurance in the current line: `:s/<old-text>/<new-text>/g`
2. replace all occurance between line _n_ to line _m_: `:n,ms/<old-text>/<new-text>/g`
3. replace all occurance in the entire file: `:%s/<old-text>/<new-text>/g`
4. like 3, but prompt for each occurance: `:%s/<old-text>/<new-text>/gc`

### Open multiple files and navigate between them
- `tabe <filepath>`: open a file
- `tabn/gt`: the next file
- `tabp/gT`: the previous file



Or work in a splitted window:
`:sp <filepath>`, then switch working window with `Ctrl+w`(maybe we need to repeat this command to make it work).

### Settings in '.vimrc'
```
set number
syntax on

filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" When identing with '>', use 4 space width
set autoindent
" On pressing tab, insert 4 spaces
set shiftwidth=4
set expandtab
```
NOTE: a line start with double quote is a comment;


### practice
- delete all line in a file: `gg` to the first line, `dG` delete all lines;
- `:w <newname>` works as "save as"
-




