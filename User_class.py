##Final attempt:
class User2():
	"""Copies and prints inputted user information"""

	def __init__(self, first, last, occupation, location, hobbies):
		"""Initializes first and last name and user_profile information"""
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

user1 = User2("mason","karsevar","data science", "seattle", "hiking")
user2 = User2("alice","karsevar","project manager","san francisco","real estate")
user3 = User2("aaron","campion","project manager", "seattle","pokemon")
user4 = User2("ari","ecombe","bicycle manufacturer","seattle","brewing")

user1.describe_user()
