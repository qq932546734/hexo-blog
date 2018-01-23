---
title: JavaScript Best Practice
date: 2017-12-14 21:16:55
tags:
categories:
    - [JavaScript, Basics]
---


### A good practice of function definition

```js
let globalFunc; 
{
    let blockVar = 'a'; 
    globalFunc = function() {
        console.log(blockVar);
    }
}
globalFunc();
```
