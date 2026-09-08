# week 2 Assignment - Simple Bill Calculator
# ask user for inputs
price = float(input("Enter price of one item:"))
quantity = int(input("Enter quantity:"))
# Calculate total
total = price * quantity
# print friendly summary using f-string
print(f"\n---Bill Summary ---")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
print("Thank you for shopping!")