---
title: Using Dexie manipulating IndexedDB
date: 2017-12-12 12:33:57
tags:
categories:
    - [JavaScript, Node]
    - [JavaScript, Basics]
---

### What's Dexie?
It a wrapper for IndexedDB, which is a javascript-based database used in client side.

### A simple example code
```js
import Dexie from 'dexie';

// The argument is the name for your db
var db = new Dexie("MyDatebase")
// Define your schema
db.version(1).stores({
    table1: 'PrimaryKey, index1, index2, ...',
    table2: 'PrimaryKey, index1, index2, ...',
    friends: "++id, name, isCloseFriend",
    pets: "++id, name, kind"
})

// Open the database. If you skip this step, db will be automatically opened.
db.open().catch(function(e) {
    console.error('Open failed: ' + e);
})
db.friends.add({name: "ted", isCloseFriend: 0});
// I am not sure why `fur` can be added as a variable in this table, but it does work
db.pets.add({name: "teddy", kind: 'cat', fur: "Too long right now"})
```

### Database versioning
Why is there database versioning in indexedDB while none in database like MySQL? Well, that's because indexedDB is a client side db, while MySQL is server-based. In the server, when you update your database schema, data get updated at the same time. This is different in client side like browser, data is stored and unable to be changed when you code to change db schema. So in this situation multiple db schema versions are required to coexist.

So, when you want to change schmea of pre-defined tables, you have to keep the original schema and add a new version to change schema.
```js
var db = new Dexie('DB')
db.version(1).stores({friends: "++id, name"});
db.version(2).stores({friends: "++id, name, shoeSize"})

var newDb = new Dexie('NewDB')
newDB.version(1).store({
    foo1: 'id, x, y, z',
    foo2: 'id, x, y, z',
    foo3: 'id, x, y, z'
})
// To update schema, just specify an updated version fo the corresponding table
newDB.version(2).store({
    foo1: 'id, x,y'
})
// So in the second version, one table `foo1` get updated by excluding `z` property. The rest reamins the same.

```

### Transaction
```js
db.transaction('rw', db.friends, db.pets, async ()=>{
    // Transaction Scope
    const friend = await db.friends.get({name: "David"});
    ++friend.age;
    await db.friends.put(friend);

}).then(() => {
    // Transaction Complete
    console.log("Transaction committed");

}).catch(err => {
    // Transaction Failed
    console.error(err.stack);
});
```

### Indexing
All variables added through `stores({})` will be indexed. You can also add other variables/properties that are not defined in the schema when you add data to the database. The difference is that properties not appearing in schema will not get indexed.
```js
// `name`, `id` will be indexed
db.version(1).stores({friends: "++id, name, age"})
// `phone`, `email` won't be indexed
db.friends.put({
    name: "ted",
    age: 20,
    phone: "110",
    email: "932546734@qq.com",
})

```


