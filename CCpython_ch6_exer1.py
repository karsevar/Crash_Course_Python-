##6-1:
persons = {"first name": "Kyle", "last name": "Hicks", "city": "Bellevue"}
print(persons)

##6-2:
favorite_numbers = {
	"kyle": 36,
	"scotty": 69,
	"chris r":79,
	"james": 54,
	"mason": 64,
	"danny": 36,
	}

for name, number in favorite_numbers.items():
	print(name.title() + "'s favorite number is " 
	+ str(number))
#the following answer was ripped off of page 104.

glossary = {
	"append()": "add to list",
	"remove()": "remove index position",
	"range()": "python's seq()",
	"pop()": "removes the last entry",
	"del": "delete",
	"print()": "print",
	"{}": "dictionary",
	"[]": "list",
	}

for name, definition in glossary.items():
	print("\n"+ name + ": " + definition)


