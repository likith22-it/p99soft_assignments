class PaymentResult:
    def process_payment(self, order_id: int, payment_details: dict) -> dict:
        print(f"Processing payment for order ID: {order_id} with details: {payment_details}")
        return {"status": "payment successful", "transaction_id": "abc123"}
    
    def refund_payment(self, transaction_id: str) -> dict:
        print(f"Refunding payment with transaction ID: {transaction_id}")
        return {"status": "refund successful", "refund_id": "refund123"}
    