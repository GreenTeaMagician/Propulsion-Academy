# First Best Practices

With `create-react-app` you are using Webpack to handle the CSS files as well.

Remember the CSS and Style Loader from JS Advanced? This is what is happening with `import './index.css';`

### One folder per Component

If you have followed from the previous notes, you have a project with 3 components:
- `App`
- `Header`
- `Intro`

However, `Header` and `Intro` don't have CSS files.

All the styles are in the `App.css` file. Which is imported in `App.js`. If we import them, then Webpack takes care of adding them to page.

In `App.css` you define `.App-header` which you later use in `Header.js`.

Let's change that.

From now on, every component will have a folder. Inside the folder there will be 2 files, a JS file and a CSS file.

We will also create a folder that will store each of the Components folder.

Start with the `Header` component in `src/Header.js`.

Move it to `src/components/Header/index.js`. Then create the CSS file there `src/components/Header/index.css`. Add the classes that you are using in `Header/index.js`. Remove them from `App.css`.

Move also the `logo.svg` in the `src/components/Header` folder.

Remember to import the CSS file in `Header/index.js` with `import './index.css';`.

Repeat the same for `Intro` and `App`.

By the end of this step you should have the following tree structure:

```
.
+-src/
| +-index.css
| +-index.js
| +-components/
|   +-App/
|     +-index.js
|     +-index.css
|   +-Header/
|     +-index.js
|     +-index.css
|     +-logo.svg
|   +-Intro/
|     +-index.js
|     +-index.css
```

Review all the imports. Remember that imports are relative. For example, in your `src/index.js`, if you want to import the `App` component. You need to change `import App from './App.js'` to `import App from './components/App/index.js'`;

**Pro Tip:**

If the name of the JS file inside a folder is `index.js`. When importing if from outside you can skip the name of the file.

Instead of:

```javascript
import App from './components/App/index.js';
```

You can simply:

```javascript
import App from './components/App';
```

### CSS Best Practice

The main idea of the Component is that they should be decoupled and independent from each other.

A good practice apart from the folder per component, is to have the namespace of the Component in the CSS classes used in the component.

Current classes are `App-header` or `App-intro`. That's because they were all used in the `App` Component.

Since you already moved that to each separate CSS file, change the classnames accordingly.

Instead of `App-header` call it `Header`. Instead of `App-logo`, call it `Header-logo`.

When using namespace you avoid classes from stepping on each other. Imagine you wanted to use the class `container` in two different containers. Using the namespace, it would be `Header-container` and `Footer-container`.
