#CAP for shopping billing system , program should , 1.ask the customer name 2.Ask the how many items customer purchered 
#use a loop ,-Enter items name -enter item prices -enter item quantities 
#4. calculate the amount for each items .
#5.calculate the total bill 
#apply discount : 10% if bill amount is greater than 5000 ,5%greater 3000 
""" display 
customer name , total amount 
discount , final payable amount """

customer_name=str(input ("Enter customer name "))
total_items=int(input("Enter total items that customer purchased"))
total=0
for items in range(total_items):
    items_name=input("Enter items")
   # items_price=float(input("items price"))
    items_price = float(input("Enter item price: "))
    items_quantity=int(input("Enter total quantity"))
    total += items_price *items_quantity
discount=0
if total>5000:
    discount= total*0.1
elif total>3000:
    discount=total*0.05
final_amount=total-discount
print(f"Customer name:{customer_name}")
print(f"total amount:{total}")
print(f"Discount:{discount}")
print(f"final payable amount: {final_amount}")

