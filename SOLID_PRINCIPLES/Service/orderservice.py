
from .Customer import Customer
from .Cart import Cart

class OrderService:

    def create_order(self, cart: Cart, customer: Customer):
        print(f"Creating order for customer: {customer.name} with items: {cart.items}")
        return {"status": "success"}
    
    def cancel_order(self, order_id: int):
        print(f"Cancelling order with ID: {order_id}")
        return {"status": "cancelled"}
    
    def get_order_status(self, order_id: int):
        print(f"Getting status for order ID: {order_id}")
        return {"status": "pending"}
    
    def update_order(self,order_id: int, cart: Cart):
        print(f"Updating order ID: {order_id} with new items: {cart.items}")
        return {"status": "updated"}


        