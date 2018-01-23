---
title: JavaScript Standards and Common Confusion
date: 2017-12-14 21:04:23
tags:
categories:
    - [JavaScript, Basics]
---

### Strict mode

Modifing an object is not allow in strict mode. For example:
```js
arguments = {}
// raise Exception
arguments.size = 10
```

### ES6 syntax

- `let` is new in ES6, prior to which the only avariable keyword is `var`. Let specifically declares a variable and you can only do it once.
```js
let targetTempC, room1 = "conference_room_a", room2 = "lobby";
```
- block is the scope between two curly brace. It defines the scope of variables defined inside the block. Although it's often a part of a control flow statement, it can also be standalone. `{ // block }`


### Common Confusion
1. Can function modified the passed-in arguments?
    Yes, both javascript and python will do that if the arguments are reference type.
2. How to pass data from the server to front-end? 
3. Differences between keyword 'let' and 'var'?
    When you declare a variable with `let`, it dosen't spring into existence until you declare it. While declared with `var`, it's available everywhere in the current scope, even before it's declared(a mechanism called hoisting). This seneario is like function declaration. When you defined a function, you calling code could be ahead of this definition (In python it's different, which mean you have to call a function after you defined it).   

    Another aspect of variables declared with var is that JavaScript doesn’t care if you repeat the definition, while you can't redeclare a variable which have beeb defined with `let`.

    Also notice, in `for` loop, if you defined a new variable with var, that variable will be available in the same scope where the for loop in. But if that variable is defined with let, that variable will be cleared when the for loop cycle ends.
    ```js
    for (let i=0; i < 5; i++) {
        console.log(i)
    }
    console.log(i)  // Here an error will be raised
    ```
    Another example to demostrate the difference between `var` and `let`
    ```js
    let name = 'ted';

    if (true) {
        let name = 'cheng'
    }
    console.log(name)   // This will output ted, becuase cheng only affect the if block.
    ```
    IF we leave out `let` keyword inside the if block, the output should be 'ted'. It does make sense.
    ```js
    var varDeclaredVarialbe = "outside";

    if (true) {
        var varDeclaredVarialbe = "inside";
    }

    console.log(varDeclaredVarialbe); // This will output inside
    ```

    ```
    // declare multiple variables in the same time
    let targetTempC, room1 = "conference_room_a", room2 = "lobby";
    ```
    So your rule of thumb should be to use a constant; if you find you have a legitimate need to change the value of the constant, you can always change it to a variable.
4. The difference between anonymous function and arrow function?
    They are almost the same, except for the meaning of keyword `this` in their function body. In anonymous function, this refers to the object created by this function, while in arrow function it refers to the outter class or function.

