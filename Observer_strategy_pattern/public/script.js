// =============================
// STRATEGY PATTERN
// =============================

// Different payment strategies

class CreditCardPayment {
    pay(amount) {
        return `Paid ₹${amount} using Credit Card`;
    }
}

class PayPalPayment {
    pay(amount) {
        return `Paid ₹${amount} using PayPal`;
    }
}

class UpiPayment {
    pay(amount) {
        return `Paid ₹${amount} using UPI`;
    }
}

// Context class

class PaymentContext {

    constructor(strategy) {
        this.strategy = strategy;
    }

    execute(amount) {
        return this.strategy.pay(amount);
    }
}

// UI Function

function makePayment() {

    const amount = document.getElementById("amount").value;
    const method = document.getElementById("paymentMethod").value;

    let strategy;

    if(method === "card") {
        strategy = new CreditCardPayment();
    }
    else if(method === "paypal") {
        strategy = new PayPalPayment();
    }
    else {
        strategy = new UpiPayment();
    }

    const payment = new PaymentContext(strategy);

    const result = payment.execute(amount);

    document.getElementById("paymentResult").innerText = result;
}


// =============================
// OBSERVER PATTERN
// =============================

class YouTubeChannel {

    constructor() {
        this.subscribers = [];
    }

    subscribe(user) {
        this.subscribers.push(user);
        renderSubscribers();
    }

    notify() {

        const notificationDiv =
            document.getElementById("notifications");

        notificationDiv.innerHTML = "";

        this.subscribers.forEach(user => {

            const p = document.createElement("p");

            p.innerText =
                `Hi ${user}! New video uploaded`;

            notificationDiv.appendChild(p);
        });
    }
}

const channel = new YouTubeChannel();

function subscribeUser() {

    const name =
        document.getElementById("subscriberName").value;

    if(name.trim() === "") {
        return;
    }

    channel.subscribe(name);

    document.getElementById("subscriberName").value = "";
}

function uploadVideo() {
    channel.notify();
}

function renderSubscribers() {

    const list =
        document.getElementById("subscriberList");

    list.innerHTML = "<h3>Subscribers:</h3>";

    channel.subscribers.forEach(user => {

        const p = document.createElement("p");

        p.innerText = user;

        list.appendChild(p);
    });
}