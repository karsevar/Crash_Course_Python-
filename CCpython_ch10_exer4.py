##10-11:
def favorite_number():
	"""Stores the user inputted favorite number using a json file"""
	filename = "favorite_store.json"
	favorite = input("What is your favorite number? ")
	with open(filename, "w") as f_obj:
		json.dump(favorite, f_obj)
		print("Your favorite number will be remembered within our system.")

def favorite_read():
	filename = "favorite_store.json"
	"""Reads back favorite number json into the python session"""
	with open(filename) as f_obj:
		favorite = json.load(f_obj)
		print("your favorite number is " + str(favorite))

##10-12:
def favorite_number():
	import json
	"""Stores the user inputted favorite number using a json file"""
	filename = "favorite_store.json"
	favorite = input("What is your favorite number? ")
	with open(filename, "w") as f_obj:
		json.dump(favorite, f_obj)
		print("Your favorite number will be remembered within our system.")

def favorite_read():
	import json
	filename = "favorite_store.json"
	"""Reads back favorite number json into the python session"""
	try:
		with open(filename) as f_obj:
			favorite = json.load(f_obj)
			print("your favorite number is " + str(favorite))
	except FileNotFoundError:
		favorite = favorite_number()

#These two functions work perfectly together!!! 

##10-13:
import json

def get_stored_username():
	"""Get stored username if available."""
	filename = "username.json"
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""prompt for a new username."""
	username = input("What is your name? ")
	filename = "username.json"
	with open(filename, "w") as f_obj:
		json.dump(username, f_obj)
	return username 

def greet_user():
	"""greet the user by name."""
	username = get_stored_username()
	if username:
		answer = input("Your username is " + username + ", is this correct? (yes/no)")
		if answer == "yes":
			print("Welcome back, " + username)
		else: 
			username = get_new_username() 
	else: 
		username = get_new_username()

greet_user()
#Solution partially obtained from the book website.

 