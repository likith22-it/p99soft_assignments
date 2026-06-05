class Discount:
    def apply_discount(self, order_id: int, discount_code: str) -> dict:
        print(f"Applying discount code: {discount_code} to order ID: {order_id}")
        return {"status": "discount applied", "discount_amount": 10}
    