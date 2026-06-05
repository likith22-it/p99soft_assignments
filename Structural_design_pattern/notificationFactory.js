class EmailNotification {
    send(message) {
        console.log(`Email sent: ${message}`);
    }
}

class SMSNotification {
    send(message) {
        console.log(`SMS sent: ${message}`);
    }
}

class PushNotification {
    send(message) {
        console.log(`Push notification sent: ${message}`);
    }
}

class NotificationFactory {
    static createNotification(type) {
        switch (type) {
            case 'email':
                return new EmailNotification();

            case 'sms':
                return new SMSNotification();

            case 'push':
                return new PushNotification();

            default:
                throw new Error("Invalid notification type");
        }
    }
}

module.exports = NotificationFactory;