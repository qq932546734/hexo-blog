---
title: Native desktop App with Electron
date: 2017-11-28 20:09:08
tags:
---
A tutorial of creating a Native desktop app with Electorn for beginner!

<!-- more -->

1. cd to your working directory, `npm init` to create the **package.json** file. When asked aobu the entry point, type something like `main.js`.
2. If this is the first time you install `electron`, firstly install it as a global package with `npm install -g electron`. After doing this, the package would be avaiable for every project depending on it. Of course, for each project, you have to save it locally to your `package.json` file with `npm install --save electron`.
3. In order to quickly start your app, use scripts listed in the `package.json` file. 
```
"scripts": {
    "start": "electorn ."
}
```
<!-- more -->
4. create the `main.js` file and start to write your app.
```js
const electron = require('electorn');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electorn;

let mainWindow;
let addWindow;

// listen for the app to be ready
app.on('ready', function(){
    //create new window
    mainWindow = new BrowserWindow({});
    // load html into window
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'mainWindow.html'),
        protocol: 'file:', 
        slashes: true
        }));

    // Quit app when closed
    mainWindow.on('close', function(){
        app.quit();
        })

    // Build menu from template
    const MainMenu = Menu.buildFromTemplate(mainMenuTemplate);

    Menu.setApplicationMenu(mainMenu);

    });

// Handle add window 
function createAddWindow(){
    //create new window
    addWindow = new BrowserWindow({
        width: 200,
        height: 300,
        title: 'add shopping list itme'
        });
    // load html into window
    addWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'addWindow.html'),
        protocol: 'file:', 
        slashes: true
        }));

    // Garbage colleciton handler
    addWindow.on('close', function(){
        addWindow = null;
        })
}

const mainMenuTemplate = [
    {
        label: 'File',
        submenu: [
            {
                label: 'Add Item',
                click(){
                    createAddWindow();
                }
            },
            {
                label: 'Clear Items'
            },
            {
                label: 'Quit',
                accelerator: process.platfrom == 'darwin' ? 'Command+Q': 'Ctrl+Q',
                click(){
                    app.quit();
                }
            }
        ]
    }
];

// if mac, add empty object to menu
if (process.platform == 'darwin') {
    mainMenuTmeplate.unshift({})
}

// Add developer tools item if not in prod
if (process.env.NODE_ENV !== 'production') {
    mainMenuTemplate.push({
        label: 'DevTools',
        submenu: [
            {
                label: "Toggle DevTools", 
                accelerator: process.platform == 'darwin' ? 'Command+I' : "Ctrl+I",
                click(item, focusedWindow){
                    focusedWindow.toggleDevTools();
                }
            }
        ]
        })
}


```
5. Start your app with `npm start`.