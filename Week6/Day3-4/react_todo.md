# Todoing with React

We are going to build a todo list with React.

We know it's kind of a cliché. But it is a cliché for a good reason :)

### Todo List So Far

If you have been following the notes so far, you should have a list of Todos at this point in the screen.

You should have an Array of Todos in the State of the TodoList Component.

### Move the State

At this point, your state is in the `TodoList`. However, it's better to have it in the main component. You'll see why later in the week.

Move the state of Todos to the `App` component and pass the todos to the `TodoList` as props.

```javascript
<div>
  <Header />
  <TodoList todos={ this.state.todos } />
</div>
```

Don't forget to add the `PropTypes` to the `TodoList` Component.

**Call an instructor at this point**

### NewTodo Component

As any other good Todo App. We need to be able to create new Todos.

At this point, create a new Component: `NewTodo`. Remember to create the folder for it.

It should render an input type text and a button.

### How to handle forms

There are 2 ways to handle forms with React.
- [Controlled](https://facebook.github.io/react/docs/forms.html)
- [Uncontrolled](https://facebook.github.io/react/docs/uncontrolled-components.html)

At this point we are going to learn the Controlled. Since it is the preferred by React.

Controlled means that the State is the single source of truth of what you see in the page.

The idea is that as you keep typing in the inputs, or changing dropdowns, those changes should reflect in the state of the Component.

This means that the State of the Component with the input, needs to have a specific state for those values.

It also means that there are `onChange` events listening in the `input`, `select` or other form tags.

Something along the following code:

```javascript
  handleNewTodoChange = (e) => {
    const newTodo = e.currentTarget.value;
    this.setState({ newTodo });
  }

  render() {
    return (
      <div className="NewTodo">
        <input
          type="text"
          placeholder="Add todo..."
          value={ this.state.newTodo }
          onChange={ this.handleNewTodoChange }
        />
        <button>Add Todo</button>
      </div>
    )
  }
```

Here you can see how `input` has a listener `onChange`.

`onChange` takes the value of the input and updates the State.

Then the value of the `input` will be set by the value of the state.

This is the sequence:
1. value of `input` set to state
2. `onChange` on the `input`, get the new value
3. set the new value as the value of the state
4. value of the `input` changes, because state has changed

At this point you still can't add new todos. But you can write down in the input with a Controlled Component.

The key here is that the state of the component has the value which is inside the `input`.

### Add listener to button

Go ahead and add an `onClick` to the `button`.

Make sure it's working by logging in the console the value of the state in the handler.

### Create the new todo!

Now we are ready to create the new todo.

However, we have one small problem. The list of todos is in the `App`, and the new todo is in the `NewTodo`. How can we add the new todo to the `App` state?

The idea is that the `App` component will have a method to add a todo to the list. Then, this method will be passed as props to the `NewTodo`.

It's important to understand that we can pass absolutely anything we want as props. Also functions.

The usage of this function passed as prop, could look something like this:

```javascript
handleAddTodo = () => {
  this.props.addTodo(this.state.newTodo);
  this.setState({ newTodo: '' });
}
```

`this.props.addTodo` will be the function passed. It will be your job to implement it in the `App` Component.

Also worth mentioning how we reset the state of the `NewTodo` state to an empty string. After adding the todo to the list of todos, we empty the input.

Just by adding the todo to the array in the state of the `App`, React will take care of re-render everything.

This is the beauty of React. You only have to care of State Management. React will do the rest.

By the end of this step, you should have something like this in your `App`:

```javascript
<div>
  <Header />
  <NewTodo addTodo={ this.addTodo } />
  <TodoList todos={ this.state.todos } />
</div>
```

**Call an instructor at this point**

### Todo as an object

Each todo at this moment is just a string. It will be hard to know whether it is completed or not. Whether it has some category or something of the kind.

Let's create the todo as an object. For now a todo should be something like this:

```javascript
{ content: 'Learn React', completed: false }
```

Change the state of todos. They should all be objects, not strings.

For now let's set them all to `completed: false`.

*Do not forget to update your method to create a new todo.*

### Completed

Change some Todo to be completed.

Let's try to differentiate which Todos need to be completed and which one are pending.

This is just as easy as add a class to the todos whether they are completed or not.

```javascript
className={ this.props.todo.completed ? 'TodoItem-completed' : '' }
```

In the class `.TodoItem-completed` you can add the rule `text-decoration: line-through;`.

### Mark as completed

Let's implement a cool feature. Toggle completed when clicking on the todo.

This is going to be similar to adding a new todo.

First add an `onClick` to the `li` rendering the todo.

Then, create a method in `App` to set a todo as completed, and pass it as props to `TodoList`.

From `TodoList` pass it as props to `TodoItem`.

It is recommended to use ids to differentiate the Todos. Do not rely on the content.

```javascript
{ id: 1, content: 'Master JS', completed: true }
```

**Important:**

- Create a new Object when change the state. Don't just mutate the object
- Create a new Array of Todos, do not just change the current one. This is easy if you use `map`.

### Style a little bit

At this point you have some basic Todo App.

Spend some time to make it look good. Center the list of todos in the page for example.

*Do not get distracted and move on!*

**Call an instructor at this point**

### Getting started with Filtering

You are going to show the todos according the some filter. There will be 3 filters:

- All
- Pending
- completed

For now just create a new Component `Filter` that can sit between the `NewTodo` and `TodoList`.

This component should render 3 radio buttons.

```html
<input type="radio" name="filter" id="all" />
```

`id="all"` will identify each input.
`name="filter"` will make sure that only one of them is selected at the same time.

Add also a label next to each one of the inputs

```html
<label htmlFor="all">Completed</label>
```

Similar to `className`, instead of having `for` in `label` we have to use `htmlFor`. The value needs to match the related input `id`.

### Controlled Filter

We like our Components to be Controlled.

Which means that the `State` should have which of the radio buttons is selected.

Few tips:

- `checked` props in the `input type="radio"` elements.
- add a new part of the state in the `App` Component. `filter: 'all'` by default for example.
- create a method in the `App` to change this state. Pass it as props to `Filter` and use it.

### Let's filter

Implementing the actual filter is simple now.

We just need to pass a filtered array as props to our `TodoList`. Instead of all the todos.

**Call an instructor at this point**

### Ron Swanson Quote

Let's change the boring Header we have.

Instead of the current static Header, you will be fetching a quote from the Ron Swanson Quotes API: `http://ron-swanson-quotes.herokuapp.com/v2/quotes`

Now Header will have some State. The quote we will fetch from the API.

When the component mounts, fetch the quote:

```javascript
fetch('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
  .then(res => res.json())
  .then(quotes => {
    this.setState({ quote: quotes[0] });
  });
```

This pattern of fetching something on `componentDidMount` and changing the state is a very common pattern. Get used to it :)

Now use the state of the Component to display it in the `h2` of the `Header`.

### Change the quote

Add a button inside the header. Something simple and subtle.

When the button is clicked, you should fetch another quote and update the state with it.

### Remove Todos!

We can set todos as completed, but maybe we want to remove them completely from the list.

Add a button next to each Todo. Remove the Todo completely `onClick`.

### Bonus features

- Add a todo when pressing enter in the input
- Add Todo Category when creating them
- Add category to todo list
- Filter by category. Use Checkboxes. More than one can be selected at the same time
