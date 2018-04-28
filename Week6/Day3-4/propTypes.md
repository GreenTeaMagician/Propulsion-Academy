# Typechecking With PropTypes

Typechecking the Props is a way to make sure that the component will receive the Props expected when you use it.

### Your first Typechecking

You need to install a new library first: `prop-types`.

In your `TodoItem` you expect a `todo` prop. More specifically, you expect `todo` to be a String.

In your `TodoItem/index.js`:

```javascript
import PropTypes from 'prop-types';
// ...
class TodoItem extends Component {
  // ...
}

TodoItem.propTypes = {
  todo: PropTypes.string
};
// ...
```

As you can see, `propTypes` will be a property of the Class `TodoItem`. It expects an object with the props you want to check.

[Here](https://facebook.github.io/react/docs/typechecking-with-proptypes.html) you have a great explanation and list of this.

**Required Props**

Typechecking is great. Usually it just warns about the types.

If you want to ensure something, you can mark that prop as required.

```javascript
//...
TodoItem.propTypes = {
  todo: PropTypes.string.isRequired
};
//...
```

By adding `isRequired` at the end, React will raise an error if that Prop is not passed.

### Default Props

You can also set default values of the props.

```javascript
// ...
TodoItem.defaultProps = {
  todo: 'Learn PropTypes!'
};
// ...
```
