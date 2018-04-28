# React State

As we have seen `props` is a way to customize what's rendered from the parents.

State is a way to customize the component from inside.

### Setup state

Remember that with ES6 classes we have the `constructor` which is the function called when creating a new instance of the class.

It is in the `constructor` of the Component that we can setup the `state`. This will be the initial state of the component.

The state might change according to events, requests, etc.

In this example let's move the list of todos to the state of the `TodoList` component.

```javascript
// ...

class TodoList extends Component {

  constructor(props) {
    super(props); // remember we are inheriting from Component. We still want to call the parent initializer

    this.state = {
      todos: ['Master JS', 'Learn React', 'Learn Redux']
    }; // that's it :)
  }

  render() {
    // no need for this => const todos = ['Master JS', 'Learn React', 'Learn Redux'];
    // we will use this.state.todos
    return (
      <ul>
        {
          this.state.todos.map((todo, index) => {
            return <TodoItem key={ index } todo={ todo } />;
          })
        }
      </ul>
    )
  }
}
```

### Change the state

The state is just a property of the Component. However, it has a few particularities.

First of all, you are not supposed to reassign it with `=`.

Do not do this `this.state = 'some other value';`. Except when you set it up in the constructor.

If you want to change the value of the `state` you use `this.setState` which is a method that expects an object and it will merge it with the current `state`.

Once the state has changed, React will take care of re-render again.

Try this in the constructor:

```javascript
constructor(props) {
  super(props);

  this.state = {
    todos: ['Master JS', 'Learn React', 'Learn Redux']
  };

  setTimeout(() => {
    this.setState({
      todos: ['Master JS', 'Learn Redux']
    });
  }, 3000);
}
```

This will change the state after 3 seconds. You should see how the todo list changes.

### Conclusion

This is the most powerful feature of React.

You take care of handling the state of the Application. React will take care or re-rendering.

There is no need to manipulate the DOM. React does it for you.
