---
title: Using Hexo and Github to build your own blog
date: 2017-06-19 17:17:12
tags:
---

## Writing in the begining  
I installed Hexo two months ago, when I was impressed by Hexo and excited imaging that I can use this tool to write blog everyday. However, the reality is not so inspiring. The ugly default theme, no topics to write on, and the inability to weild hexo very fluently all added to my unwillingness to work on the seemingly inspiring project. It recently comes back to my mind to continue this greate project, especially noticing the potential importance in my future job seeking process. When I start to use it again, I found that I can hardly remember the procedures on how to use it, even when refering to the official documentation. Thus, I think writing an article tracing the learning process will benefit from multiple aspects, including familiarity increasing, more practices, and writing skill improvement. So, I write this article, hoping it can also help those who also want to have their own blog. 

## Why and then how would we combine Hexo and github together?
A: Well, Hexo provides an awesome approach to build your own blog, while github provide a free repository to store your content and a free personal website which can be accessed conveniently. 
## The steps to complete 
1. install Hexo
2. create a working space to store articles and necessary supporting files. 
3. editing the file `_config.yml` in the root folder, configure the deploy setting part to make sure the blogs are deployed to github when deploying. (It is necessary to have the SSH key installed and connected to your github account)

## How to change the theme?
A: Well, this is incredibly simple. First, clone/download the theme file from github (you can clone the theme folder in the root folder of your blog working space), then edit the `_config.yml` file by setting the theme name to the one you just download. `hexo g && hexo d`, you will see your blog in a new style. 

## Hexo plugins
To take the most advantage of hexo, you should try its various plugins. You can see the plugins installed in the `package.json` in the root folder. After deciding which plugins to install, use the following code to have them install:
```
npm i -S hexo-{browsersync, deployer-git, generator-feed, generator-sitmap}
```

## How to write a blog
```
$ cd <your project direcotry>
$ hexo new post <TITLE>
```
The file will be created at directory `source/_post`.

## What if you want to have your special icon for your blog?
Put your icon file `favicon` in the `source` folder.

