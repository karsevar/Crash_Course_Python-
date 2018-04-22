##8-9:
magicians = ["madokka","magician","mind monger","david blane","dr.bitch"]
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
show_magicians(magicians)

##8-10:
magicians = ["madokka","magician","mind monger","david blane","dr.bitch"]
def make_great(magician):
	print("\nThe Great " + magician.title())

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
		make_great(magician)

show_magicians(magicians)
#I used a nested function call, where the make_great() function is used within 
#the show_magicians() function. this is most likely not what the author had in 
#mind as it complicates matters. 

#modifying the magicians list:
magicians = ["madokka","magician","mind monger","david blane","dr.bitch"]
great_magicians = []
def make_great(magicians):
	"""
	Displays all magician names with the phrase "the great" at the beginning.
	And moves all objects from magicians to the great_magicians list.
	"""
	while magicians:
		magician_current = magicians.pop()
		great_magicians.append("the great " + magician_current)
make_great(magicians[:])
print(great_magicians)# Sweet this function actually worked.
print(magicians)#The slice method actually made a copy of magicians.

def show_magicians(magicians):
	"""this function prints the objects within list magicians"""
	for magician in magicians:
		print(magician.title())

show_magicians(magicians = great_magicians)
#I believe this is actually what the author had in mind.

##8-11:This is primarily the same operation from the preceeding function calls:
magicians = ["madokka","magician","mind monger","david blane","dr.bitch"]
great_magicians = []#this operation zeros out the other objects from previous 
#operations.
make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)



