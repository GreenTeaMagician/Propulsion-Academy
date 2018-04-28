# Getting Started With React

First of all, make sure you have `node` and `npm` installed.

Make sure you have Node >= 6 and npm >= 3. Run `node -v` and `npm -v`.

### Hello world

First install `react-create-app` `npm` package.

```
npm install -g create-react-app
```

Then in the folder where you want to create your app run the following:

```
create-react-app hello-world
```

Where `hello-world` is the name of your app.

This will create a folder `hello-world` in that directory.

Then enter that folder and run:

```
npm start
```

This might open a new tab in your browser in `http://localhost:3000/`. If it doesn't, go to the url opening a new tab manually.

You have just created your first React application!

### React-create-app

`React-create-app` is a project by Facebook to easily create React app without configuration.

Usually, if you want to create your React application you have to do a relatively big setup. Either with Webpack and Babel or other tools. However, using `create-react-app`, you rely on the configuration given to you.

Check their amazing [docs](https://github.com/facebookincubator/create-react-app)

This is perfect for beginners.

### Important files

At this moment, please review the following files: `src/App.js`, `src/index.js` and `public/index.html`.

**index.html**

Check that you have:

```html
<div id="root"></div>
```

**src/index.js**

Everything starts here.

As you can see, here you are requiring the component App: `import App from './App';`

Then using a `ReactDOM.render` to initialize the app.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // requiring the component from below
import './index.css'; // requiring general CSS

ReactDOM.render(
  <App />, // using the component
  document.getElementById('root') // remember you have a `div id="root"` in the html
);
```

**App.js**

This is your first component:

```javascript
import React, { Component } from 'react';
import logo from './logo.svg'; // you can also require images. Webpack will handle this.
import './App.css'; // requiring the CSS for this component

class App extends Component { // extending from Component
  render() { // render needs to return JSX
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App; // don't forget to export the component
```

### JSX

You might have noticed `<div className="App">`. Why `className` and not `class`?

The `return` value of the `render` method is not HTML, but JSX.

We will go deeper into JSX later. However, for now let's say that in JSX, to add a class you need to use `className` instead of `class`.
