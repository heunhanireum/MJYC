// const express = require('express')
// const serverStatic = require('serve-static')
// const path = require('path')

// const app = express()
// const port = process.env.PORT || 3000

// // SERVES FILES from our dist directory which now contains out index.html
// app.use('/', serverStatic(path.join(__dirname, '/dist')))
// app.listen(port)
// console.log('Listening on port:' + port)
// // app.get('/', (req, res) => res.send('Hello World!'))
// // app.listen(port, () => console.log(`Example app listening on port port!`))


const express = require('express');
const path = require('path');
const history = require('connect-history-api-fallback');

const app = express();

const staticFileMiddleware = express.static(path.join(__dirname + '/dist'));

app.use(staticFileMiddleware);
app.use(history({
  disableDotRule: true,
  verbose: true
}));
app.use(staticFileMiddleware);

app.get('/', function (req, res) {
  res.render(path.join(__dirname + '/dist/index.html'));
});

var server = app.listen(process.env.PORT || 8080, function () {
  var port = server.address().port;
  console.log("App now running on port", port);
});