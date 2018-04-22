def make_great(magicians):
	"""
	Displays all magician names with the phrase "the great" at the beginning.
	And moves all objects from magicians to the great_magicians list.
	"""
	for magician in magicians:
		magician_current = magicians.pop()
		great_magicians.append("the great " + magician_current)
		return(great_magicians)
		

def show_magicians(magicians):
	"""this function prints the objects within list magicians"""
	for magician in magicians:
		print(magician.title())


great_magicians = []
magicians = ["mason karsevar","alice karsevar","kieth mosher","tj hooker"]
great_magicians = make_great(magicians)
print(great_magicians)