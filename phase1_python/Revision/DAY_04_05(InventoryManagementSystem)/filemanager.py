# File operations
from models import Product

def save_to_file(products):
    with open("inventory.txt", "w") as file:
        for p in products:
            file.write(f"{p.name},{p.quantity},{p.price}\n")

    print("Data saved to file")


def load_from_file():
    products = []

    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                name, qty, price = line.strip().split(",")
                products.append(Product(name, int(qty), float(price)))

    except FileNotFoundError:
        print("No saved data found")

    return products