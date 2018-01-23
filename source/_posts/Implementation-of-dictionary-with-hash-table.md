---
title: Implementation of dictionary with hash table
date: 2017-12-13 21:37:23
tags:
---

### hash table
1. hash function convert the search key into an integer, then compress the large integer to a smaller number within the range of hash table size.
2. hash table size is often a prime number.
3. when two search key hash to the same hash index, we call it index collision. There are often two ways to resolve it. First one is called open addressing, which means to store them in other buckets. Open addressing can be achieve by Linear probing, Quadratic probing and Double hashing. The main priciple is to mark all bucket as one state of null(never used before), available(used once then item removed) and occupied(being used). Search will start from the first matching bucket till the null bucket. Another way is making each bucket able to hold multiple items. we call it separate chainig. The bucket can be a list, sorted list, chain of linked nodes, Array or vector.


### Implemetation of dict in python
Dictionary and set are implemented using hash table. It uses the built-in hash function to calculate the hash index.  
