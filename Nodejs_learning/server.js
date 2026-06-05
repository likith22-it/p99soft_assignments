const http = require('http');

const hostname = '127.0.0.1'; // Localhost
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  const url = req.url;
  if (url==="/"){
    res.write("welcome to the homepage!");
  }

  if (url =="/about"){
    res.write("welcome to the about page!");
  }
});

// 4. Start the server
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

