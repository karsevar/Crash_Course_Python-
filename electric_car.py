from car import Car2

class Battery2():
	"""A simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=70):
		"""Initialize batter attribute."""
		self.battery_size = battery_size 

	def describe_battery(self):
		"""print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

	def get_range(self):
		"""print statement about the range this battery provides"""
		if self.battery_size == 70:
			range = 240
		else:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
		print(message)


class ElectricCar2(Car2):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery2()