// http://www.dickinson.edu


console.log('---------------------THIS IS AN EXAMPLE OF THE REQUEST PACKAGE---------------------')
var request = require('request');
request('http://www.dickinson.edu', function (error, response, body) {
//   console.log('error:', error); // Print the error if one occurred
//   console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
//   console.log('body:', body); // Print the HTML for the Google homepage.
});

console.log('---------------------THIS IS AN EXAMPLE OF THE CHEERIO PACKAGE--------------------')
var cheerio = require("cheerio");

// load a fake HTML
var $ = cheerio.load(`
  <html>
    <head>
    </head>
    <body>
      <h1>Hello world</h1>
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

console.log('---------------------THIS IS AN EXAMPLE OF THE QUEUE MODEL--------------------')

// var async = require('async');

// var worker = function(number, callback) {
//   console.log("Got number " + number);

//   // create two more numbers from it
//   if (number < 32) {
//     queue.push(number*2);
//     queue.push(number*2+1);
//   }

//   // timeout of 1 second
//   setTimeout(function() {
//     // call callback to signal that we are done
//     callback();
//   }, 1000);
// }

// // create a queue, with worker function "worker", and allow 2 workers to operate in parallel.
// var queue = async.queue(worker, 2);

// lets add initial number to the queue & get the ball rolling
// queue.push(1);

// Output will be
//    Got number 1
//    Got number 2
// (pause for approx 1 sec)   
//    Got number 3
//    Got number 4
// (pause for approx 1 sec)
//    ...
// --> This is because we have 2 workers that can work at the same time
// --> & each worker needs approximately 1 sec to execute


var loki = require("lokijs");
var db = new loki('my-db');

var presidents = db.addCollection('presidents');

presidents.insert({name:'George H. W. Bush', year: 1989})
presidents.insert({name:'Bill Clinton', year: 1993})
presidents.insert({name:'George W. Bush', year: 2001})
presidents.insert({name:'Barack Obama', year: 2009})
presidents.insert({name:'Donald Trump', year: 2017})

// Find all presidents that were inaugurated after year 2000
var after2000 = presidents.find({
  year: {
    $gt: 2000
  } 
});

console.log("All presidents inaugurated after 2000");
for (var president of after2000) {
  console.log(" == " + president.name);
}

// Find all Presidents that have "Bush" in their name
// (attention: string search is case sensitive, i.e. Bush != bush)
var bushes = presidents.find({
  name: {
    $contains: "Bush"
  }
})

console.log("All presidents named Bush");
for (var president of bushes) {
  console.log(" == " + president.name);
}

// Attention! You can also insert a certain value 2x:
// --> there will be two DB entries called "Donald Trump" in the database after calling the next line
presidents.insert({name:'Donald Trump', year: 2017})
var trumps = presidents.find({
  name: {
    $contains: "Trump"
  }
})

console.log("All presidents named Trump");
for (var president of trumps) {
  console.log(" == " + president.name);
}

// Use the following to update an entry
var existingRecord = presidents.findOne({name: "Donald Trump"})
if (existingRecord) {
  existingRecord.name = "Orang Utan";
  presidents.update(existingRecord);
}

var newRecord = presidents.findOne({name: "Orang Utan"});
console.log("Successfully renamed " + newRecord.name);
