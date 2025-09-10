#Fare Discount Calculator

discount = "yes"

name = input("Input your name --> ")
fare = eval(input("Enter your fare --> "))
student = input("Are you a student?(yes/no) ")


s = fare * 0.25

if student == discount:
	print("Your total fare is ₱",s)

else:
	print("Your total fare is ₱",fare)

