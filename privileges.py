#Keeps the class Privileges() within a separate module.

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