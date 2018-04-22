##chapter 8 Functions:
##Defining functions:
def greet_user():
	"""Display a simple greeting."""
	print("hello!!")

greet_user()# In R this is defined as a temporary function (since no additional)
#information needs to be inputted. 

#The R interpretation of this function is:
#greet_user <- function(x){
#	print("Hello!!!")
#}

#Interesting the statement enclosed in """""" is called a docstring.

##Passing information to a function:
def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user("mason")
#experiment:
greet_user(username = "mason")#this command still works in python. At least there
#isn't too much difference between R function calls and python function calls.

##Passing arguments:
##Positional arguments:
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")#Interestingly the author only talks about
#the positional properties of the arguments in the function assembly. I 
#believe you can bypass this through the following call:
describe_pet(pet_name = "harry", animal_type = "hamster")# Knew it. Python 
#functions are just like R functions. 

##Multiple function calls:
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster","harry")
describe_pet("dog","willie")

#Fun for loop experiment:
name_pets = {
	"willie": "dog",
	"harry": "hamster",
	"rudy": "dog",
}

for name, pet in name_pets.items():
	describe_pet(animal_type = pet, pet_name = name)
#Sweet this function and for loop combination worked. These functions again
#work just like R function.

##Order matters in positional arguments:
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("harry","hamster")

##Keywork arguments:
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = "hamster",pet_name = "harry")#Funny the author clarified
#this point. 
describe_pet(pet_name = "harry", animal_type = "hamster")

##Default values:
def describe_pet(pet_name, animal_type = "dog"):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = "Rudy")
describe_pet("Willie")
describe_pet(pet_name = "Willie", animal_type = "hamster")#This is just like 
#R functions. you can overide default function settings through the same 
#argument. 

##Equivalent Function Calls:
def describe_pet(pet_name, animal_type = "dog"):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("willie")
describe_pet(pet_name = "willie")
describe_pet("harry", "hamster")
describe_pet(animal_type = "hamster", pet_name = "harry")

##Avoiding Argument Errors:

##Return Values:
#The return statement takes a value from inside a function and sends it back
#to the line that called the function.

##Return a Simple Value:
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + " " + last_name 
	return full_name.title()

#This is almost the same as R, except that return is written as return().
author = get_formatted_name("mason", "karsevar")
print(author)

##Making an argument optional:
#Writing a function with a middle name option:
def get_formatted_name(first, middle, last):
	"""Return a full name, neatly formatted."""
	full_name = first + " " + middle + " " + last 
	return full_name.title()

musician = get_formatted_name("john","lee","hooker")
print(musician)
#this function only works if the middle name argument is filled.
#I believe an if statement within the function is needed.

def get_formatted_name(first, last, middle = ""):
	"""Return a full name, neatly formatted."""
	if middle:
		full_name = first + " " + middle + " " + last
	else:
		full_name = first + " " + last 
	return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker","lee")
print(musician)

##Returning a dictionary:
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {"first": first_name, "last": last_name}
	return person

musician = build_person("jimi", "hendrix")
print(musician)

#Additional argument, age:
def build_person(first_name, last_name, age):
	"""Return a dictionary of information about a person."""
	person = {"first": first_name, "last": last_name}
	if age:
		person["age"] = age
	else:
		person["age"] = "NA"#Since having empty columns that overlap into other
		#person's data is dangerous in the field of data science.
	return person

musician = build_person("jimi","hendrix", 27)
print(musician)

##Using a function with a while loop:
def get_formatted_name(first, last):
	"""Return a full name, neatly formatted."""
	full_name = first + " " + last 
	return full_name.title()

#This example uses a while true loop:
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == "q":
		break
	l_name = input("Last name: ")
	if l_name == "q":
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")


