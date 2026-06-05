class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"Customer(name={self.name}, email={self.email})"
    
    def update_email(self, new_email: str) -> None:
        print(f"Updating email for {self.name} from {self.email} to {new_email}")
        self.email = new_email
    