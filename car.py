##Car module from chapter 9 page 179:
class Car2():
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
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an odometer.")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles 

	def fill_gas_tank(self):
		"""prints gas tank is being filled"""
		print("gas tank is being filled!!!")








