##the following module stores the Restaurant parent class and the IceCreamStand
#subclass within a separate file. The classes are from chapter 9.

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