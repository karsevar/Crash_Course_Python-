##Modifying an attribute's value through a method:
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

my_new_car = Car("audi", "a4",2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#Setting the odometer to a specified value. Or rather keeping the odometer 
#from being rolled back.
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
		"""
		set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage 
		else:
			print("You can't roll back an odometer.")

my_new_car = Car("subaru","wrx sti", 2003)
my_new_car.update_odometer(26000)
my_new_car.read_odometer()

#OK now let's try to roll back the odometer of the defined 
#Subaru car.
my_new_car.update_odometer(12000)#It actually worked!!!

##Incrementing an attribute's value through a method:
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

my_used_car = Car("subaru","outback",2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23000)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

##Inheritance:
#Using the Car class from earlier as the parent class for the ElectricCar class.
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

my_tesla = ElectricCar("tesla","model s", 2016)
print(my_tesla.get_descriptive_name())

##Defining Attributes and methods for the child class:
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		"""print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

my_tesla = ElectricCar("tesla","model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

##Overriding methods from the parent class:
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
		self.battery_size = 70

	def describe_battery(self):
		"""print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

	def fill_gas_tank(self):
		"""Electronic cars don't have a gas tank."""
		print("This car doesn't need a gas tank")#this overrides the 
		#fill_gas_tank method within the parent class Car.


my_tesla = ElectricCar("tesla","model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()#The parent method has been overwritten.

my_old_car = Car("toyota","mr2","1987")
print(my_old_car.get_descriptive_name())
my_old_car.fill_gas_tank()#The fill_gas_tank() method remains the same 
#for objects called by the Car() parent class.

##Instances and attributes:
class Battery():
	"""A simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=70):
		"""Initialize batter attribute."""
		self.battery_size = battery_size 

	def describe_battery(self):
		"""print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar("tesla","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

##Expanding on the Battery class:
class Battery():
	"""A simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=70):
		"""Initialize batter attribute."""
		self.battery_size = battery_size 

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

my_tesla = ElectricCar("tesla","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

##Importing classes:
##Importing a single class:
#module has been creates that stores a copy of the Car class. This class has
#been renamed Car2 as to descrease confusion.
from car import Car2

my_new_car = Car2("audi","a4",2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

##Storing multiple classes in a module:
#from car import ElectricCar2 

#my_tesla = ElectricCar2("tesla","model s", 2016)

#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()

##importing multiple classes from a module:
#from car import Car2

my_beetle = Car("volkswagen","beetle",2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla","roadster",2016)
print(my_tesla.get_descriptive_name())

##Importing an entire module:
#import car 

#my_beetle = car.Car("volkswage","beetle",2016)
#print(my_beetle.get_descriptive_name())

#my_tesla = car.ElectricCar2("tesla","roadster",2016)
#rint(my_tesla.get_descriptive_name())

##Importing a module into a module:
#Creating a electriccar and battery module and removing the ElectricCar2 
#and Battery2 classes from the car module.

from car import Car2
from electric_car import ElectricCar2

my_beetle = Car2("volkswage","beetle",2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla","roadster",2016)
print(my_tesla.get_descriptive_name())

##the python standard library:
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")





