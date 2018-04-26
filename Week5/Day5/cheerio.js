var cheerio = require("cheerio");

// load a fake HTML
var $ = cheerio.load(`
  <html>
    <head>
    </head>
    <body>
    <img src="This is the first src" />
      <h1>Hello world
      This is Michal
      I have infiltrated your defenses
      Your power is mine now. Muahahahaha</h1>
      <img src="This is a src" />
      <img src="This is another src" />

    </body>
  </html>
`)

// get all h1
var h1 = $("h1")
console.log(h1[0].firstChild.data); // prints "Hello world"

// get all img
var img = $("img")
for (var i=0; i < img.length; i++) {
  var el = img[i];

  console.log(el.attribs.src) 
}

// prints "This is a src"
// prints "This is another src"
