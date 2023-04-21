const http = require('http'); //바뀌지 않을 값. 내장된 http 모듈이 있음.

http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
}).listen(7777);