# Lifecycle methods

Lifecycle methods are methods that React will call in different situations.

For example:
- `componentDidMount` will be called once the Component is mounted the first time.
- `componentWillReceiveProps` is invoked before a mounted component receives new props.

[Here](https://facebook.github.io/react/docs/react-component.html#the-component-lifecycle) is a list of these lifecycle methods.

### Try it out

Go to your `Header` class for example and create this methods in the class.

Just log something different in everyone and you will see when they are called.

### Usage

The most useful is to fetch some data from the server when the component is mounted.

```javascript
// ...
componentDidMount() {
  fetch('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
    .then(res => res.json())
    .then(quotes => {
      this.setState({
        quotes,
      });
    });
}
// ...
```

It is very common to fetch some data when the Component is mounted and then change the state.

React will take care of re-rendering once the state has changed.
