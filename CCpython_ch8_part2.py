##Passing a list:
def greet_users(names):
	"""print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ["hannah","ty","margot"]
greet_users(usernames)

##Modifying a list in a function:
#This example will only move the contents of a list into another list:
unprinted_designs = ["iphone case","robot pendant","dodecahedron"]
completed_designs = []
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("Print model: " + current_design)
	completed_designs.append(current_design)

print("\nThe following models have been printed.")
for completed_design in completed_designs:
	print(completed_design)

def print_models(unprinted_designs, completed_models):
	"""
	simulate printing each design, until none are left. 
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Print model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed"""
	print("\nThe following models have been printed")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ["iphone case","robot pendant","dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

##Preventing a function from modifying a list:
print_models(unprinted_designs[:], completed_models)#In this function call 
#used the slice syntax to make a copy of the unprinted_designs list. 

##Passing an arbitrary number of arugments:
def make_pizza(*toppings):
	"""print the list of toppings that have been requested."""
	print(toppings)

make_pizza("pepperoni")
make_pizza("mushroom","green peppers","extra cheese")
#the * syntax tells python to make an empty tuple called toppings and pack
#whatever values it recieves into this tuple.

def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

##Mixing positional and arbitrary arguments:
#When using the * argument syntax make sure that the argument is positioned at 
#the end of the function call. As a means to decrease confusion within the
#function assembly. 
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, "pepperoni")
make_pizza(12, "mushroom","pepperoni","extra cheese")

##Using arbitrary keyword arguments:
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	profile = {}
	profile["first_name"] = first 
	profile["last_name"] = last 
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile("albert", "einstein",
							location = "princeton",
							field = "physics")
print(user_profile)

##Storing your functions in modules:
##importing an entire module:
#(important) A module is a file ending in .py that contains the code you 
#want to import into your program. 

#Ok just created a new file called pizza.py (let's see if this works without)
#configuring my work directory).
import pizza 


