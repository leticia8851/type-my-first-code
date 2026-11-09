from os import name


print("Welcome TO CATUC SHOP")
print("THANKS FOR YOUR PATRONAGE")
num_items = int(input("Enter the number of items purchased: "))
items = []
subtotal = 0
# Collect details of each item
for i in range(1, num_items + 1):
    print(f"\nITEMS {i}")
    items_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))
    total_price = quantity * unit_price
    #Store item details
    items.append([items_name, quantity, unit_price, total_price]) 
    subtotal += total_price
# Calculate discount
if subtotal >= 10000:
    discount_rate = 0.30
elif num_items > 5 and subtotal > 4000:
    discount_rate = 0.15
elif subtotal > 5000:
    discount_rate = 0.10
else:
    discount_rate = 0
discount = subtotal * discount_rate
total_cost = subtotal - discount
# Display receipt
print("=" * 75)
print("=====================================================")
print("                 CATUC SHOP RECEIPT") 
print("=" * 75)
print("'S/N   Description        Quantity    Unit Price     Total Price")
print("=" * 75)
# Display each item
for i, item in enumerate(items, start=1):
    name, quantity, unit_price , total_price = item
    print(i,"       ", name, "           ",   quantity,"               ", unit_price,"               ",total_price) 
print("=" * 75)
print(f"Subtotal:                {subtotal:.2f} FCFA")
print(f"Discount rate:                {discount_rate * 100:.0f}%")
print(f"Discount amount:                {discount:.2f} FCFA")
print(f"TOTAL PURCHASE:                {total_cost:.2f} FCFA")
print("=" * 75)
print("          THANK FOR YOURG PATRONAGE!")
print("=" * 75)