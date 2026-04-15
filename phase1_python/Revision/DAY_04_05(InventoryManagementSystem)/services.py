# Business logic
from models import Product

products = []

def add_product():
    try:
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        product = Product(name, quantity, price)
        products.append(product)

        print("Product added successfully!")

    except ValueError:
        print("Invalid input!")


def view_products():
    if not products:
        print("No products available")
        return

    print("\n--- Product List ---")
    for p in products:
        print(p)