# React events

Events is one of the most important things for user interaction.

How do we add listeners with React?

You don't add listeners in the regular way.

### Your first event

React has its own way of listening for events.

It uses special props on the Elements.

Let's try an example with `TodoItem`:

```javascript
//...
handleClick() {
  console.log('you clicked the element!');
}

render() {
  return <li onClick={ this.handleClick }>{ this.props.todo }</li>;
}
```

Go ahead and make sure you get the log when clicking on one event.

### React events

With React, if you want to add some event listener to an Element, you use the props.

In the previous example:

```javascript
<li onClick={ this.handleClick }>{ this.props.todo }</li>
```

You can see how you are using `onClick` props on the `li` element.

This is how you add events.

You can also use:
- `onChange` for `input` or `textarea`
- `onMouseEnter` or `onMoueLeave`
- [List of supported events](https://facebook.github.io/react/docs/events.html)

### React SyntheticEvent

When the handler is called. It receives something similar to the `event` object you are used to.

However, it is not exactly the same object. It is a `SyntheticEvent` created by React.

At this point this is not important. You can still use the regular `currentTarget` or `preventDefault` just like in the regular `event` object.

### Remember `this`!

Tricky question. What's the value of `this` inside `handleClick`?

```javascript
//...
handleClick() {
  console.log('you clicked the element!');
  console.log(this); // ????????!!!
}
```

Hopefully you understand that `this` will not be the instance. Which means we don't have access to `this.props` or `this.setState`.

A way to solve this? There are a few. You should understand this solution:

```javascript
<li onClick={ this.handleClick.bind(this) }>{ this.props.todo }</li>
```

However, there is a better way:

```javascript
//...
handleClick = () => {
  console.log('you clicked the element!');
}

render() {
  return <li onClick={ this.handleClick }>{ this.props.todo }</li>;
}
```

Now `handleClick` is an arrow function, not the regular function with `function` keyword.

Arrow functions do not create any new context. The context is wherever they are defined.

**Important**

Even though you can use methods as arrow functions when using React with `create-react-app`. You have to understand that this is an *experimental* feature. It is not an ES6 feature.

This is possible thanks to Babel. [Here](https://babeljs.io/docs/plugins/transform-class-properties/) you have the info.
