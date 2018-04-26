# Todoing with React and Redux

Remember yesterday Todo List with React?

Today you will add Redux to it

### Todo List

For now, move the Todo List to Redux.

This means, that instead of having the State of Todos in the `App` Component. The array of Todos will be in Redux.

Don't worry, you have the whole day for it.

If you don't know how to implement something.

Refer to the notes or [Redux Docs](http://redux.js.org/docs/introduction/).

These are the steps. Read through all of them first. Then start implementing.

### Create a Store

Create a Redux Store. Just one reducer. Initial State could be a `{ hello: 'world' }`.

Connect the Redux Store to `App`. Use `Provider`, `connect` and `mapStateToProps`. You should be able to print the initial state in the console. With a log in the `App` component.

### Filter State

Move the Filter to the Redux Store. Not the todos yet.

You are going to use `combineReducers` at this point. The `filterReducer` will have a `'all'` as initial State. This is how the whole state should look like:

```javascript
{
  filter: 'all'
}
```

Use the filter from the Redux State rather than the one in the `App` Component State.

You will need to get that State from Redux and use it in your Components.

Remove that Component state. At this point, you will get errors when trying to change the filter.

**Important:** Remember about `PropTypes`.

### Change Filter State

Create the actions creators for changing the state.

In the reducer of the `filter` act accordingly and change the state depending on the type of action that passes through it.

By the end of this exercise you should be dispatching actions to change the `filter` state.

Connect the `Filter` Component to the Redux store, then you should be able to dispatch actions from there.

```javascript
this.props.dispatch(action);
```

### Todos State

Implement each step at a time.

The Todo App will be partially broken until the end of the steps. Each step will just fix one small thing at a time.

First of all, move the State of Todos -the array of todos- to the Redux State.

You will need to create another reducer for it: `todos`.

Create it with an initial State with some Todos so that you can check whether it's working properly.

```javascript
// ...
const initialTodos = [
  { id: 1, content: 'Learn JS', completed: true },
  { id: 2, content: 'Learn React', completed: false }
];

const todosReducer = (state = initialTodos, action) => {
  // ...
}
// ...
```

Use this initial State instead of the one from the `App Component`.

After this step you won't need any Component State. Except in the `NewTodo` to handle the input to create new todos and the Ron Swanson Quote if you got there.

**Important:** Remember about `PropTypes`.

### Filter todos

Remember that you can switch the view of the Todos with a filter.

This means that the list of todos passed to the Component, depends on the `filter` State.

Implement a filtering in the `mapStateToProps` of the Component receiving the Todos.

Do not just pass down all the Todos. Only those filtered according to the value of the `filter` State.

**Ask for a code review at this point**

### Add a Todo

Adding a todo means:

- Action creator to create the Action
- Expect and act accordingly in the `todosReducer`. Remember to return a new object every new State.
- Connect the `NewTodo` to the store
- Dispatch the action from the `NewTodo` component

Maybe we missed some step. Too bad, it will be up to you to find out ;)

### Toggle Todo

Toggle a todo from completed to pending requires the same steps as previously:

- Action Creator
- `todosReducer`
- Connect the component
- dispatch the action when needed

### Removing a Todo

Same same, but different.

### Bonus Features

- Add the quote of Ron Swanson to the State
- Go to [react-redux](https://github.com/reactjs/react-redux) Github page and investigate and implement `mapDispatchToProps`.
- Go to the [Redux Docs](http://redux.js.org/docs/basics/UsageWithReact.html). Read about Presentational and Container Components. Implement these differentiation.
- Use the proper `shape` for your `PropTypes`.
