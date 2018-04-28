# Material UI

A Set of React Components that Implement Google's Material Design

### Getting Started

[Getting Started](http://www.material-ui.com/#/get-started/installation)

**Install npm package**

```
npm install --save material-ui
```

**Wrap the most parent Component in a material-ui Component: `MuiThemeProvider`.**

```javascript
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

// ...

ReactDOM.render(
  <MuiThemeProvider>
    <App />
  </MuiThemeProvider>,
  document.getElementById('root')
);
```

**Add the Roboto Font to your project.**

For example with a link to it in your `public/index.html`.

```html
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">
```

**Fix a small material-ui bug**

Install `react-tap-event-plugin` npm package.

In your `src/index.js`:

```javascript
// ...
import injectTapEventPlugin from 'react-tap-event-plugin';
// ...

// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();

ReactDOM.render(
  // ..
);
```

### How to use

From now on, if you want to use one Material UI Component. You just import it and use it as it was your own.

```javascript
import { RaisedButton } from 'material-ui';

// ...
<RaisedButton label="Default" />
```

Check out the [List of Components](http://www.material-ui.com/#/components/app-bar)

Each of this Component is used in a different way. Check always the documentation of the Component you want to use, before doing so.
