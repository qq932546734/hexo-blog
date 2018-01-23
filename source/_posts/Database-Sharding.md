---
title: Database Sharding
date: 2017-11-13 09:22:17
tags:
---


> A database shard is a horizontal partition of data in a database or search engine. Each individual partition is referred to as a shard or database shard. Each shard is held on a separate database server instance, to spread load. Some data within a database remains present in all shards,[notes 1] but some appears only in a single shard. Each shard (or server) acts as the single source for this subset of data. --wiki

### Advantage and disadvantage
#### Advantage
1. Since tables are divided and distributed into different servers, rows of each talbe in each databases are reduce, thus reducing index size and speeding up search procedures.
2. Tasks are assigned to multiple machines, which can improve performance significantly.
3. If there are some real-world segmentation of the data, such as in region, seperating them into different database shard can make it possbile to query on the needed part of the corresponding tables.

#### Disadvantge
1. high reliance on the interconnect between servers.
2. Increased latency.
3. high tendency towards failure in consistency and durability.

While horizontal partition often happens within a single isntance of a schema and a database server, sharding splits rows of tables into multiple instance of a schema and servers. 

Some examples of database supporting sharding include `Apache HBase, MongoDB, MySQL Cluster`.