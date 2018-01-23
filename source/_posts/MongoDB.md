---
title: MongoDB
date: 2017-11-06 16:57:46
tags:
categories:
---

table->collection; rows->documents;columns->fields;

# Installation 
* on Ubuntu: [official website](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-the-latest-stable-version-of-mongodb)

### Something we need to know for debug

#### Configuration file

Usually, the configuration file is `/etc/mongod.conf`, where you can set where to store your mongo data and where to record the log. The MongoDB instance stores its data files in `/var/lib/mongodb` and its log files in `/var/log/mongodb` by default, and runs using the mongodb user account.

#### service file in Linux
Following the offical tutorial to install MongoDB, you will get a service which you can use to start mongod. The service file is at `/lib/systemd/system/mongod.service`. The service defines which user to start mongod, you can also change it to decide which configuration file to load when start mongod.

#### To change configuration
If you want to change the location of database and/or log file, first you need to make sure that the user `mongodb` has access to that folder or file. To change the owner of folders or files:
```
sudo chown mongodb:mongodb <path_or_file>
```


# Uninstall
There are several files you need to remove:
1. the configuration file, usually located in `/etc/mongod.conf`;
2. the service file if that has been changed, located in `/lib/systemd/system/mongod.service`;
3. After removing those file and reinstall MongoDB, you may found `sudo service mongod start` doesn't work. It reports that `Units.mongod.service not found`. Don't worry, just type in `sudo systemctl enable mongod` and run it. Then you will find it works fine. 


# Make mongodb accessbile remotely

By default, mongodb is restricted only to be accessed locally and thus the authorization is not set. If we want to access it remotely, we should the following things:
1. disconnect the bind to `localhost` in */etc/mongod.conf* by commenting `bindIP: 127.0.0.1`;
2. Enable authrization in Security setting by adding `authrization: enabled` under the security setting;
3. create a user for you database in mongodb shell, you can do it either locally or by logging the server remotely through `ssh` **I am confused by the account system of MongoDB, need to learn more about it**
```
> use <database_name>
> db.createUser({
    user: 'ted', 
    pwd:'pwd', 
    roles: [{role: 'readWrite', db: '<database_name>'}]})
> use test
> db.createUser(
    {
      user: "tester",
      pwd: "password",
      roles: [
         { role: "read", db: "test1" },
         { role: "read", db: "test2" },
         { role: "read", db: "test3" },
         { role: "readWrite", db: "test" }
      ]
    });
```
4. Restart mongodb by `sudo service mongod restart`. Make sure the port used by mongodb is not restricted in accssibility in your server settings.
5. Now you can use it either by mongodb shell remotely or in you python program through pymongo.
`mongo -u ted -p pwd 172.16.160.203/<database_name>`
```
from pymongo import MongoClient
c = MongoClient('mongdb://ted:pwd@172.16.160.203/<database_name>')
db = c.<database_name>

```

```
// start mongodb server
$ mongod
// enter mongo shell client
$ mongo
// import data in json file to the database
$ mongoimport --db test --collection restaurants --drop --file ~/downloads/primer-dataset.json
// To remove a collection from a database; if succeed, true will be returned
> use <db_name>
> <db_name>.<col_name>.drop()

```
As far as I know, there is no way to explictly create a database. You can just `use <new_database_name>` and then insert one document into a collection in that database. The new database will be created. Stilling looking for a more 'normal' way to do so.
## Mongo Shell
```
> help 
> create d
> use test_db
// Here db represents the current database, namely test_db
> db.restaurants.find()
// `it` represent the last query result, for further reference
> it 
> db.restaurants.find({a: 1})
> db.restaurants.insert({"address": "Londen", "name": "Ted"})
> db.restaurants.find( { "borough": "Manhattan" } )
// Query by a field in a embedded document
> db.restaurants.find( { "address.zipcode": "10075" } )
```

## Query with conditions
`{ <field1>: { <operator1>: <value1> } }`

```
// greater than
> db.restaurants.find({"grades.score": {$gt: 30 }})
> db.restaurants.find({"grades.score": {$lt: 10 }})
// Logical and & or
> db.restaurants.find({ $or: [{'borough': 'brooklyn'}, {'address.building': '1007'}]aa

// sort the query result
> db.restaurants.find().sort( { "borough": 1, "address.zipcode": 1 } )
```





## How to add index in mongoDB? Are there any requirements in terms of the type of the field?


## Sharding in mongodb

Before we dive into sharding, let's have a look at horizontal scaling and verticle scaling.

Horizontal scaling means that you scale by adding more machines into your pool of resources whereas Vertical scaling means that you scale by adding more power (CPU, RAM) to an existing machine.











