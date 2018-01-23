---
title: React working with typescript
date: 2017-12-26 15:39:34
tags:
categories:
    - [JavaScript, React]
---

### Create a new react component
```js

export interface IToolbarButtonProps {
    readonly ID: string
    className: string
}

export interface IToolbarButtonStates {
    
}

class ToolbarButton extends React.Component<IToolbarButtonProps, IToolbarButtonStates> {

}

```

### Each React component should have one thing unique to identify itself.
