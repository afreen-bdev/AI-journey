# Main application

from services import add_product, view_products, products
from filemanager import save_to_file, load_from_file

# Load existing data
products.extend(load_from_file())

while True:
    print("\n--- Inventory System ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Save Data")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            view_products()
        elif choice == 3:
            save_to_file(products)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid number")