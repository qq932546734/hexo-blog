---
title: MySQL Learning
date: 2017-12-30 23:56:51
tags:
categories:
    - [Database, MySQL]
---

### Encoding
> PROBLEM: Using the standard way to install mysql, mysql will be set as using `latin1` as the default encoding. Then we I use Django ORM to deal with mysql and create database and tables, the newly created database and tables also use encoding `latin1`. To solve this problem, just create the database manually with the desired unicode encoding system. Then tables will also use that encoding.
Encdoing can be different for databases, tables and cloumns.
- database encoding:
    + `use <dbname>; show variables like "character_set_database";`
- table encoding:
    + `SHOW TABLE STATUS where name like 'article';`
    + `show table status from <dbname>;`
- column encoding:
    + `SHOW FULL COLUMNS FROM <tablename>;`

### Types supported in mysql
datetime: `select * from web_blogarticle where CreateTime >= DATE_SUB(NOW(),INTERVAL 1 YEAR);`


### mysql shell
```shell
mysql> show databases;
mysql> use <databasename>;
mysql> show tables;
mysql> describe <tablename>;
mysql> desc <tablename>;
mysql> drop table <tablename>;
mysql> show engins;
mysql> show table status;
mysql> set default_storage_engine=INNODB;
mysql> create database <dbname>;
mysql> create table <tbname> (<first_col> <type>, <second_col> <type>);
mysql> ALTER TABLE <tbname> ADD <colname> <datatype>;
mysql> ALTER TABLE <tbname> DROP COLUMN <colname>;
# show the create sql syntax for an existing table.
mysql> SHOW CREATE TABLE <tbname>;
# Change an existing column to be unique
mysql> ALTER TABLE <tbname> ADD UNIQUE (<colname>);
# Create an index for certain column
mysql> CREATE IDEX <indexname> ON <tbname> (<colname>);
```

### CRUD
create table <tablename> (id int)


### Primary key
Although we can set any type as primary key, it's recommended to set int type as primary key to get a fast search.

### Join query
```
mysql> SELECT a.id, a.name, a.age, b.sale FROM account a, work b WHERE a.id=b.id
```
The simple join only fetch records meeting the condition. There is another join, called `left join`, which will give extra consideration to the left table. In a word, records in the left table not matching the condition will be will be fetched. In that case, fields for the right table will be populated with `NULL`.
```
mysql> SELECT a.id, a.name, a.age, b.sale FROM account a LEFT JOIN word b WHERE a.id=b.id
```

### Pattern matching in MySQL
Two meta character are supported for matching:
- %: zero or more 
- _: any single character

Here are some examples and their explaination:
- s%: a value that begins with letter 's'
- %s: a value that ends with letter 's'
- %s%: a value that contains the letter 's'
- s%l: a value that begins with 's' and ends with 'l'
- s%l%: a value begins with s and contains at least one instance of letter 'l'
- s_l%: a value begins with 's' and whose third letter is 'l'
- __%: a value with at least two characters

SQL syntax: `SELECT * FROM mail WHERE name LIKE 'g%' `

**NOTICE:** Here the condition should use 'like', instaed of eqaulity mark. `g%` shoule be quoted by single quotation mark or double quotation mark.

