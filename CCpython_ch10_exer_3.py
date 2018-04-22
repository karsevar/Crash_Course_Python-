##10-6:
def addition(number_1, number_2):
	try:
		answer = int(number_1) + int(number_2)
		print("The solution is " + str(answer))
	except ValueError:
		print("I'm sorry you can't add a none numerical value.")

addition(3, 4)
addition("string", 4)
#Function works perfectly with both of the instances.

##10-7:
def addition(number_1, number_2):
	"""A calculator that can only do addition"""
	try:
		answer = int(number_1) + int(number_2)
		print("The solution is " + str(answer))
	except ValueError:
		print("I'm sorry you can't add a none numerical value.")

addition(3, 4)
addition("string", 4)

while True:
	print("You can quit this session through inputting 'q'")
	number_1 = input("Please input a number: ")
	if number_1 == "q":
		break
	number_2 = input("Please input another number: ")
	if number_2 == "q":
		break
	else:
		addition(number_1, number_2)
#this while loop works perfectly on the console.

##10-8:
filename = "dog_names.txt"

try: 
	with open(filename, encoding = "utf-8") as f_obj:
		contents = f_obj.read()
		print(contents)
except FileNotFoundError:
	print("File can't be found in your directory.")

filenames = ["dog_names.txt","cat_names.txt","whale_names.txt"]#of course 
#whale_names.txt does not exist in the directory. This is used to test whether
#the except command works or not.

def file_exist(filename):
	"""Prints the contents of the designated files."""
	try: 
		with open(filename, encoding = "utf-8") as f_obj:
			contents = f_obj.read()
			print(contents)
	except FileNotFoundError:
		print("File can't be found in your directory.")

for filename in filenames:
	file_exist(filename)
#This function worked perfectly.

##10.9:
def file_exist(filename):
	"""
	Prints the contents of the designated files. 
	Does not print failed instances.
	"""
	try: 
		with open(filename, encoding = "utf-8") as f_obj:
			contents = f_obj.read()
			print(contents)
	except FileNotFoundError:
		pass

for filename in filenames:
	file_exist(filename)

##10.10:
filenames = ["Alice_in_Wonderland.txt","Treasure_Island.txt","Moby_Dick.txt",
"gospel_peter.txt","little_woment.txt"]

def word_frequency(filename, word):
	try:
		with open(filename, encoding = "utf-8") as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass

	else:
		counting = contents.lower().count(word)
		print("The word " + word + " shows up in " + filename + 
			" about " + str(counting) + " times.")

for filename in filenames:
	word_frequency(filename, "the")# Cool this function actually worked.

#Let's check if there's any difference in word frequency between lower case 
#upper case instances of the word the.
filenames = ["Alice_in_Wonderland.txt","Treasure_Island.txt","Moby_Dick.txt",
"gospel_peter.txt","little_woment.txt"]

def word_frequency(filename, word):
	try:
		with open(filename, encoding = "utf-8") as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass

	else:
		counting = contents.count(word)
		print("The word " + word + " shows up in " + filename + 
			" about " + str(counting) + " times.")

#Lower case instances:
for filename in filenames:
	word_frequency(filename, "the")

#upper case instances:
for filename in filenames:
	word_frequency(filename, "The")

#should have know the lower case instance of "the" is more than its
#upper case counterpart. 
#A funny little analysis is finding how many "thes" are required to be considered 
#a literary master piece. 






	
