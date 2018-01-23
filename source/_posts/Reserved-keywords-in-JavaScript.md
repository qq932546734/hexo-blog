---
title: Reserved keywords in JavaScript
date: 2017-12-06 10:47:06
tags:
categories:
    - [JavaScript, Basics]
---

You may have noticed that types in javascript can be very confusing. For example
```js
a = 1
typeof(a) === 'number'
```
The variable `a` is type number, while `number` itself is not a reserved keywords in javascript. To create a number type in class,
```js
a = new Number('2')
```
The reason for this is that there are two kinds of type in javascript: primary and reference type. To make using primary type more convient, javascript did some special thing to make primary types act as object.
- number => Number
- boolean => Boolean
- string => String
- null, undefined, Symbol

So, I concluded that primary type's type name is not reserved keywrod, while their object wrapper names are reserved keywords.

### Keywords
|        |       |   |   |
|:---------|:--------|:----------|:-----|
|break     | do       |instanceof  | typeof|
|case      | else     | new        | var|
|catch     |finally   |return      | void|
|continue  |for       |switch      | while|
|debugger  |function  |this        | with|
|default   |if        |throw       | null|
|delete    |in        |try         | true|
|false|

### Future Reserved Words
|    |       |   |   |
|:---------|:--------|:----------|:-----|
|abstract  |export      |interface  |static|
|boolean   |extends     |long       |super|
|byte      |final       |native     |synchronized|
|char      |float       |package    |throws|
|class     |goto        |private    |transient|
|const     |implements  |protected  |volatile|
|double    |import      |public     | 
|enum      |int         |short      |
## To Explore
1. Usage of `Symbol`