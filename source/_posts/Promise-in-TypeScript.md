---
title: Promise in TypeScript
date: 2017-12-14 16:19:46
tags: [Promise, Async]
catetories:
    - [JavaScript, Basics]
---


### How does JS handle error in different cases

##### In synchronous programming
Just throw out an error once an exception raised. You can use `tyr/catch` statement to decide what to do when an error occured.
```js
import fs = require('fs');
function loadJSONSync(filename: string) {
    return JSON.parse(fs.readFileSync(filename));
}
console.log(loadJSONSync('good.json'));

try {
    console.log(loadJSONSync('absent.json'));
} catch (err) {
    console.log('absent.json error', err.message);
}

try {
    console.log(loadJSONSync('invalid.json'));
} catch(err) {
    console.log('Invalid.json error', err.message);
}
```

##### In asynchronous programming
JavaScript uses `callback` for asynchronous programming. An asynchronous function will call the callback function after finishing its tasks. So in order to complete an asynchronous task, we may need serveral nested callback function, in which case the code would become hard to format and read.
```js
const fs = require('fs');

function loadJSON(filename: string, cb: (error: Error, data: any) => void) {
    fs.readFile(filename, function(err, data) {
        if (err) cb(err);
        // To handle parse error
        else {
            try {
                parsed = JSON.parse(data)
            } catch(err) {
                return cb(err)
            }
            return cb(null, prased)
        }
    })
}
```
**Notice we did not call the `callback` function inside the try statement**. In conclusion, there are mainly two drawbacks of using callback function for asynchronous programming. First, it's hard to handle error, which means we have to write many boilerplate code to deal with error. Second, the code will be hard to manage. 

##### In Promise style rather than callback
```js
function readFileAsync(filename: string): Promise<any> {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, (err, data) => {
            if (err) reject(err);
            else resolve(data)
        });
    });
}

function loadJSONAsync(filename: string): Promise<any> {
    // Here we know the chained Promise object returns a Promise object
    return readFileAsync(filename)
                .then((res) => {
                    return JSON.parse(res)
                })
}
```
Thus, Promise are a far cleaner solution to write asynchronous code than callbacks. At the same time, the resulting code is easier to read. With the catch handler it also gives us a single place wehre we can handle errors.



### Why Promise?
If we are going to use Promise, a new object, we have to be clear about what problems it solves and the advantages of using it. Imagine a scenario where you need to read three file and calculate their total size. Traditionally, we would finish this task with callbacks.
```js

```

### How to use promise?
```js
// create a Promise to chain
const p = new Promise((resolve, reject) => {
    if (false) {
        // resolve is similar to return, while resolve also represents success
        resolve("something");
    } else {
        reject("Error message")
    }
});
// A simpler way to create a Promise
const p = Promise.resolve("something")

// Or create a function which returns a Promise
function IReturnAPromise(param: string): Promise<any> {
    return Promise.solve()
}
```
To chain a promise
```js
p.then((res) => {
    // Here we can return another promise
    return Promise.resolve(123)
}).then((res) => {
    console.log(res); // this will output 123, not the Promise object itself.
})

p.then((res) => {
    // we can also just return a value
    return 123
}).then((res) => {
    console.log(res); // this will output 123
})
```
some tips:
- `catch` statement does **not** have to be in the tailing postion.
- any synchronous erros thrown in a `then` or `catch` result in the returned promise to fail.
- only the nearest `catch` is called for a given error (as the catch starts a new promise chain).
- a `Promise` being chained with `then` or `catch` will return a new Promise.
- no matter one `then` or `catch` statement returns a value/Promise object or not, chains after that will get executed.


### Any other benefits from using Promise?
We have used `Promise` to simplify the implementation of async tasks, but can we extract more from it? Image that you need to calculate the size of three file on the disk. Using promise, we can read each file to get its size by chaining these procedures. However, given the long waiting time for I/O, we can save some time if we could do them simultanously. In that case, we can use `Promise.all()` to run these tasks at the same time. 
```js
let item1, item2;
Promise.all([asyncTask(1), asyncTask(2)])
    .then((res) => {
        [item1, item2] = res;
        console.log('done');
    })
```

### Promise with async/await
```js
function delay(milliseconds: number, count: number): Promise<number> {
    return new Promise<number>(resolve => {
            setTimeout(() => {
                resolve(count);
                }, milliseconds);
        });
}

async function dramaticWelcome(): Promise<void> {
    console.log('Hello');

    for (let i=0; i < 5, i++) {
        // Await is converting Promise<number> into number
        const count: number = await delay(500, i);
        console.log(count);
    }
    console.log("world!");
}

dramaticWelcome();
```


### Example code

```js
"use strict"
let performUpload = function(imgStatus: string): Promise<{imgStatus: string}> {
    return new Promise((resolve) => {
        console.log(`Status: ${imgStatus}`);
        setTimeout(() => {
            resolve({ imgStatus: imgStatus });
        }, 1000);
    });
}

var upload;
var compress;
var transfer;

performUpload('uploading...')
    .then((res) => {
        upload = res;
        return performUpload('compressing...'); 
    })
    .then((res) => {
        compress = res;
        return performUpload('transfering....');
    })
    .then((res) => {
        transfer = res;
        return performUpload('uploaded successfully')
    })
```


### FAQ
1. 'Promise' only refers to a type, but is being used as a value here?
    `npm i --save-dev  @types/es6-promise`
2. 
