# Redux

Redux is an implementation of the Flux architecture.

It was built by Dan Abramov and Andrew Clark. Both work at Facebook at the moment. Both in the React project.

Redux Docs are amazing. For the first time in this bootcamp, we will refer to them.

Read the [Introduction](http://redux.js.org/docs/introduction/). The following Topics:

- Motivation
- Core Concepts
- Three Principles

Watch the course [Getting Started With Redux](https://egghead.io/courses/getting-started-with-redux).

Watch at least the first 15 videos -a little bit more than 30 min-. Total is 121 minutes.

![Redux explained](https://camo.githubusercontent.com/5aba89b6daab934631adffc1f301d17bb273268b/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6d656469612d702e736c69642e65732f75706c6f6164732f3336343831322f696d616765732f323438343535322f415243482d5265647578322d7265616c2e676966)

### Key things

**Important: The code here is for demonstration purposes. Not for you to follow along**

**How to create the Store**

Create reducer combining 2 reducers.

```javascript
const todoApp = combineReducers({
  todos,
  visibilityFilter
});
```

```javascript
const store = createStore(todoApp);
```

**How to dispatch an action**

```javascript
store.dispatch({
  type: 'ADD_TODO',
  id: 1,
  text: 'Go shopping'
});
```

### Action Creators

This is an action:

```javascript
{
  type: 'ADD_TODO',
  id: 1,
  text: 'Go shopping'
}
```

It has a `type` that will be read by the reducer and then some information about the data.

Every time we dispatch an action we could create the object literal.

However, it is very common to have functions that create this object literals.

In the previous example, the object literal is to create a todo.

If we wanted to create another todo we could just dispatch another action:

```javascript
{
  type: 'ADD_TODO',
  id: 2,
  text: 'Learn Redux'
}
```

This is easy, but it might lead to problems. We might want to change the `type` in the future. Or add more data to the todo.

If we did it like this and in the future we wanted to change something. We would have to go to all the object literals and change them.

This is why Action Creators are useful. Action Creators are just functions that return actions.

```javascript
const addTodo = (id, text) => {
  return {
    type: 'ADD_TODO',
    id, // remember ES6 object short notation
    text,
  };
}
```

Which means we could use it like this:

```javascript
store.dispatch(addTodo(2, 'Learn Redux'));
```

Here is a more readable version:

```javascript
const addTodoAction = addTodo(2, 'Learn Redux');
store.dispatch(addTodoAction);
```

**We recommend using Action Creators**
