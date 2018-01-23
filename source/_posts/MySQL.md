---
title: MySQL
date: 2017-11-06 15:43:18
tags:
---


### I want to query all data from a table, but the table has thousands of rows, how should I write my SQL query systax?

### 

### fetch rows with a specific column's length greater than 10
`SELECT count(*) from target_table WHERE LENGTH(column_name)>10`


### How to select with sort?
```
SELECT DISTINCT pasid from bas_userinf order by pasid;

select count(*) from bas_userinf where pasid=101101101110;

select Comment_Title, count(*) from bas_comment GROUP BY Comment_Title order by count(*);

select user_id, count(*) from bas_comment GROUP BY User_ID order by count(*) DESC;
```

### How to generrate SQL in python without quote in string type?

