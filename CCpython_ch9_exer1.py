##9-1:
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

restaurant = Restaurant("dude's", "italian")
restaurant.open_restaurant()
restaurant.describe_restaurant()
print(restaurant.name)
print(restaurant.cuisine)
#this simple class command call works just fine. Really cool, I didn't know 
#was even possible with python programming. 

##9-2:
restaurant_1 = Restaurant("jim", "american")
restaurant_2 = Restaurant("kenji", "japanese")
restaurant_3 = Restaurant("rhino", "ethiopean")
restaurants = [restaurant_1, restaurant_2, restaurant_3]

for restaurant in restaurants:
	restaurant.describe_restaurant()
	restaurant.open_restaurant()
#All the class calls (or rather all three attributes) work perfectly.

##9-3:
class User():
	"""Copies and prints inputted user information"""

	def __init__(self, first, last, user_profile):
		"""Initializes first and last name and user_profile information"""
		self.first = first 
		self.last = last 
		self.user_profile = user_profile

	def describe_user(self):
		"""Prints user information"""
		print(self.first + " " + self.last + 
			"user profile includes: " + self.user_profile)

	def greet_user(self):
		"""Gives user a personalized greeting"""
		print("Welcome back " + self.first.title() + " " + self.last.title() + "!")

user1 = User("mason","karsevar","data science")
user2 = User("alice","karsevar","project manager")
user1.describe_user()
user1.greet_user()
#This works pretty well. But I might have to change the user_profile argument 
#call into a syntax that can take more than one object. Will use the ** syntax
#from page 153.

class User_me():
	"""Copies and prints inputted user information"""

	def __init__(self, first, last, **user_profile):
		profile = []
		"""Initializes first and last name and user_profile information"""
		self.first = first 
		self.last = last 
		for self.key, self.value in self.user_profile.items():
			profile[self.key] = self.value
		return profile

	def describe_user(self):
		"""Prints user information"""
		print(self.first + " " + self.last + 
			"user profile includes: " + profile)

	def greet_user(self):
		"""Gives user a personalized greeting"""
		print("Welcome back " + self.first.title() + " " + self.last.title() + "!")

#user1 = User("mason","karsevar", occupation = "data science", location = "seattle")
#user2 = User("alice","karsevar","project manager")
#user1.describe_user()
#It seems that the ** syntax doesn't work within class calls. Will need to 
#create the class the more conventional way.

##Final attempt:
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

profiles = [user1, user2, user3, user4]
for profile in profiles:
	profile.describe_user()
	profile.greet_user()

#Sweet this function call works perfectly. 




