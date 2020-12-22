var express = require('express');
var app = express();
const port = 3000; 
 

app.use(express.static(__dirname + '/index.html'));
app.use(express.static(__dirname));

app.post 
 
 
console.log(`App listening at http://localhost:${port}`);
app.listen(port);
