# Webpack

There are many tools that we could use for Front End Development.

However, Webpack has become one of the most popular.

### What is Webpack?

Webpack is a module bundler.

```
Webpack takes modules with dependencies and generates static assets representing those modules.
```

This means that Webpack will take a bunch of Javascript files -not just JS files, more on this later- and create a single javascript file. Then, that new created file will be the one required in the html.

### Why use Webpack

Webpack allows us to use `npm` dependencies in our Javascript code. Webpack will ship the code of those dependencies for use. No need to download and add a `script` tag in our html.

Webpack also allows us to use `compilers` such as [Babel](https://babeljs.io/) that allow us to write new Javascript regardless of the browser support.

The created file can also be easily minified and uglified for production purposes.

*Production means the code that the final user will use. Not just during development.*

It is very common on Production Mode, to compress as much as possible your code. No white spaces, nor long variable names, etc. However, all that is done automatically by some tool. In this case, Webpack takes care of it.

These are the main reasons on why choose Webpack.
