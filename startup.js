var express = require('express');
var app = express();
const port = 3000; 
 

app.use(express.static(__dirname + '/index.html'));
app.use(express.static(__dirname));

/*app.get('/house', (req, res) => {
  res.sendFile(__dirname + '/house_report.html')
  // Note: __dirname is the current directory you're in. Try logging it and see what you get!
  // Mine was '/Users/zellwk/Projects/demo-repos/crud-express-mongo' for this app.
*/

const {spawn} = require('child_process'); 
app.get('/house', (req, res) => {
 
  var dataToSend;
  // spawn new child process to call the python script
  const python = spawn('python', ['house_price_predictions.py']);
  // collect data from script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataToSend = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  python.on('close', (code) => {
  console.log(`child process close all stdio with code ${code}`);
  // send data to browser
  res.send(dataToSend)
 });

})  

 
console.log(`App listening at http://localhost:${port}`);
app.listen(port);
