var request = require('request');
var cheerio = require("cheerio");
var loki = require("lokijs");
var lfsa = require('lokijs/src/loki-fs-structured-adapter.js');

var db = new loki('sandbox.db', { 
  adapter : new lfsa(),
  autoload: true,
  autoloadCallback : databaseInitialize, // will be called once DB is loaded
  autosave: true, 
  autosaveInterval: 4000 // save every 4000ms (4s)
});



function databaseInitialize() {
    console.log("Database is initialized, let's start working...");

    // get or create presidents collection
    var webLinks = db.getCollection('links');

    if (webLinks === null) {
        webLinks = db.addCollection('links');
      }
    homeLink = 'http://www.dickinson.edu/'
    myWebCrawler(homeLink, webLinks)    
}
console.log('yoyoyo, ma duuuuude')


// var webLinks = db.addCollection('webLinks');

// webLinks.insert({link:'http://www.dickinson.edu'})

// var homeLink = 'http://www.dickinson.edu'

// console.log(webLinks)

// var homepageHTML

function myWebCrawler(homeLink, webLinks) {
    // console.log(homeLink)
    // console.log(webLinks)
    request(homeLink, function (error, response, body) {
        // console.log('error:', error); // Print the error if one occurred
        // console.log('status Code:', response && response.statusCode); // Print the response status code if a response was received
        // console.log('body:', body); // Print the HTML for the Google homepage.
        var $ = cheerio.load(body)
        // console.log($("a"))
        var add = false
        var aLinks = $("a")
        // console.log(aLinks.length);
        // console.log(aLinks)
        // console.log("the web link", webLinks)
        webLinks.insert({ 'link': homeLink })
        //TO BE PUT INTO A WHILE LOOP LATER
        var data = webLinks.find({ 'link': homeLink });
        // console.log("the data", data)
        for (var k = 0; k <= webLinks.data.length - 1; k++) {
            // console.log("the date from the for loop", data[k].link)
            // console.log(webLinks.data[k].link)
            // console.log('yoooooooooooooo')
            // console.log(data[k].link)
            request(webLinks.data[k].link, function (error, response, body) {
                console.log('HOWDOYOUTURNTHISON')
                // console.log(webLinks.data.length - 1)
                var $ = cheerio.load(body)
                var aLinks = $("a")
                for (var i = 0; i <= aLinks.length; i++) {
                    if (aLinks[i]) {
                        console.log(aLinks[i].attribs.href)
                        if (aLinks[i].attribs.href!==undefined && aLinks[i].attribs.href.indexOf('dickinson.edu') !== -1 ) {
                            // console.log('second if loop');
                            // console.log(webLinks.data.length)
                            for (var j = 0; j <= webLinks.data.length; j++) {
                                // console.log('-----------------')
                                // console.log(webLinks.data[j])
                                console.log(webLinks.data[j])
                                // console.log('-----------------')
                                if (webLinks.data[j]!==undefined && webLinks.data[j].link && aLinks[i] !== webLinks.data[j].link) {
                                    var add = true
                                }
                                // console.log('outside of break')
                            }
                            console.log(add)
                            if (add === true) {
                                dbObject = { 'link': aLinks[i].attribs.href }
                                webLinks.insert(dbObject)
                                console.log('we made it! yaay!')
                            }
                            add = false
                            // console.log(webLinks)
                            // console.log(db)
                            // db.save()
                            // console.log('savvvveed, baby')
                            console.log(webLinks.data.length - 1)
                        }
                    }
                }
                // console.log(webLinks)
                // console.log('made it')
            })
            // console.log(webLinks)
            // var regex = new RegExp("^\/"+homepageHTML+"\/\d+$", "g");

        };
    });
}

console.log('You made it! Hurray!')