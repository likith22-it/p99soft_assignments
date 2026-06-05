const logger1 = require('./logger');
const logger2 = require('./logger');

logger1.log("Application started");

console.log(logger1 === logger2); // true