#Inventory Management (Basic)
inventory = {}

print("---- Inventory System ----")

for i in range(3):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    inventory[item] = quantity

print("\n--- Inventory ---")

for item, qty in inventory.items():
    print(item, ":", qty)

# Find item with highest quantity
max_item = None
max_qty = 0

for item, qty in inventory.items():
    if qty > max_qty:
        max_qty = qty
        max_item = item

print("\nHighest stock item:", max_item, "-", max_qty)