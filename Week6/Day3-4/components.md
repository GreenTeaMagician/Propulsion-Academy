# React Components

### Your first component

Follow from the previous getting started project.

**Create the component**

Create a new file `src/Header.js`.

In there copy the code:

```javascript
import React, { Component } from 'react';

class Header extends Component {
  render() {
    return (
    );
  }
}

export default Header; // don't forget to export the component
```

Now, go to `src/App.js` and get the `div` with the class `App-header` and all it's children:

```javascript
<div className="App-header">
  <img src={ logo } className="App-logo" alt="logo" />
  <h2>Welcome to React</h2>
</div>
```

Add this as the return value of your `render` method.

**Use the component**

Now instead of having that code in `src/App.js` we created a component just for it.

Let's use it in `src/App.js`.

First import the component: `import Header from './Header.js'`.

Then in the `render` method. Substitute the `<div className="App-header">` and children with the Component.

```javascript
class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}
```

Go and check in `localhost:3000` that everything is still working.

You just created and used your first component!

### What is a Component

Simply set, a Component is just a Class that implements a `render` method that returns JSX.

*You can also have a Function to be a Component, we will see that later in the week.*

JSX is almost HTML. But we can use other Components in there, not just HTML tags. Just like we did with `<Header>`.

This class needs to inherit from `Component` which we import from `react` library.

Hence:

```javascript
import React, { Component } from 'react'; // importing

class Header extends Component { // extending
  render() {
    return ( // the value should be JSX
    );
  }
}

export default Header; // never forget to export it!!!
```

Repeat with me:

**A Component is a Class that implements a `render` method returning JSX**

Apart from the word JSX, you should be comfortable with the rest of the concepts.

### How to use a Component

We can use a Component just like we would an HTML Tag. JSX and React will take care of everything else.

Hence:

```javascript
render() { // render needs to return JSX
  return (
    <div className="App">
      <Header /> // our own component
      <p className="App-intro">
        To get started, edit <code>src/App.js</code> and save to reload.
      </p>
    </div>
  );
}
```

Do not forget to import the component in the file you are using it. There is no magic here. In order to use it, you need to import it.

### Why to use Components

Components make it very easy to reuse code. For example, we might have another place where we want to use the same header.

If we have a component we can import it wherever we want and use it easily.

Components help us to understand and reason about our UI.

They are also configurable. Which means, that if we have two very similar components, we might want to create one and somehow configure it depending on where we are using it.

There are many more reasons to use Components and/or React. You will see the power of this type of front-end development during this week.

### Your turn

Create a new component `src/Intro.js`. Use this component instead of the `p` tag with the class `App-intro`.

By the end of this small step you should have the following in `src/App.js`.

```javascript
import React, { Component } from 'react';
import Header from './Header';
import Intro from './Intro';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Intro />
      </div>
    );
  }
}

export default App;
```

If you go to `localhost:3000` you should have exactly the same.

### Do Not forget

Everything is initialized `src/index.js`.

```javascript
ReactDOM.render(
  <App />, // using the component
  document.getElementById('root') // remember you have a `div id="root"` in the html
);
```
