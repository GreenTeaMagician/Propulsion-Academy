
var request = require('request');

request('https://www.imdb.com', function (error, response, body) {
    console.log('error:', error); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    console.log('body:', body); // Print the HTML for the Google homepage.
});
// request('http://google.com/doodle.png').pipe(fs.createWriteStream('doodle.png'))