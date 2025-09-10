#Ask for item price
#Quantity
#if cost above 100, apply discount of 10%

price = eval(input("Input Item Price --->"))
qty = eval(input("Input Item Quantity --->"))

cost = price * qty
discount = cost * 0.10 

if cost > 100:
	final_cost = cost - discount 
	print("Discount price is ",final_cost)

else:
	print("No discount applied,cost is ", cost)