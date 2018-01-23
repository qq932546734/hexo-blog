---
title: Typescript
date: 2017-12-05 12:59:26
tags: [ts, js]
categories:
    - [JavaScript, TypeScript]
---

### Before starting
1. install typescript package
```shellsession
// To make it accessible from anywhere
$ npm install -g typescript tslint
```
2. prepare your code
3. transpile the code to javascript file
```shellsession
$ tsc main.ts
```
This will produce a js file with the same name. If any error detected, the transcompiler will prompt us the error and still produce a js file.  

To smooth our development procedure, we want the ts file to be transpiled each time we save it. To do so, we can make tsc working in a watch mode: `tsc main.ts -w`. To make the js file compatible with ES5, `tsc main.ts --target ES5`.


### Type annotation
A super set of javascript. 
- Strong typing
- OO features
- Compile-time errors
- Great tooling

### Restrains
1. type restriction
```js
// Declare variable without assignment, it default to be type `any`
let a;
// Deaclare variable by assigning value, its type is restricted to be that value's type
let a = 1;
// Declare with explict type
let a: number;
let b: boolean;
let c: string;
let d: any;
// Type Array
let e: number[] = [1, 2, 3];
let f: any[] = [1, true, 'a', false];
// Another to declare an array
let stringArray: Array<string>;
let numArray: Array<number>;
// Other types include Void, Null, Tuple, Enum, Generics, undefined
let strNumTuple: [string, number];

// Without explictly assginment, items of the enum will implictly get 0, 1, 2 ....
enum Color {Red, Green, Blue};
// The best practice is to assign them explictly
enum Color { Red=0, Green=1, Blue=2}
let backgroundColor = Color.Blue;

// Type Assertion: 
let message;
message = 'abc';
// Although We assgined a string to message, message's type is still any.
// The first way of type assertion
(<string>message).endsWith('c');
// The second way of type assertion
(message as string).endWith('c');

// Type restrain can also be used for return value.
function getSum(num1: number, num2: number): number {
    // Here has to return a number value
    return num1 + num2
}

let mySum = function(num1: number): number {
    return num1 + 1
}

// optional arugments also work on function
function anotheSum(num1: number, num2?: number) {
    return num1 + num2
}
```
2. inline annotation
```js
let drawPoint = (point: {x: number, y: number}) => {
    console.log(point.x);
}
```
3. interface
```js
interface Point {
    x: number,
    y: number
}

let drawPoint = (point: Point) => {
    console.log(point.x)
}

drawPoint({x: 1, y: 2})
```
4. Generics
```js
function GetType<T>(val: T): string {
    return typeof(val);
}

let aStr = "a string";
let aNum = 10;
GetType(aStr);
GetType(aNum);
```


__Notice__: Interface is used for declaration, while no implementation. Class is used for implementation.

### Arrow functions
A cleaner way to declare function
```
let someFn = (message) => {
    console.log(message)
}
// If the function body only contains oneline code, the curly braces can be omitted
let someFn = (message) => console.log(message)
```


### Classes
```js
class Point {
    x: number;
    y: number;

    // Only one constructor for each class
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }

    // Just for demostration of option arguments
    constructor(x?: number, y: number) {
        this.x = x;
        this.y = y;
    }

    draw() {
        console.log(this.x)
    }

    getDistance(another: Point) {

    }
}

let point = new Point(1, 2);
point.draw();
```


### Inheritance
```js
class User {
    name: string;
    email: string;
    age: number;

    constructor(name:string, email: string, age: number) {
        this.name = name;
        this.email = email;
        this.age = age;
        console.log('User created: ' + this.name)
    }
}

class Member extend User {
    id: number;

    constructor(name:string, eamil: string, age: number) {
        super(name, email, age);
        this.id = random_id();
    }
}
```
`instanceof` are used to determine the inheritance relationship between two object. 

### Access modifier
To avoid arbitrary modification of properties after initialization, we should use access modifier to restrain that from happening.
```js
let point = new Point(1, 2);
// This should be prevented.
point.x = 3;
```
There are three access modifier, `public`, `private`, `protectedk`. Without access modifier, attributes and methods default to be public. 
```js
class Point {
    private x: number;
    private y: number;
    constructor(private x?: number, private y?) {
        this.x = x;
        this.y = y;
    }
}
```
A more concise version
```js
class Point {
    constructor(public x?:number, private y?: number){}
}
```


### Properties
After we declared some properties as private property, what if we want to access it or set it at some late time? Well, there are two solutions. The first one is to create new methods to accomplish that.
```js
class Point {
    private x: number;
    private y: number;
    // the name of this method depends on you
    setXProperty(value:number){
        this.x = value;
    }
    getX(){
        return this.x;
    }
}
```
A more concise way to do so:
```js
class Point {
    //....
    get x() {
        // of course, you can modify it and then return or you can return anything you want
        return this.x
    }

    set x(value: number) {
        if (value < 0) {
            throw new Error('Value cannot be less than 0.');
        }
        this.x = value;
    }

}
```
Notice that the name for set and get can not be the same with attributes name. The common solution for that is setting attributes name with underscore, making them only accessible inside the class declaration. Then we can use the normal lower case name for set and get method. 
```js
class Point {
    constructor(private _x?: number, private _y?: number){}

    get x() {
        return this._x
    }

    set x(value: number) {
        this._x = value
    }
}
```

### Interfaces combined with classes
Although this is not mandatory, we can use interface for class implementation to make the class's interface more obvious to see.
```js
interface UserInterface {
    name: string;
    email: string;
    age: number;
    register();
    payInvoice();
}

class User implements UserInterface {
    name: string;
    email: string;
    age: number;

    constructor(name: string, emial: string, age: number) {
        //...
    }

    register() {
        //...
    }

    pyInvoice() {
        //...
    }
}
```

### Modules
Each ts file is treated as a module. 
```js
export class Point {

}
```
To import these types or variables from other file:
```js
// No need to add `.ts` extension in the path 
import {Point, AnotherClass} from './point';
```
If there are many modules and you don't want to import modules one by one to import all wanted variables/types, you can put these modules in a folder and create a `index.ts` file inside to folder to import all of these variables, thus you can just import variable from the folder.
```
- working.ts
- package
----index.ts
----firstModule.ts
----secondModuel.ts
----thirdModule.ts
```

```js index.ts
import * from './firstModule';
import * from './secondModule';
import * from './thirdModule'
```

```js working.ts
import {a, b, c} from './package'
```

### To be explored
1. Does propotypes exists in typescript?
2. We can use `...arr` like `*args` in python.

### Debugging 
1. When with only oneline in ts file, it will prompt the error: `Cannot redeclare block-scoped variable`. To solve this, add one line at the outmost scope: `export {}` if there is nothing to export for that module.









