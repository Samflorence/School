name = input("what is your name? ")
fare = eval(input("how much is your fare fee? "))
student = input("are u are student rn? (yes / no) ")
if student == "yes":
	discount = fare * 0.40
	new_fare = fare - discount
	print("hi ", name)
	print("your discount is ", discount)
	print("your fare is ", new_fare)