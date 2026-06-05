const fs = require('fs');
const path = require('path');

class Logger {
    constructor() {
        if (Logger.instance) {
            print("Using existing Logger instance");
            print(Logger.instance);
            return Logger.instance;
        }

        this.logFile = path.join(__dirname, 'app.log');

        Logger.instance = this;
    }

    log(message) {
        const logMessage = `[${new Date().toISOString()}] ${message}\n`;

        // Write to console
        console.log(logMessage);

        // Write to file
        fs.appendFileSync(this.logFile, logMessage);
    }
}

// Export single instance
module.exports = new Logger();