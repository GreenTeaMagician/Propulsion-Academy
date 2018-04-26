# Folder Structure

The amount of small pieces that we have so far has grown exponentially.

Reducers, `createStore`, actions, `Provider`, dispatching, mapStateToProps, ...

### Recommended Folder Structure

This is the recommended folder structure:

```
.
+-src/
| +-components/
|   +-App/
|     +-index.js
|     +-index.css
|   +-Header/
|     +-index.js
|     +-index.css
|     +-logo.svg
|   +-Intro/
|     +-index.js
|     +-index.css
| +-store/
|   +-index.js
| +-index.css
| +-index.js
```

### Redux Stuff

All the Redux reducers, actions and `createStore` should go into the `store` folder.

Specifically, start with this in the `store/index.js`:

```javascript
import { createStore } from 'redux';

const reducer = (state = {}, action) => {
  return state;
}

const store = createStore(reducer);

export default store;
```

Then you can start implementing the reducers and maybe use `combineReducers` if you need to.

**The most important is that you export the store**

### Provider

The `Provider` could be used in the `src/index.js` which is the entry point.

`src/index.js`:

```javascript
// ...
import store from './store';

ReactDOM.render(
  <Provider store={ store }>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

**The Most Important is that you import the store and use the Provider**

### Connected Components

Then, each component that you might want to connect. You will use `connect`.

`components/App/index.js` for example:

```javascript
// ...

class App extends Component {
  // ...
}

const mapStateToProps = (state) => {
  return {
    todos: state.todos,
  }
};

export default connect(mapStateToProps)(App);
```
