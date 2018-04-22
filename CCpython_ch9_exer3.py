##9-6:
class Restaurant():
	"""A simple restaurant printing class"""

	def __init__(self, name, cuisine):
		"""Initializes name and cuisine"""
		self.name = name 
		self.cuisine = cuisine 

	def describe_restaurant(self):
		"""prints the name and cuisine of the restaurant"""
		print("This restaurant's name is "
			+ self.name.title() + " and it serves " + self.cuisine.title() 
			+ " style cuisine.")

	def open_restaurant(self):
		"""prints whether the restaurant is open"""
		print(self.name.title() + " is now open!")

class IceCreamStand(Restaurant):
	"""
	Represents aspects of a restaurant that sells ice cream products.
	Inherits from Restaurant class.
	"""
	def __init__(self, name, cuisine):
		"""Initialize attributes of the parent class"""
		super().__init__(name, cuisine)

	def ice_cream_flavors(self, flavors):
		"""stores and displays a list of ice cream flavors"""
		self.flavors = flavors
		print("Todays flavors are: ")
		for flavor in flavors:
			print("\t" + flavor)

iscream = IceCreamStand("Ice Cream Monkey","Desert")
iscream.describe_restaurant()
iscream.ice_cream_flavors(["vanilla","pineapple","cherry","salted carmel","orange"])
#Not sure if this is what the author had in mind, but it does store 
#a list of ice cream flavors and prints the list onto the console.

##9-7:
class User2():
	"""Copies and prints inputted user information"""

	def __init__(self, first, last, occupation, location, hobbies):
		"""
		Initializes first and last name and user_profile information.

		"""
		self.first = first 
		self.last = last 
		self.occupation = occupation 
		self.location = location 
		self.hobbies = hobbies 

	def describe_user(self):
		"""Prints user information"""
		print(self.first + " " + self.last + 
			" user profile includes: ")
		print("\t" + self.occupation)
		print("\t" + self.location)
		print("\t" + self.hobbies)

	def greet_user(self):
		"""Gives user a personalized greeting"""
		print("Welcome back " + self.first.title() + " " + self.last.title() + "!")

	def login_attempts(self, attempts):
		"""logs the number of login attempts per day."""
		self.attempts = attempts
		return attempts

	def read_login_attempts(self):
		"""Reads number of login attempts"""
		print("Current number of login attempts: " + str(self.attempts))

	def increment_login_attempts(self):
		"""
		increments login attempts by 1.
		Prints the number of attempts.
		"""
		self.attempts += 1
		print("current number of login attempts: " + str(self.attempts))

	def reset_login_attempts(self):
		"""resets the number of login attempts to zero"""
		self.attempts = 0

class Administrator(User2):
	"""creates sub-category for administrators of a website"""
	def __init__(self, first, last, occupation, location, hobbies):
		"""Initializes all arguments from the User2 parent class"""
		super().__init__(first, last, occupation, location, hobbies)

	def show_privileges(self, privileges):
		"""
		prints and establishes privileges of administrators within
		the website.
		"""
		self.privileges = privileges 
		print("Administrator " + self.first.title() + " " + self.last.title() + 
			" has the following privileges at their disposal: ")
		for privilege in privileges:
			print("\t- " + privilege)

	def greet_user(self):
		"""over writing user greeting from parent class"""
		print("Welcome back administrator " + self.first.title() + " " + 
			 self.last.title() + ".")

admin = Administrator("alice","karsevar","project manager","san francisco","real estate")
admin.describe_user()
admin.greet_user()
admin.show_privileges(["barring users","expelling users","deleting messages"])
#The new administrator methods work perfectly as well as the old parent
#class description methods.

##9-8:
class User2():
	"""Copies and prints inputted user information"""

	def __init__(self, first, last, occupation, location, hobbies):
		"""
		Initializes first and last name and user_profile information.

		"""
		self.first = first 
		self.last = last 
		self.occupation = occupation 
		self.location = location 
		self.hobbies = hobbies 

	def describe_user(self):
		"""Prints user information"""
		print(self.first + " " + self.last + 
			" user profile includes: ")
		print("\t" + self.occupation)
		print("\t" + self.location)
		print("\t" + self.hobbies)

	def greet_user(self):
		"""Gives user a personalized greeting"""
		print("Welcome back " + self.first.title() + " " + self.last.title() + "!")

	def login_attempts(self, attempts):
		"""logs the number of login attempts per day."""
		self.attempts = attempts
		return attempts

	def read_login_attempts(self):
		"""Reads number of login attempts"""
		print("Current number of login attempts: " + str(self.attempts))

	def increment_login_attempts(self):
		"""
		increments login attempts by 1.
		Prints the number of attempts.
		"""
		self.attempts += 1
		print("current number of login attempts: " + str(self.attempts))

	def reset_login_attempts(self):
		"""resets the number of login attempts to zero"""
		self.attempts = 0


class Administrator(User2):
	"""creates sub-category for administrators of a website"""
	def __init__(self, first, last, occupation, location, hobbies):
		"""Initializes all arguments from the User2 parent class"""
		super().__init__(first, last, occupation, location, hobbies)

		#initializes privileges argument.
		self.privileges = Privileges()

	def greet_user(self):
		"""over writing user greeting from parent class"""
		print("Welcome back administrator " + self.first.title() + " " + 
		self.last.title() + ".")

class Privileges():
	"""
	Creates a now class that handles privileges. As a class assignment 
	in place of an attribute within Administrator.
	"""
	def __init__(self, privileges = []):
		"""Initializes the argument for privileges."""
		self.privileges = privileges
	
	def show_privileges(self):
		print("Administrator has the following privileges at their disposal: ")
		for privilege in self.privileges:
			print("\t- " + privilege)

mason = Administrator("mason","karsevar","data scientist","seattle","hiking")
mason.privileges.privileges = ["managing user blogs","bad actor control"]
mason.privileges.show_privileges()
#Solution is from the ehmatthes github repo. I wouldn't have been able to 
#come up with the following solution. Still have a long way to go.


##9-9:
class Car():
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make + " " + self.model 
		return long_name.title()

	def read_odometer(self):
		"""print a statement showing the car's mileage."""
		print("this car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""set the odometer reading to the given value."""
		self.odometer_reading = mileage 

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles 

	def fill_gas_tank(self):
		"""prints gas tank is being filled"""
		print("gas tank is being filled!!!")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


class Battery():
	"""A simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=70):
		"""Initialize batter attribute."""
		self.battery_size = battery_size 

	def upgrade_battery(self):
		"""increase battery capacity"""
		self.battery_size += 15

	def describe_battery(self):
		"""print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

	def get_range(self):
		"""print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "this car can go approximately " + str(range)
		message += " mils on a full charge."
		print(message)

electronics = ElectricCar("chevy","bolt",2017)
electronics.battery.upgrade_battery()
electronics.battery.get_range()
#I hope this is what the author had in mind when he said that he wanted to 
#to create a line of code that will be able to update the battery
#capacity. the get_range() function was modified due to this function.

#Will need to see how to create a fully customizeable battery capacity function.







