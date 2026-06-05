const NotificationFactory = require('./notificationFactory');

const email = NotificationFactory.createNotification('email');
email.send("Welcome User!");
console.log("-------------");


const sms = NotificationFactory.createNotification('sms');
sms.send("OTP: 1234");

const push = NotificationFactory.createNotification('push');
push.send("You have a new message");