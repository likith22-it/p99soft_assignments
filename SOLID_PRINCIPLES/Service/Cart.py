from typing import Any, List


class Cart:
    
    def __init__(self) -> None:
        self.items: List[Any] = []

    def add_item(self, item: Any) -> None:
        self.items.append(item)
        print(f"Added item: {item} to cart. Current items: {self.items}")



    def remove_item(self, item: Any) -> None:
        if item in self.items:
            self.items.remove(item)
            print(f"Removed item: {item} from cart. Current items: {self.items}")
        else:
            print(f"Item: {item} not found in cart. Current items: {self.items}")



    def clear_cart(self) -> None:
        self.items.clear()
        print("Cleared cart. Current items: []")




    def update_item(self, old_item: Any, new_item: Any) -> None:
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item
            print(f"Updated item: {old_item} to {new_item} in cart. Current items: {self.items}")
        else:
            print(f"Item: {old_item} not found in cart. Current items: {self.items}")
