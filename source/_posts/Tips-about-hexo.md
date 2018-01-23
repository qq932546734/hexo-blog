---
title: Tips about hexo
date: 2017-12-03 13:11:53
tags:
    - hexo
    - another
categories:
    - [Tools, Hexo]
---

### Preface
Hexo is a wonderful tool and there are lots of useful functions for us to explore. Here are some common tips which can improve your experience with Hexo.
<!-- more -->

### How to set tags and categories?

Well, after you create a new post with `hexo new post <title_name>`, a new file will be created for you to modify. There are losts of attributes you can set in the head of the the post file. 
- title: default to the one you set
- date: captured automatically 
- updated: I am not sure how to set this one.
- comments: enable comment feature for the post, default to true.
- tags: multiple tags should be separated by `yaml` style.
- categories: multiple categories can be set as the same with tags. Category hierachy can be set in this way:
```javascript
categories:
    - [Top, middle]
    - [Top2, this]
```

### Color your code block
To be able to highlight code with color, two settings must be done: the hexo setting and the theme setting. In the hexo setting file, it's in `[writing] -> highlight`. By default this value is true. Then you need to change the `highlight theme` in your theme setting. In `NexT`, there are five options available.  

That's not enough. To make the style suit for the language of your code, add the language name after the first trible backticks. Available languages include `py`, `js` and so on.

Another advanced approach is using tag plugin. 
```
{% codeblock [title] [lang:language] [url] [link text] %}
code snippet
{% endcodeblock %}
```


### How to add image to your post
In hexo configuration file, set 'post_asset_folder' in writing section to true(if only serveral post needs to use image, don't set this config. Instead, create the folder by yourself). Then every time you create a new post, a directory with the same name as the post will be created along with the post. To add images to post, although you can use markdown syntax, the best way remians to use `{% asset_img <slug> <title> %}` to avoid incorrect display in archive or index page. For example:
```
{% asset_img example.jpg This is an example image %}
```

### Others
- To enable 'read more', just add `<!-- more -->` to the place in your post from where you want to hide in the preview page.
- When you are still working on your post and not yet prepared to publish it, you can create a draft with `hexo new draft <title_name>`. In this case, the file will be created in the `_draft` directory, instead of `_post`. When you get ready to publish it, `hexo publish <title_name>`



### Something to be explored
- how to add the `updated` time automatically
- 
