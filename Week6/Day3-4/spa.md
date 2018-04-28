# Single Page Applications - SPA

From Wikipedia:

```
In an SPA, either all necessary code – HTML, JavaScript, and CSS – is retrieved with a single page load
```

```
The appropriate resources are dynamically loaded and added to the page as necessary, usually in response to user actions.
```

```
The page does not reload at any point in the process, nor does control transfer to another page
```

```
Interaction with the single page application often involves dynamic communication with the web server behind the scenes.
```

### Single Page Load

SPA load all the necessary code with one single page load.

This means that we only ask for 1 HTML page. Which itself requires all the CSS and JS files needed.

This `body` of this single HTML usually looks something like this:

```HTML
<div id="app"></div>
```

Then everything is created and appended with JS.

### Data

The data needed to render the website is retrieved dynamically through requests from the browser.

Using `fetch` or `AJAX` javascript will request for the data that will then get rendered as HTML.

### Navigation

In a SPA there is no full page reload when navigating in the website.

Javascript will take care of removing the HTML elements and create the new ones on the fly.

### Fetching

In SPA there is a heavy communication with the browser using JS.

Requests from the browser to the server API are common.

It's the only way to ensure that the actions of the user are persisted in the Database.
