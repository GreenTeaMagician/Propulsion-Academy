# Redux Counter

The exercise is to create a counter using Redux.

Just the number and a button to increase and a button to decrease.

### Setup

Create an HTML with a `<p>` tag to render the number and 2 buttons.

Give those ids so that you can use `getElementById`.

Require Redux:

```HTML
<script src="https://unpkg.com/redux@latest/dist/redux.min.js"></script>
```

This will create the `Redux` global variable. You are going to use `Redux.createStore` to create the Redux Store.

Add also a script tag requiring your JS file. Place it at the bottom of the `<body>` tag so that you don't have to worry about the document ready.

### Create Store

The State of this app will be just a number. Not an object.

Remember that the reducer is a function. It expects the State and an action. It returns the new State.

```javascript
var reducer = function(state = 0, action) {
  // ...
}
```

Create a store with this reducer

### Render Initial Counter

Once you have the store. You can access the state with `store.getState()`.

Create a `render` function. It should have access to the store, access the state with `getState` and append the state into the `<p>` tag that is in the HTML.

### Subscribe to the store

The store has a method that will notify us every time the State changes.

When the state changes, we will want to call this `render` function.

```javascript
store.subscribe(render);
```

`subscribe` is a method that expects a function as a parameter -a callback-. This function will be called every time the State changes.

### Buttons

Now you add event listeners to each button.

The increment button should dispatch an action that will increment the State.

The decrement button should dispatch an action that will decrement the State.

*Check [YouMightNotNeedJQuery](http://youmightnotneedjquery.com/) for how to add listeners with vanilla jQuery*

1. Add the listeners.
2. Dispatch a different action in each of them.
3. Complete the reducer to act accordingly to every different action.

An action could look something like this:

```javascript
{ type: 'increment' }
```

In this app actions, there is no extra information. We just need to know whether increment or decrement the state.

**Call an instructor for a code review**

### Add a Todo List

Next try to add a Todo List next to your counter.

The Todo List would be managed as well by Redux.

So far the state was only the number of the counter.

However, now it will have 2 different parts:

- Counter
- Todos

So it would be something like this:

```javascript
{
  counter: 0,
  todos: ['Learn Redux', 'Master React']
}
```

**First step**

Change the initial state to have place for the Todos.

Make sure that the Counter still works.

**Second step**

Add a list of todos to your initial state.

Render them in the page in some `<ul>`.

**Third step**

Add todos.

Add an input and a button to be able to add todos to the list.

Steps:
- Add a listener on the button click
- Get the value in the input
- Dispatch an action
- Handle the action properly in the reducer

**Fourth Step**

Use `combineReducers`.

Probably you have one single reducer handling the counter and the todos.

Investigate what [combineReducers](http://redux.js.org/docs/api/combineReducers.html) does and use it.

**Congratulations you just created your first Redux App!!**

### Bonus

- Remove Todos.
- Set a Todo as completed.
- Filter Todos: *all*, *not completed*, *completed*.
