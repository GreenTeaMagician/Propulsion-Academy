# Functional Components

In a nutshell:

  - Functional Components are functions that return JSX
  - Class Components are Classes with the `render` method

### How to use them

Both are used in the same exact way.

While using them there is no way to differentiate them.

```javascript
<Header />
```

`Header` could be either a Functional or a Class Component.

### Functional Component

```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

The function will be called with the `props` passed.

When used:

```javascript
<Welcome name="Sam" />
```

### When to use them?

Use Functional Components always that is possible.

They are more performant than Class Components.

However, since they are just functions, they can't have State nor they can have any behavior since you can't add methods.
