/*
console.log(`house js started running `);
const spawn = require('child_process').spawn;

const process = spawn('python', ['./house_price_predictions.py']);

process.stdout.on('data', (data) =>{ 
  //console.log("hi");
  console.log(data.toString()); 
 });
 */

 
 
/*
let {PythonShell} = require('python-shell');

PythonShell.run('house_price_predictions.py', function (err) {
  if (err) throw err;
  console.log('finished');
});

*/

const express = require('express');
const {spawn} = require('child_process');
const app = express().Router();
app.get('/', (req, res) => {
 
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

