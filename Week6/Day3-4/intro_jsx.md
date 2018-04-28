# Intro to JSX

Most important is to understand that JSX is just syntactic sugar.

It doesn't have any new functionality. We could accomplish the same without it.

However it is very convenient and easy to read.

### HTML Elements

```html
<h2>Welcome to React</h2>
```

Even though it looks a lot like HTML. It is not HTML. However, in this specific case this code will create an `h2` tag with `Welcome to React` between the tags.

### React Components

As we have seen with JSX we can also use React Component as Tag elements.

```javascript
<Header />
```

`Header` is not an HTML tag. It's a React Component, but with JSX we can use it as if it was an HTML Tag.

**Self Closing Tag**

If the element does not have any child. You don't need the closing tag.

`<div />` vs `<div></div>`.

### More than just HTML

However, there is one cool thing you can do with JSX you can't with HTML.

Interpolate JS code.

Example:

```javascript
render() {
  var title = 'Welcome to React';
  return <h2>{ title }</h2>;
}
```

Similar to the String Literals: `${ 1 + 1 }`.

We can add JS expressions between `{` and `}`.
