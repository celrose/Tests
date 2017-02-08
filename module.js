var http = require('http');

var server = http.createServer(function(request, response) {
	console.log('request');
	response.write('CELROSE');
	response.end();
});


server.listen(3000);
//console.log('hi');