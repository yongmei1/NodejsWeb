
const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();

router.get('/',function(req,res){
  res.sendFile(path.resolve(__dirname+'/express/login.html'));
  //__dirname : It will resolve to your project folder.
});

router.get('/home',function(req,res){
  res.sendFile(path.join(__dirname+'/home.html'));
});

router.get('/run_report',function(req,res){
  res.sendFile(path.join(__dirname+'/run_report.html'));
});

router.get('/viewclients',function(req,res){
    res.sendFile(path.join(__dirname+'/viewclients.html'));
  });

//add the router
app.use('/', router);
app.listen(process.env.port || 3000);

console.log('Running at Port 3000');
 