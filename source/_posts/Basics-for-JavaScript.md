---
title: Basics for JavaScript
date: 2017-11-05 21:22:16
tags:
categories:
    - [JavaScript, Basics]
---

### Flow control
- normal for loop
  ```js
  // forEach is instance method, so 'Array' is just a placeholder
  Array.forEach(function(current_value, index, initial_array) {}, this_context )

  var my_array = ['a', 'b', 'c'];
   
  for (var i=0; i< my_array.length; i++) {
      console.log(my_array[i]);
      //a b c
  }

  my_array.forEach(function(current_value) {
      console.log(current_value);
      //a b c
  });
  ```
- for... in loop
  Loop through a dict-like object, the variable represents its keys.
- for... of loop
  loop through an array-like object, the variable represent its items.
- while 
  ```js
  while (funds > 1 && funds < 100) {

  }
  ```
- do...while
  ```js
  do {
    // repeating something
  } while (condition)
  ```
- switch
  ```js
  switch(expression) {
    case value1:
      // doSomething()
      break;
    case value2:
      // doSomethingElse()
      break;
  }
  ```
- others
  `break` and `continue` works in javascript as other high-level language. Be carefully when looping over an array and modifing its elements. It's much safer to do that using descending index.

### Function expression
Function expression is equal to anonymous function.

### Immediately invoked function expression (IIFE)
    
```js
(function() {
// this is the IIFE body
})();

const message = (function() {
    const secret = "I'm a secret!";
    return `The secret is ${secret.length} characters long.`;
})();
console.log(message);
```
The purpose of IIFE is to make a function can store state, just like object. The variables used to store the state are opaque out of that scope. It was used for running and return something from that closure.  
Unlike python, where we have to use `nonlocal` in order to access and modify the variables inside the outter function from the inner function, javascript has no such a restiction. You just can access and modify it inside the function as long as the function and the desired variables are in the same scope. 

Notice the difference
```js
var firstname = 'ted';

(function() {
  var firstname = 'John';
  console.log(firstname);
}());

console.log(firstname);
```



### The scope of variables in if statement

### function hositing

### Primitive types and objects
Primitive types: Number, String, Boolean, Null, Undefined, Symbol

Objects: Array, Date, RegExp, Map, Set

### Array
```js
const arr = ['a', 'b', 'c'];
arr.length;
```

### Type converting

#### convert to number
```js
// First
const numStr = '33.3';
const num = Number(numStr);
```
If `numStr` can't be converted to number, NaN will be returned.

```js
// string 'volts' will be ignored
const a = parseInt('16 volts', 10);
// result is 58
const b = parseInt('3a', 16);
// base is 10, string `kph` is ignored
const c = parseFloat('15.5 kph');
```
We can also convert a date type to time stamp
```js
const d = new Date();
const ts = d.valueOf();
```
Convert a boolean value to 1 or 0
```js
const n = bolleanValue ? 1 : 0;
```

#### convert to string
**All objects have a method `toString()`.** However, this method is not necessary for converting due to implict type conversion.  
A frequent problem is converting an object to string, which often output `[object object]`.

#### convert to boolean
```js
const n = 0;
const b1 = !!n
const b2 = Bollean(n);
```

### String method
1. split('<token>')
2. 

### subtle things
  -  `num++` is used in js, which is not available in python. The counterpart of this in python is `num += 1` 
  -  block statement is useful when combined with control flow statemnet. `while` statement can work without block statement.
  -  the difference between pre-increment operator (++num) and post-increment operator (num++) is that the return value of the former is (num+1), while the later one is (num).

### Expression and Statement(non-expression statement)
Expression resolves to a value, while statement does not.
- Assignment expression itself resolves to the assigned value.







