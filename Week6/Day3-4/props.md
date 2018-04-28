# Props

Props and State are probably the hardest things to grasp as a beginner in React.

However, it shouldn't be that way.

### Header with props

At this moment, the `Header` has the title hardcoded in it. `Welcome to React`.

However, what if we could change the title when using the `Header`. In some page we could use `Welcome to React` and in another place `Goodbye Angular`.

We can accomplish this with the Props of the component.

**Pass props**

In `App/index.js`:

```javascript
render() {
  return (
    <div className="App">
      <Header title="Goodbye Angular" />
      <TodoList />
    </div>
  )
}
```

We add something that looks like an HTML attribute -`title="Goodbye Angular"`- to the `Header`. These are the props.

**How to use props**

If we don't change anything in our `Header`, it will still render `Welcome to React`.

If we want to use it, we need to use `this.props`.

```javascript
render() {
  return (
    <div className="App-header">
      <img src={ logo } className="App-logo" alt="logo" />
      <h2>{ this.props.title }</h2>
    </div>
  )
}
```

Take a look at this:

```
<h2>{ this.props.title }</h2>
```

Now we are interpolating some JS expression in JSX. We are using whatever value we have in `this.props.title`.

React attaches all the Props to `this.props` inside the Component Class.

In this specific situation we passed `<Header title="Goodbye Angular" />`: `title` is the prop. Hence `this.props.title` will have `Goodbye Angular`.

### Children props

HTML tags usually have children:

```html
<div class="App-header">
  <img src={logo} class="App-logo" alt="logo" />
  <h2>Welcome to React</h2>
</div>
```

The `<div>` has the `img` and `h2` tags as children.

We can do similar with JSX and our own components.

Instead of passing the title as a `title` prop. We could pass it as a child.

```javascript
render() {
  return (
    <div className="App">
      <Header>Goodbye Angular</Header>
      <TodoList />
    </div>
  )
}
```

Take a close look at `<Header>Goodbye Angular</Header>`.

Now we are not passing the `title` prop. We have an opening and closing `Header`.

With React. Whatever we pass between the opening and closing tags is also a props. A special kind of prop: `this.props.children`.

So, instead of using `this.props.title`. We will do:

```javascript
render() {
  return (
    <div className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <h2>{ this.props.children }</h2>
    </div>
  )
}
```

The children could be a:
- String
- One React Component
- More than one React Component
