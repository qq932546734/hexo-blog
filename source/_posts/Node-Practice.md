---
title: Node Practice
date: 2017-12-12 09:21:32
tags:
categories:
    - [JavaScript, Node]
---

### How to use event emitter
In node with javascript
```js
const EventEmitter = require('Events');
const myEmitter = new EventEmitter();
// Each time a new `listener` being added will trigger a `newListener` event
myEmitter.once('newListener', (event, listener) => {
    if (event == 'my-event') {
        myEmitter.on('my-event', () => {
            console.log('A')
        });
    }
})
// the first argument is the event name, the second is a function, whose argument is the event's argument.
myEmitter.on('my-event', (arg) => {
    console.log('B');
    console.log(arg)
});

// first parameter represents the event name, the second object will be pass as an argument to this event's listener.
myEmitter.emit('my-event', {name: 'TED', age: 20})
```

### Dive into event emitter
A simplified version:
```js
function Emitter() {
    this.events = {};
}

Emitter.prototype.on = function(type, listener) {
    this.events[type] = this.events[type] || [];
    this.events[type].push(listener);
}

Emitter.prototype.on = function(type) {
    if (this.events[type]) {
        this.events[type].forEach(function(listener) {
            listener();
        });
    }
}
```
