# Custom Cart System
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def __len__(self):
        return len(self.items)

    def total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

cart = Cart()

for i in range(2):
    name = input("Enter product name: ")
    price = int(input("Enter price: "))

    p = Product(name, price)
    cart.add_item(p)

print("\nItems in cart:", len(cart))
print("Total price:", cart.total())