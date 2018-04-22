##7-1:
prompt = "Welcome to Car Rental Masters! the first fully automated car rantal service. "
prompt += "What make or model would you like to rent today? "
rental_car = input(prompt)

print("Let's see if we currently have a " + rental_car +" in our inventory.")

##7-2:
table_number = input("How many people are you expecting in your party? ")
table_number = int(table_number)
if table_number > 8:
	print("Please wait for a couple of minutes as we get your table ready. ")
else: 
	print("Your table is ready!")
#Sweet this line of code actually works!!! I can now create shitty interactive
#programs.

##7-3:
number = input("Think of a number! ")
number = int(number)
if number % 10 == 0:
	print("This number is a multiple of ten.")
else:
	print("This number is not a multiple of ten.")