##8-3:
#Just a little experiment with input() objects and functions.
def make_shirt():
	"""Displays the size and the message of a shirt"""
	print("Hello traveler!!! This is shirt bro.")
	print("The first fully automated, custom shirt supplier.")
	size = input("Please enter what size shirt you want (S/M/L): ")
	message = input("Please enter the message you want printed on the shirt: ")
	print("Ok, your order for a size " + size + " shirt with message")
	print(message + " has been placed into our system. You will recieve your ")
	print("apparel in two days.")
#This function actually works just fine.

def make_shirt2(message, size):
	"""Displays the size and the message of a shirt"""
	print("Your order for a size " + size + " shirt with the message")
	print(message + " has been placed within our system.")

size = "Medium"
message = "Eat me"
make_shirt2(message, size)
make_shirt2(size = size, message = message)

##8-4:
def make_shirt2(message = "I Love Python", size = "Large"):
	"""Displays the size and the message of a shirt"""
	print("Your order for a size " + size + " shirt with the message")
	print(message + " has been placed within our system.")

make_shirt2()
make_shirt2(size = "medium")
make_shirt2(size = "Small", message = "Hi Mister")

##8-5:
#A little experiment with a for loop within a function.
cities = {
	"iceland": "reyjavik",
	"united states": "seattle",
	"south africa": "cape town",
	"mexico": "mexico city",
	"united states": "san francisco",
	"philippines": "manila",
}

def describe_cities(cities):
	"""Takes a dictionary of cities and countries and prints the city 
	with the country of origin"""
	for country, city in cities.items():
		if country == "united states":
			print("\n" + city.title() + " is located in the " + country.title() + ".")
		else:
			print("\n" + city.title() + " is located in " + country.title() + ".")

describe_cities(cities)

#Actual solution:
def describe_city(city, country):
	"""Displays a statement with a city and its corresponding country"""
	print(city.title() + " is located in " + country.title() + ".")

describe_city(city = "seattle", country = "united states")

#Default example:
def describe_city(city, country = "united states"):
	"""Displays a statement with a city and its corresponding country"""
	if country == "united states":
		print("\n" + city.title() + " is located in the " + country.title() + ".")
	else: 
		print("\n" + city.title() + " is located in " + country.title() + ".")

describe_city(city = "new york")
describe_city(city = "salt lake city")
describe_city(city = "tokyo", country = "japan")



