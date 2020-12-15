const spawn = require('child_process').spawn;

const process = spawn('python', ['/house_price_predictions.py']);


process.stdout.on('data', data=>{
  console.log(data.toString());

});


/*var PythonShell = require('python-shell');

PythonShell.run('house_price_predictions.py', function (err) {
  if (err) throw err;
  console.log('finished');
});*/