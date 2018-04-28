# Looping

There is a very common usage of Props.

Creating components based on an array of values.

### Todo App

Let's start a Todo App. Based on what you have so far.

First, remove the `Intro` component.

Create a `TodoList` component. This will render the list of Todos.

In your `components/App/index.js` you should have something like this:

```javascript
render() {
  return (
    <div className="App">
      <Header />
      <TodoList />
    </div>
  )
}
```

Then in the Todo List we are going to render a `<ul>` and a `<li>` for each Todo.

```javascript
render() {
  return (
    <ul>
      <li>Master JS</li>
      <li>Learn React</li>
      <li>Learn Redux</li>
    </ul>
  )
}
```

This is not very good. Remember that with JSX we can use `{}` to add JS Expressions:

```javascript
render() {
  const todos = ['Master JS', 'Learn React', 'Learn Redux'];

  return (
    <ul>
      {
        todos.map(todo => {
          return <li>{ todo }</li>;
        })
      }
    </ul>
  )
}
```

You get a warning with this. This is because when you create elements dynamically within a loop React needs a way to differentiate one from the other.

```javascript
render() {
  const todos = ['Master JS', 'Learn React', 'Learn Redux'];

  return (
    <ul>
      {
        todos.map((todo, index) => {
          return <li key={ index }>{ todo }</li>;
        })
      }
    </ul>
  )
}
```

Take a closer look at `<li key={ index }>{ todo }</li>`. There are a few important things going on in there.

First, the `key` is a prop that React uses internally to differentiate different elements created dynamically with a loop.

Second `{ todo }`: `todo` is just each element in the `todos` array. Which means that is just a string.

Third, mapping through the `todos` array we are creating a new array of React Elements.

Similar to this:

```javascript
<ul>
  {
    [
      <li>Master JS</li>,
      <li>Learn React</li>,
      <li>Learn Redux</li>
    ]
  }
</ul>
```

That is one of the cool things about React and JSX. We can pass an array of Elements as Children. As long as each of them have a `key` property that is unique.

### TodoItem

Let's go a little bit further and create a new custom Component for each todo. Instead of just a `<li>`.

Create the `TodoItem` Component in `src/components/TodoItem/index.js`.

This is how to use it. It's your job to implement the `TodoItem`.

```javascript
render() {
  const todos = ['Master JS', 'Learn React', 'Learn Redux'];

  return (
    <ul>
      {
        todos.map((todo, index) => {
          return <TodoItem key={ index } todo={ todo } />;
        })
      }
    </ul>
  )
}
```

We are passing the `todo` as a `prop` of `TodoItem`. `TodoItem` should render a `<li>`.
