#stores the user2 class within a separate module.
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