---
title: Webpack
date: 2017-12-05 09:39:18
tags: [tools, ]
categories:
    - [JavaScript, Basics]
---

### What's webpack?
One of the good things accompanying `Node` is module. With module, you can split your app's functionalities into different files, which will make your code more easy to manage. Also, some modules are reusable. But it becomes cubomsome if we want to import all these files into one html page. Here comes the handy tool, webpack, which is designed to combine all of these modules and facilitate importion by creating just one file to be imported. In concise, it's a module bundler.

With `Loaders`, we can also import CSS, SASS, JSX(react) except for js module. Common loaders include CSS&Style, Sass&Less, JSX, Babel, Coffee, TypeScript, EJS, Pug, HandlerBars, json.

#### What's a source map?



### How does it work?
There are mainly two approaches to execute webpack command.
#### With configuration file
Create a configuration file `webpack.config.js` to define the entry point of your modules and the output file.
##### A gist of webpack configuration
```js
let debug = process.env.NODE_ENV !== 'production';
let webpack = require('webpack');

module.exports = {
    context: __dirname,
    devtool: debug ? 'inline-sourcemap' : null,
    entry: './js/scripts.js',
    output: {
        path: __dirname + '/js',
        filename: 'scripts.min.js'
    },
    module: {
          loaders: [
              {test: /\.css$/, loader: "style-loader!css-loader"},
              {test: /\.js$/, loader: "babel-loader, exclude: /node_modules/, query: {presets: ['es2015']}"}
          ]    
      }, 
    plugins: debug ? [] : [
        new webpack.optimize.DedupePlugin(),
        new webpack.optimize.OccurenceOrderPlugin(),
        new webpack.optimize.UglifyJsPlugin({
                mangle: false,
                sourcemap: false
            })
    ]
};

```
#### Easy one
```shellsession
$ webpack <entry.js> <final.js>
```


### CSS loader
First, install the loaders.
```
$ npm install -s css-loader style-loader
```
Then, inside your js module, import your css with css-style loader.
```js
require('!style-loader!css-loader!./theme.css');
```
Of course, this does not look good. Let's turn to the configuration file of webpack and define which loader to load files with `.css` extension. After doing so, we can require css file like how we require normal js file.

### Babel loader
Babel is used for ES5 compatiblity.
```shellsession
npm install babel-core babel-loader babel-preset-es2015 --save-dev
```

### Webpack dev server
```shellsession
$ npm install -g webpack-dev-server --save-dev
```
package.json
```js
{
    "scripts": {
        "start": "webpack-dev-server --entry ./src/js/app.js --output-filename ./dist/bundle.js",
        "build": "webpack"
    }
}
```

### Best practice
organize your source code and other files.  

Source code including js, css file should be included inside src file. Another sibling foler named `dist` is used for generated files during the building process. `package.json`, `webpack.config.js` should be in the root of the project foler. All commands used for building, test and so on should be written in the `package.json` scripts so that we can build our app with `npm build`.

### Things to explore
Babel, 

### The advantage of using webpack
1. It facilitates modules importion;
2. variables only work in the module they exist, thus no global variable conflict. For example, if only one of these js scripts import jquery, jquery will only work in that module. After import the minified bundle script, jquery won't work in the global scope.
3. It makes possible for every module only doing one thing.


