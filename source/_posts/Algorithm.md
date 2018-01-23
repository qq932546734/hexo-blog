---
title: Algorithm
date: 2017-11-12 10:37:01
tags: [Algorithm]
categories:
    - [CS, Basics]
---

Running time
exchange


## Basic sort algorithm

### selection sort

First, find the smallest item in the array and exchange it with the first entry (itself if the first entry is already the smallest). Then, find the next smallest item and exchange it with the sec- ond entry. Continue in this way until the entire array is sorted. This method is called selection sort because it works by repeatedly selecting the smallest remaining item.

Selection sort uses  N 2/2 compares and N exchanges to sort an array of length N.

Disadvantage: Even the given array is already ordered, it still needs to perform comparison the same times. Namely, this sorting algorithm can't take advantage of orders.
Advantage: data movement is miminal, since movements is linear with the array size.

### Insertion sort

Each time, choose one item and put it in the proper place among the already sorted items, until the last one has been put into the right place. There are two type of insertion sort: in-place sort or non in-place sort. 

The worst case is  N 2/2 compares and  N 2/2 exchanges and the best case is N   1 compares and 0 exchanges.

Advantage: if the array is some kind of sorted, insertion sort will run much faster. Insertion sort is very suitable for partially sorted array. And, it also good for short array.
Disadvantage: it requires many exchanges if the order is revesed.

### Shell sort 

Shellsort gains efficiency by making a tradeoff between size and partial order in the subsequences. At the beginning, the subsequences are short; later in the sort, the subse- quences are partially sorted. In both cases, insertion sort is the method of choice.

Shellsort is perfer for some kind of sorted array and arrays with little size. At the same time, the improved h-th shell sort make shell sort works well for large array. Thus, it's a choice in most cases.

> Experienced programmers sometimes choose shellsort because it has acceptable running time even for moderately large arrays; it requires a small amount of code; and it uses no extra space.