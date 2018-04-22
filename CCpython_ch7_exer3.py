##7-8:
sandwich_orders = {}
condition = True 
while condition == True:
	name = input("\nPlease enter your name: ")
	print("Hi " + name)
	sandwich = input(", what sandwich would you like today? ")
	sandwich_orders[name] = sandwich
	print("Your " + sandwich + " will be out sortly.")
	response = input("Would you like to order another item from our menu? (yes/ no")
	if response == "no":
		condition = False
		
finished_sandwiches = {}
for name, sandwich in sandwich_orders.items():
	finished_sandwiches[name] = sandwich 
	print("Hi " + name + " your " + sandwich + " sandwich is ready to be picked up!")
print(finished_sandwiches)

##7-9:
sandwich_orders = {}
condition = True 
while condition == True:
	name = input("\nPlease enter your name: ")
	print("Hi " + name)
	sandwich = input(", what sandwich would you like today? ")
	if sandwich == "pastrami":
		print("Sorry " + name + " we are out of pastrami.")
	else:
		print("Your " + sandwich + " will be out sortly.")
	sandwich_orders[name] = sandwich
	response = input("Would you like to order another item from our menu? (yes/ no")
	if response == "no":
		condition = False
#This time I will fill the input() orders with some pastrami sandwiches.

#dictionary while loop experiment:
sandwich_new = []
for sandwich in sandwich_orders.values():
	if sandwich == "pastrami":
		print("pastrami detected:")
	else:
		sandwich_new.append(sandwich)
print(sandwich_new)
#I still don't know how to remove the pastrami orders as well as the keys from
#the dictionary through a for or while loop. will need to look into alternatives.

##7-10:
poll_active = True# The only way I can think of at the moment is writing this
#command as conditional while loop. Will need to learn the len() equivalent for
#dictionaries before I can write an active while loop.
responses = {}
while poll_active:
	name = input("What is your name? ")
	response = input("Where would you like to visit? ")
	responses[name] = response
	repeat = input("Would you like to let another person respond (yes/ no) ")
	if repeat == "no":
		poll_active = False

for name, response in responses.items():
	print(name.title() + " would like to go to " + response.title() + ".")

#this command runs perfectly. Needed to use the example from page 130. 



