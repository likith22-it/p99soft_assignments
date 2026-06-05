class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __str__(self):
        return str(self.value)
    
num1 = Number(10)
num2 = Number(5)    
result_add = num1 + num2
result_sub = num1 - num2
print(result_add)  # Output: 15
print(result_sub)  # Output: 5  