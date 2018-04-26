# React and Redux

React by itself is great.

However, the true power and growth of React came when it was combined with Redux.

This is what we are going to learn here.

Watch the rest of the course [Getting Started With Redux](https://egghead.io/courses/getting-started-with-redux) for more details.

**Important: The code here is for demonstration purposes. Not for you to follow along**

### Targets

The target of combining React and Redux is to:

- be able to dispatch actions from the React components.
- retrieve data from the Redux State.

Dispatching an action will change the state.

Then, React will re-render with the new state and the user will be able to see it in the page.

What we want to be able to do something like this in our `App` Component in `src/components/App/index.js`.

```javascript
// ...
class App extends Component {
  // ...
  addTodo = (content) => {
    const addTodoAction = addTodo(content); // `addTodo` is an action creator
    this.props.dispatch(addTodoAction); // this will dispatch the action
  }
  // ...
}

// ...
```

**Do not forget this**

### Listening to Redux State Changes

React Components re-render when their internal state changes with `setState`.

We want something similar when we change the State of Redux.

### Welcome react-redux

`react-redux` is an npm package that provides us with the tools to make all that possible.

This library provides 2 important things:
- `Provider` which is a React Component
- `connect` which is a function

Combining these 2 tools we will connect React to Redux.

They work together. One does not work without the other.

You will need to install both packages: *redux* and *react-redux*.

```
npm install --save redux react-redux
```

### Provider

`Provider` makes accessible the Redux store and the Dispatcher to all its children.

Without `Provider` you can't use `connect`.

**How to use it**

First import it from the package:

```javascript
import { Provider } from 'react-redux';
```

Then wrap you main Component with it. Passing as prop the store created previously.

```javascript
ReactDOM.render(
  <Provider store={ store }>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

`store` should be a store created with `createStore` from `redux` package.

Since `App` is the Parent of all the Components. Wrapping it with `Provider` ensures that all the children of `App` will also be children of `Provider`.

*It doesn't need to be in the `ReactDOM.render`. Just wrapping the Parent or all Components.*

### connect

`Provider` makes accessible the store to all their children.

`connect` is what actually connects the Component to the `store`.

**How to use**

In any component we want to 'connect':

```javascript
import { connect } from 'react-redux';
// ...
class App extends Component {
  // ...
}

export default connect()(App);
```

`connect` is a function, that when called, returns another function which expects a Component and returns that Component 'connected' to the store.

Now, we would be able to use `this.props.dispatch` inside the Component.

### How to retrieve the Redux State

Once the Component is connected to the store and we can dispatch actions. There is only one thing left.

We need to get access to the Redux State.

Remember this line:

```javascript
export default connect()(App);
```

The first time we call `connect` we didn't pass anything.

Now we are going to pass a function as first parameter to the first invocation of `connect`.

We are going to call this function `mapStateToProps`. Its responsibility will be to receive the whole Redux State and return an object, that will be added to the Component props.

```javascript
const mapStateToProps = (state) => {
  return {
    todos: state.todos
  }
};
```

As you can see is a pretty straightforward function.

This function will be called by `react-redux`. It will pass the state to it, hence that we expect it.

Whatever object this function returns, it will be merged to the props.

In this specific case, it will pass as props whatever is in `state.todos`.

**Remember:** With `combineReducers` you create namespaces for each of your reducers. Each is a part of the state.

### Conclusions

Wrap the parent container with `Provider`:

```javascript
ReactDOM.render(
  <Provider store={ store }>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

Connect whatever Component you want with `connect`:

```javascript
// ...
class App extends Component {
  // ...
}

const mapStateToProps = (state) => {
  return {
    todos: state.todos
  }
};

export default connect(mapStateToProps)(App);
```
