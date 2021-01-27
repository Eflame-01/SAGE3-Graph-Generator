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
const port = 3001;

//init variables needed to interact with python code
const spawn = require("child_process").spawn;
const pythonProcess = spawn('python3', ["dataCollection.py"])

//use the app
app.use(express.static(__dirname));

//listen to anything that is using the port
var server = http.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

//test code checking interaction with python code works
pythonProcess.stdout.on('data', (data) => {
  mystr = data.toString();
  myjson = JSON.parse(mystr)

  //console.log(myjson.Data)
})

var writeFile = function(file) {
  // write file
  fs.writeFile("./data/data_information.txt", file, function(err){
    if(err){
      console.log(err.message);
    }
    else{
      console.log("this is when we write the data and send it to our files.");
    }
  })
};

app.post('/', urlencodedParser, function(req, res) {
  console.log(req.body);
  res.sendStatus(200);
  var file = req.body.file;

  //if we get here, then we can create the file
  writeFile(file);
});