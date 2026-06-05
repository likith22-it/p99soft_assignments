const express = require('express');
const http= require('http');
const app = express();
const port = 3000;  
app.use(express.json());   // for JSON data
app.use(express.urlencoded({ extended: true })); 
try{
app.get('/', (req, res) => {
    res.send('Hello, World!');
});
}catch(err){
    res.status(400).send("request error"); }

try{
app.post('/submit', (req, res) => {
    res.send('Data received!');
}); }
catch(err){
    res.status(400).send("request error"); }


app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});