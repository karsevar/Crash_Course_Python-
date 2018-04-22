##Chapter 10 Files and Exceptions:
with open("pi_digits.txt") as file_object:
	contents = file_object.read()
	print(contents)#This works just like the read() function in R 

##File paths:
#Relative file paths for files within one's directory:
file_path = "/User/masonkarsevar/Desktop/rworks/redwines.csv"
#with open(file_path) as file_object: 
#It seems this function doesn't work with different directory locations or 
#rather with cxv files. Will need to look into what the problem is.

##Reading line by line:
filename = "pi_digits.txt"

with open(filename) as file_object:
	for line in file_object:
		print(line)

#Using rstrip() to delete the new lines within the filename output:
filename = "pi_digits.txt"

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

##Making a list of lines from a file:
filename = "pi_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

##Working with a file's contents:
filename = "pi_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#Getting rid of the rest of the white space within the string:
filename = "pi_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

##Large files one million digits:
filename = "almost_million.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.strip()

print(pi_string[:52])#this forces the python console to only print 51 
#of the first lines in the text file.
print(len(pi_string))

##Is your birthday contained in pi?
filename = "almost_million.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.strip()

def birthday_pi(birthday):
	if birthday in pi_string:
		print("your birthday appears in the first million digits of pi.")
	else:
		print("It appears that your birthday is not contained in the first million digits of pi.")

birthday_pi("120372")
birthday_pi("01081992")#Too bad my birthday is not in pi.
#Since sublime text doesn't support input() functions. I had to tweak the 
#chapter exercise a little bit.

##Writing to a file:
##Writing to an empty file:
filename = "program.txt"

with open(filename, "w") as file_object:
	file_object.write("I love programming")

##Writing multiple lines:
with open(filename, "w") as file_object:
	file_object.write("I love programming")
	file_object.write("I hate programming")

with open(filename) as file_object:
	content = file_object.read()
	print(content)#the author was right. Python doesn't put in any 
	#new line characters within the open("w") call.

#Redo with the new line characters:
with open(filename, "w") as file_object:
	file_object.write("I love programming\n")
	file_object.write("I hate programming\n")
with open(filename) as file_object:
	content = file_object.read()
	print(content)

##Appending to a file:
filename = "program.txt"

with open(filename, "a") as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating appications.\n")
#Let's read back what this command does to the program.txt file.
with open(filename) as file_object:
	content = file_object.read()
	print(content)

##Exceptions:
##handling the ZeroDivisionError exception:
#print(5/0)# This raises an error and stops python from accepting 
#anymore information.

##Using try_except blocks:
try:
	print(5/0)
except ZeroDivisionError:
	print("you can't divide by zero!")

##Using exception to prevent crashes:
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break 
	second_number = input("Second number: ")
	if second_number == "q":
		break
	answer = int(first_number) / int(second_number)
	print(answer)
#this program has no exceptions built into the code base hence it is 
#susceptible to DivisionZeroErrors.

##The else block:
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break 
	second_number = input("Second number: ")
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("you can't divide by zeros.")
	else:
		print(answer)

##Handling the FileNotFoundError:
filename = "alice.txt"

#with open(filename, encoding = "utf-8") as f_obj:
	#contents = f.obj.read() 
#Results in an error.

##solution:
filename = "alice.txt"

try:
	with open(filename, encoding = "utf-8") as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)

##Analyzing Text:
title = "Alice in wonderland"
title.split()#To count the number of a specific word within a work of 
#literature, you have to first separate the words into separate lists.

filename = "Alice_in_Wonderland.txt"# Text file retrieved from gutenberg.org.

try:
	with open(filename, encoding = "utf-8") as f_odj:
		contents = f_odj.read()
except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
else:
	#count the number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")

##working with multiple files:
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding = "utf-8") as f_odj:
			contents = f_odj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + 
			" words.")


filename = "Alice_in_Wonderland.txt"
count_words(filename)#Cool the function works perfectly.

filename = "Treasure_Island.txt"
filename2 = "Moby_Dick.txt"
count_words(filename)
count_words(filename2)#That's to be expected, Moby Dick should have more words 
#than treasure island (due to it's more adult oriented themes). But interestingly
#Alice in Wonderland has less words than Treasure Island. 

#Using a for loop to analyze multiple text files:
filenames = ["Alice_in_Wonderland.txt","Treasure_Island.txt","Moby_Dick.txt",
"gospel_peter.txt","little_woment.txt"]
for filename in filenames:
	count_words(filename)

##Failing silently:
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding = "utf-8") as f_odj:
			contents = f_odj.read()
	except FileNotFoundError:
		pass #this command tells python to print nothing when a command fails.
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + 
			" words.")

filenames = ["Alice_in_Wonderland.txt","Treasure_Island.txt","Moby_Dick.txt",
"gospel_peter.txt","little_woment.txt"]
for filename in filenames:
	count_words(filename)#Now the output of little_women is missing from the 
	#result. 

##Storing Data:
##Using json.dump() and json.load():
#will need to create separate files to write the json file and read the json
#back into python. Their names will be number_writer.py and number_reader.py.

##Saving and reading user-generated data:
import json

username = input("What is your name? ")

filename = "username.json"
with open(filename, "w") as f_obj:
	json.dump(username, f_obj)
	print("We'll remember you when you come back, " + username + "!")

#reading the user information back into the console:
import json 

filename = "username.json"
with open(filename) as f_obj:
 	username = json.load(f_obj)
 	print("Welcome back, " + username + "!")


import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it.
filename = "username.json"
try: 
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, "w") as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")

##Refactoring:
import json 

def greet_user():
	"""Greet the user by name"""
	filename = "username.json"
	try: 
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, "w") as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()

#Refactoring the greet_user() function a little more.
import json 

def get_stored_username():
	"""Get stored username if available."""
	filename = "username.json"
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None 

	else:
		return username

def greet_user():
	"""greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = input("What is your name? ")
		filename = "username.json"
		with open(filename, "w") as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")

greet_user() 

#refactoring continued:
import json

def get_stored_username():
	"""Get stored username if available."""
	filename = "username.json"
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""prompt for a new username."""
	username = input("What is your name? ")
	filename = "username.json"
	with open(filename, "w") as f_obj:
		json.dump(username, f_obj)
	return username 

def greet_user():
	"""greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user() 


