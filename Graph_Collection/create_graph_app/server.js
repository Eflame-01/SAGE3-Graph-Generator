/* server.js creates the server that will display the app */

//init variables needed to create thef server
var express = require('express');
var app = express();
const http = require('http').Server(app);

var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

//init variables needed for writing files onto the page
var fs = require('fs');

//init variables to get the hostname and port
const hostname = '127.0.0.1';
const port = 5000;

//use the app
app.use(express.static(__dirname));

//listen to anything that is using the port
var server = http.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

var writeFile = function(name, file) {
  // write file
  fs.writeFile("./data/" + name, file, function(err){
    if(err){
      console.log(err.message);
    }
    else{
      console.log("We have written " + name + " into our application.");
      //send the name of the file to python in order for python to retrieve the information
    }
  })
};

app.post('/loading', urlencodedParser, function(req, res) {
  console.log(req.body);
  var name = req.body.file;
  var file = req.body.data;

  //create the file
  writeFile(name, file);
  res.sendFile(__dirname + "/loading.html");
});