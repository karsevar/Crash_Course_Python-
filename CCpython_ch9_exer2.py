##9-4:
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

	def set_number_served(self, number_served):
		"""
		Sets and prints the number of customers served in the
		restaurant.
		"""
		self.number_served = number_served 
		print("Total number of people served since opening: " + str(self.number_served))

	def read_number_served(self):
		"""prints the number of customers served"""
		print("Total number of people served since opening: " + str(self.number_served))

	def increment_number_served(self, number):
		"""increments the number of people served daily"""
		self.number_served += number 

restaurant = Restaurant("dino","italian")
restaurant.set_number_served(100000)#this class method call worked perfectly.
#The idea surrounding this method is the same as the odometer example.
#The method prints the total number of people served sinced first opening for 
#business.
restaurant.increment_number_served(200)
restaurant.read_number_served()#Was forced to make this function do to 
#the fact that set_number_served() couldn't read the number of people served
#without a number argument call.

##9-5:
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

user1 = User2("alice","karsevar","project manager","san francisco","real estate")
user2 = User2("mason","karsevar","data science","seattle","hiking")
user1.login_attempts(1)# this starts the increment login attempts method.
user1.increment_login_attempts()
user1.reset_login_attempts()
#This class function works just as the author instructed within the 
#problem description. I believe that this class program can be improved upon.
#Will need to come back to this problem later.


user1.read_login_attempts()