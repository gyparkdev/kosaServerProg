let express = require("express");

let app = express();
app.listen(8888); // 클라이언트 요청에 대기할 때 listen
console.log("Server is running on port 8888");

// url, 파라미터값
app.get("/", (req, res)=> {
    res.send("Hello World");
});

var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(bodyParser.text());

app.use('/calculator', express.static(__dirname + '/static'));

app.post("/calc", (req, res)=> {
    var data = req.body;
    console.log(data);
    var result = eval(data);
    console.log(result)
    res.send(String(result));
});
