from Service.Cart import Cart
from Service.Customer import Customer
from Service.orderservice import OrderService
from Service.pricingservice import PricingService
from Service.Discount import Discount
from Service.Deliverystatus import DeliveryStatus
from Service.paymentresult import PaymentResult


def main() -> None:
    customer = Customer("Alice", "alice@example.com")
    cart = Cart()
    cart.add_item({"name": "Book", "price": 15.99})
    cart.add_item({"name": "Pen", "price": 2.50})

    pricing_service = PricingService()
    total_price = pricing_service.calculate_price(cart.items)
    tax = pricing_service.calculate_tax(total_price)
    delivery_charge = pricing_service.calculate_delivery_charge(total_price)

    order_service = OrderService()
    order_response = order_service.create_order(cart, customer)
    print(f"Order response: {order_response}")

    discount = Discount()
    discount_response = discount.apply_discount(1, "SPRING10")
    print(f"Discount response: {discount_response}")

    payment_result = PaymentResult()
    payment_response = payment_result.process_payment(
        1,
        {
            "method": "card",
            "amount": total_price + tax + delivery_charge - discount_response.get("discount_amount", 0),
        },
    )
    print(f"Payment response: {payment_response}")

    delivery_status = DeliveryStatus()
    delivery_update = delivery_status.update_delivery_status(1, "shipped")
    print(f"Delivery update: {delivery_update}")

    order_status = order_service.get_order_status(1)
    print(f"Order status: {order_status}")


if __name__ == "__main__":
    main()
