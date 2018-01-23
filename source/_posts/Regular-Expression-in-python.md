---
title: Regular Expression in python
date: 2018-01-02 16:19:40
tags: [RegExp]
categories:
    - [Python, Basics]
---

### Metacharacters
- backslash \
- caret ^
- Dollar sign $
- dot .
- pipe symbol |
- question mark ?
- asterisk *
- +
- ()
- []
- {}

### Character classes/sets
`[]` are used to create character sets.
range
```
/licen[cs]e/
/[a-z]/
/[0-9]/
/[0-9a-zA-Z]/
/[0-9[a-z[A-Z]]]/
```
negation of ranges
```
/[^0-9]/
```

### Predifined character classes
- `.`: match any character except newline `\n`
- `\d`: `[0-9]`, its opsite is `\D`
- `\s`: any whitespace character; `[->\t\n\r\f\v]`
- `\w`: any alphanumeric character; `[a-zA-Z0-9_]`

### Alternative
`/yes|no/` will match `yes` or `no`


### match
`*` match any character 
`a*` match a with 0 or more occurance.

### Quantifiers
- `?`: 0 or 1
- `*`: zero or more
- `+`: one or more
- {n, m}: between n and m times; {n,} >=n; {,m} <=m; {n} =n
**Notice**: quantifiers only applied to its previous token.

### greedy quantifiers
`/".+"/` match `English "Hello", spanish "Hola".` will match the whole sentence, rather than the first quote and second quote. 

In python, greedy quantifiers is applied by default. To make reluctant behavior, add extra question mark to the quantifiers.
`/".+?"/`

### Boundary character
`^`, `$`, `\b`

### Raw string
Since backslash will be treated as a special character in python literal, double baskslashes are needed if we want to express a backslash. However, with raw string, literal will be what it looks like.
```py
# without raw string
a = '\\w'
# with raw string
a = r'\w'
```

### Regular expression in python
There are two kinds of objects associated with regualr expression:
- RegexObject: a compiled regular expression
- MatchObject: the matched pattern

#### match(string, pos=0, endpos=end)
Match the compiled pattern only at the begining of the string. If we set pos, the match will begin from that position.
```py
pattern = re.compile('<html>')
pattern.match('  <html>')   # No match, becuase match starts from the begining
patterm.match('  <html>', 2) # match
re.compile('^<html>').match('  <html>', 2)  # no match, because pattern matchs from the beining






