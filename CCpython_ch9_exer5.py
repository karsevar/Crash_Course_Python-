##9-13:
glossary = {
	"append()": "add to list",
	"remove()": "remove index position",
	"range()": "python's seq()",
	"pop()": "removes the last entry",
	"del": "delete",
	"print()": "print",
	"{}": "dictionary",
	"[]": "list",
	"sorted()": "temporary sorting method",
	"sort": "permanent sorting method",
	"set()": "searches for unique entries in dictionaries",
	"values()": "Dictionary, lists values",
	"items()": "Dictionary, lists values and keys",
	"keys()": "Dictionary, lists the keys",
	}

for name, definition in glossary.items():
	print("\n"+ name + ": ")
	print(definition)
#Unordered

#ordered
from collections import OrderedDict

glossary_ordered = OrderedDict()
for name, definition in glossary.items():
	glossary_ordered[name] = definition 

for name, definition in glossary_ordered.items():
	print("\n" + name + ":")
	print(definition)

print(glossary)#Interesting the original glossary retained it's components even 
#after the for loop.

##9-14:
from random import randint
x = randint(1,6)

x = []
while len(x) < 10:
	x.append(randint(1,6))

print(x)

class Die():
	"""simulates rolling a six-sided die"""
	def __init__(self, sides):
		"""Initializes the self and sides arguments"""
		self.sides = sides 

	def roll_dice(self):
		"""rolls dice by default 1 time"""
		x = randint(1, self.sides)
		print("The dice landed on a " + str(x))

	def roll_more(self, times):
		"""rolls dice more than the default value"""
		self.times = times
		x2 = []
		while len(x2) < times:
			dice_roll = randint(1, self.sides)
			print("The die has rolled a " + str(dice_roll))
			x2.append(dice_roll)
			
			

mice = Die(6)
#The default random generator works perfectly. 
mice.roll_dice()

#Let's see if the roll_more() function works also.
mice.roll_more(10)





