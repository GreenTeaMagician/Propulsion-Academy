# Getting Started with Webpack

Webpack is very powerful and can be confusing at the beginning.

However, when working step by step from the most basic feature it becomes clearer.

By the end of the exercises there might be a confusing configuration file, but you'll be able to understand it.

In real life projects, theses configuration files are the main reason why webpack is considered confusing.

### Install Webpack

Create a `node` project with `npm init -y`.

Install Webpack `npm install --save-dev webpack@3.8.1`. Make sure you got it in your `package.json`.

Create an `index.html` file. Add some heading there.

In the terminal create a server that will serve `index.html`. You can use `http-server`.

*If you haven't install `http-server` globally*

Just run `http-server` from inside the root folder.

Visit `localhost:8080` to make sure you serve the page.

### Add some script tag

Create a `src/` folder. Add your first javascript file there `app.js`. Require it from the index.html.

For now, just add some `console.log('hello cruel world')` in it to make sure it works.

### Your first bundle

In order to create our first bundle we need three things.

**1. Configuration File**

In the root folder create the file `webpack.config.js`. The name has to be exact.

Add the following code:

```Javascript
var path = require('path');

module.exports = {
  entry: __dirname + '/src/app.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'app.bundle.js'
  },
}
```

First of all, this file is exporting an object. That's what Webpack configuration is.

The object has two properties:

- `entry`. Which is the main javascript file. Usually it is just one file.
- `output`. Where the new created file will be. It has the `path` which is the folder where it will created and the `filename`.

**2. Run the build command**

In order to create the new bundle, you need to run the command `webpack`. Which will read the configuration file and perform the bundle.

You need to use `npm` scripts for this. Open the `package.json` and you will see a key called `scripts`.

```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "build": "webpack"
},
```

You probably already have the `test` key in the `scripts`. You just need to add `"build": "webpack"`.

Then in order to run it: `$ npm run build`. This is usually equivalent to running `webpack`, but you don't need the package installed globally.

After running the command you will see that a new folder was created `dist/` in this case, and that it has a file in it `app.bundle.js`.

Go ahead and check and try to find your code in all that mess ;)

**3. Require the new file in the HTML**

Now go to your script tag in the index.html and change the path of the javascript file.

```html
<script src="dist/app.bundle.js"></script>
```

Everything should be working normally for now.

You will need to run the build command after every change.

### Add your own module

Go ahead and create another javascript file in `src/`. Export a file from it, import and use it in `app.js`.

*Use node modules*

Remember to run the build command to check the change.

### Add an npm package

Add `moment` package.

First, install it using npm. Second require it from your `app.js`, then use it to make sure it works.

```javascript
console.log(moment().format('LTS'));
```

### ES6

Let's start using ES6.

There are some new ES6 features that are not supported by the browsers.

Because of that we want to convert those to ES5, the previous version.

Let's try it with arrow functions.

For now, when exporting do the following:

*In `src/app.js`*

```javascript
var yell = (name) => {
  console.log(name.toUpperCase());
}
```

If you are using the latest version of Chrome, this works. However, if some user enters the page with some old version of Internet Explorer, it won't work.

What we need to do, is tell Webpack to translate ES6 to ES5.

**Loaders**

From the [Webpack Docs](http://webpack.github.io/docs/using-loaders.html)

```
Loaders are transformations that are applied on a resource file of your app. They are functions (running in node.js) that take the source of a resource file as the parameter and return the new source.
```

We need a Loader that will take our ES6 code and transform it to ES5, the old Javascript.

To add a loader you just need to add it to your `webpack.config.js` file:

```Javascript
var path = require('path');

module.exports = {
  entry: __dirname + '/src/app.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'app.bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: 'babel-loader',
        options: {
          presets: ['es2015']
        }
      }
    ]
  }
};
```

*We will be using [Babel](https://babeljs.io) to transform from ES5 to ES6.*

We added one more property to the exported object: `module` and another property nested inside `rules`, which is an array.

This will try to use `babel-loader` when running your code.

- `test` is a Regular Expression to define, which files need to use this loader. For now, all ended with `.js`.
- `exclude` is the folders we don't want to compile.
- `loader` is the name of the loader.
- `options` are options for the loader. In this case there are some presents. This is Babel related, not just Webpack.

Try running now the build command. You should get an error. You don't have the loader installed.

```
$ npm install --save-dev babel-core babel-loader babel-preset-es2015
```

After installing Babel, Babel Loader and the Babel Preset you are good to go.

**Try now and check in the browser that everything is working**

**Ask for a code review to some instructor**

### More than just Javascript code

One of the most powerful features of Webpack is to be able to also handle other file types. Such as CSS.

Add a `<div>` to your HTML file and with CSS give it some width, height and background color.

*Remember to require the CSS file from the html*

Make sure everything is working.

Once everything is working, remove the `<link>` tag that requires the CSS file. We will be managing CSS files with Webpack.

In order to require it, just add:

*In src/app.js*

```Javascript
import '../style.css';
```

The path needs to be the relative path where the CSS file is located. Just like requiring any JS file.

If you run the build command now it will break. Go ahead and try it.

We need to add one more Loader.

Add the following loader to the array of rules in `webpack.config.js`:

```Javascript
{
  test: /\.css$/,
  exclude: /(node_modules)/,
  loaders: ['style-loader', 'css-loader']
},
```

CSS loader are weird. There is one file to handle the CSS code and another one to inject it to the html page. Style Loader and CSS Loader.

Go ahead and install them `$ npm install --save-dev style-loader css-loader`.

Now you can run your build command and everything should be working.

Go and check the Elements tab in the console browser. You should see a few `style` tags added. That was webpack.

### One more loader.

Just to give you a sense of the power of webpack, we will be also managing images from it.

Instead of a `background-color` go ahead and add some image.

You need to copy an image in the folder and use it in the CSS file: `background-image: url('./fry.jpg');`.

As usual, try to run the build command and see it fail.

We need one last loader: URL Loader.

- Install it: `$ npm install --save-dev url-loader`.
- Use it:

  ```javascript
  {
    test: /\.jpg/,
    exclude: /(node_modules)/,
    loader: 'url-loader'
  }
  ```

Go ahead and try now.

*Check for the image extension*

### Webpack Dev Server

It's very annoying to have to run the build command every time you make a change.

Webpack Dev Server comes to the rescue. With the Webpack Development Server the build command will be run every time you make a change. You will need only to refresh the page.

You need to make a few changes to use this server.

- Install it `$ npm install --save-dev webpack-dev-server@2.9.4`
- Set `publicPath` for the output file:

  ```javascript
    output: {
      filename: 'app.bundle.js',
      path: path.resolve(__dirname, 'dist'),
      publicPath: '/dist/'
    },
  ```

- Create the proper `npm` script:

  ```javascript
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack",
    "start:dev": "webpack-dev-server"
  },
  ```

Now if you run the command `npm run start:dev` you will initialize a server.

Instead of using `http-server` you will be using the Webpack Dev Server to serve the files.

Go to `localhost:8080` to check the page.

Make a change in your code.

Refresh to page to make sure it's there.

### Conclusions

Congratulations! You created your first front end development environment using the latest technologies.

- We learned how to use `node` for front end Development.
- How to use Webpack to bundle our front end assets.
- Using different Webpack Loaders for different purposes.
- Use Webpack Dev Server for better development experience.
