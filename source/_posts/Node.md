---
title: Node
date: 2017-11-08 21:10:08
tags:
categories:
    - [JavaScript, Node]
---
### Configuration of Env
```
$ npm init
```
You will be asked about a lot of question, type whatever you want or press Enter to accept the default setting. This will crate a `package.json` file and a directory named `node_modules`. The function of `package.json` is to keep track of what you have installed and their version. You can run `npm install` (current working directory should be where `package.json` resides) to update or repair you node modules.
```
$ npm install
```
build tools: Gulp and grunt
```
$ npm install -g gulp
```
to get a local Gulp for each project, run this in project root 
```
$ npm install --save-dev gulp
```

// install babel
```
$ npm install --save-dev babel-preset-es2015
$ npm install --save-dev babel-core
$ npm install --save-dev gulp-babel
```

```javascript
// gulpfile.js
const gulp = require('gulp')
const babel = require('gulp-babel')

gulp.task('default', function() {
    // this will match all js file in folder es6 and in its subdirectory
    gulp.src("es6/**/*.js")
        .pipe(babel())
        .pipe(gulp.dest("dist"));

    gulp.src("public/es6/**/*.js")
        .pipe(babel())
        .pipe(gulp.dest("public/dist"));
    });
```



wirte you code in the corresponding folders then run `gulp`, it will transcompile your source code and convert it to ES5 at the same time. To run them, `node <transcompiled_file>`


### Linting

```
$ npm install -g eslint
//create a configuration file named `.eslintrc` for this project
$ eslint --init
// the above command will create a configuration file for you in the root of your project
```

## Objects in Node

### global

`global` object exsit both in browser and Node, although there are some major differences between them. In the browser when you declare a varaible at the top-level, it becomes global. This is not true in Node.

### Buffer
In node, I/O was handle in Buffer. You can create a Buffer object like this
```
let buf = new Buffer(24);
buf.fill(0);    // To initialize the object
```
Or create it from a string object
```
let str = 'New string';
let buf = new Buffer(str);
```


### Timer
There are two timer we can use: `setTimeout(fn, timelapse, args)` and `setInterval(fn, timelapse, args)`. In order to stop them, use `clearInterval(interval_return)` and `clearTimeout(timeout_return)` respectively. After setting timer, the programing will keep running, waiting for the timer to fire. `timer.unref()` is used for cutting the reference to timer, which means the timer will not keep the programming alive. The timer is still alive as long as the program does not exit. 

### Exports
There are three types of module pattern we can use in node.
```js
module.exports = obj
```
or 
```js
exports.name = 'ted'
```
or 
```js
function Fn() {
    this.greeting = "Hello World!!!";
    this.greet = function() {
        console.log(this.greeting);
    }
}

module.exports = new Fn();
// Also, we can export the Fn itself
module.exports = Fn;
```

**Revealing Module Pattern:** Exposing only the properties and methods you want via an returned object.
**Difference between `exports` and `module.exports`**: they both reference to the same object, so in most case they are equal in usage. But when we assigned another object to one of them, this connection will be broken. Thus, if we only mutate one of them, they are still equal. However, the safest way to hanle this is only using `moduel.exports`

### Modules
Although there is no package in javascript, it works as package in python. To have a 'package', you group your modules in a directory and expose these modules's API inside the `index.js` file. Then when requiring the folder name -- the packag name, you will get these APIs.

### Inheritance 
Inheritance in JavaScript is achieved by prototype through `function constructors` (a normal function that is used to construct objects) before ES6.
With ES6, `class` will do the trick.

In function constructor, `this` variable points a new **empty object** and that object is returned from the function automatically.
```js
function Person(firstname, lastname) {
    this.lastname = lastname;
    this.firstname = lastname;
}

Person.prototype.greet = function() {
    console.log('Hello' + this.frstname + " " + this.lastname);
}

var Ted = new Person('Guohua', 'Cheng');

// we can access its prototype 
console.log(Ted.__proto__)
```

### Require a json file
We can directly require/import a json file as we do with modules, and the json content will be converted to an object which will be aviable for you. 

### Tips
- In ES6, a new syntax with the same functionality as `require` is introduced: `import * as some from 'greet'`.









