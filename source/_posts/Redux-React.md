---
title: Redux & React
date: 2018-01-16 23:18:46
tags:
categories:
    - [JavaScript, React]
---

### Redux
In redux, each reducer accept two parameters -- a current state and an action object. `action` should be pure function, which means it should not mutate the current state, instead, the new state is supposed to be calculated based on the current state but not modify it with any side effects. Thus, if the state is an array, when we want to add an item to the current state, we should use `currentState.put(newItem)`, what we should do is:
```js
return currentState.concat(newItem)
// or
return [...currentState, newItem]
// Almost most the same, if we want to remove an item, we should avoid:
return currentState.splice(index, 1)
// Instead
return currentState.slice(0, index).concat(currentState.slice(index + 1))
```

Just as the same priciple, when we want to change one attribute of an object, we don't change the object directly. Instead, we create a new object with the same attributes expect the one we want to modify.
```js
currentToDo = {
    id: 0,
    text: "this is great",
    completed: false
}

// reducer: change this to-do as completed
function(currentToDo, action) {
    return {
        id: currentToDo.id,
        text: currentToDo.text,
        completed: !currentToDo.completed
    }
}
// And in ES6, there is a more convenient way to do so
function(currentToDo, action) {
    return Object.assign({}, currentToDo, {
        completed: !currentToDo.completed
    })
}
// OR
return {...currentToDo, {}}
```
