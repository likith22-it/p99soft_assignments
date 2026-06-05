class DeliveryStatus:
    def update_delivery_status(self, order_id: int, status: str) -> dict:
        print(f"Updating delivery status for order ID: {order_id} to: {status}")
        return {"status": "delivery status updated", "order_id": order_id, "new_status": status}
    
    def delivery_status(self, order_id: int) -> dict:
        print(f"Getting delivery status for order ID: {order_id}")
        return {"status": "in transit", "order_id": order_id}
    
    def pending_status(self, order_id: int) -> dict:
        print(f"Getting pending status for order ID: {order_id}")
        return {"status": "pending", "order_id": order_id}
    