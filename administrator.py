#Stores the Administrator() class within a separate module:
from user import User2
from privileges import Privileges

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