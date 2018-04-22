##8-12:
def build_sandwich(*fixings):
	"""Prints the fixings that a customer wants on his sandwich"""
	print("\nYou have just ordered a sandwich with: ")
	for fixing in fixings:
		print("-" + fixing)

build_sandwich("roast beef","turkey","swiss cheese","pineapple","olives")
build_sandwich("roast beef")
build_sandwich("BLT","turkey","ham")

##8-13:
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	profile = {}
	profile["first_name"] = first 
	profile["last_name"] = last 
	for key, value in user_info.items():
		profile[key] = value
	return profile

mason_profile = build_profile("mason", "karsevar", location = "Spokane", hobbies = "hiking", interests = "R programming")
print(mason_profile)

def car(manu, model, col, **additional_info):
	"""Builds a dictionary containing everything about a particular car 
	of interest"""
	car_format = {}
	car_format["manufacturer"] = manu
	car_format["make"] = model
	car_format["color"] = col
	for key, value in additional_info.items():
		car_format[key] = value 
	return car_format

subaru = car("subaru","outlander","green", year = 2005,
			 vin = 3340555, owner = "alice Karsevar")
print(subaru)

subaru = car("subaru","outlander","green", tow_package = True)
print(subaru)


