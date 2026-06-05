import { calculateTotal } from "./pricingService";
import { processPayment } from "../payments/paymentFactory";

export function createOrder(user, item, qty, payment) {
  processPayment(payment);

  const total = calculateTotal(item, qty, user);

  return {
    id: Date.now(),
    user,
    item,
    qty,
    total,
    status: "PLACED"
  };
}