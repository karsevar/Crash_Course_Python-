
def make_great(magicians):
	great_magicians = []
	"""
	Displays all magician names with the phrase "the great" at the beginning.
	And moves all objects from magicians to the great_magicians list.
	"""
	while magicians:
		magician_current = magicians.pop()
		great_magicians.append("the great " + magician_current)
	return great_magicians

def show_magicians(magicians):
	"""this function prints the objects within list magicians"""
	for magician in magicians:
		print(magician.title())

