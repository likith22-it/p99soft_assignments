from typing import List, Dict

class PricingService:
    def calculate_price(self, items: List[Dict]) -> float:
        total_price = sum(item['price'] for item in items)
        print(f"Calculated total price: {total_price} for items: {items}")
        return total_price
    
    def calculate_tax(self, total_price: float) -> float:
        tax = total_price * 0.1  # Assuming a fixed tax rate of 10%
        print(f"Calculated tax: {tax} for total price: {total_price}")
        return tax
    
    def calculate_delivery_charge(self, total_price: float) -> float:
        delivery_charge = 5.0 if total_price < 50 else 0.0  
        print(f"Calculated delivery charge: {delivery_charge} for total price: {total_price}")
        return delivery_charge
    