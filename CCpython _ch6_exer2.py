##6-4:
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

rivers = {
	"nile": "egypt",
	"columnbia": "washington, united states",
	"amazon": "brazil",
	"rine": "germany",
	"Rio Grand": "mexico"
	}
for river, country in rivers.items():
	print("\nI believe the " + river.title() + " River runs through "
		+ country.title())

for country in rivers.values():
	print(country.title())

for river in rivers.keys():
	print(river.title() + " River.")

##6-6:
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

poll_names = ["jen","steve","ash","sarah","pete","edward"]
for name in poll_names:
	if name in favorite_languages.keys():
		print("\nThank you " + 
		name.title() +  " for being a part of our semi-annual poll!")
	else:
		print("\nHi " + name.title() 
		+ " we noticed that you haven't responded to our computer language poll.")
		print("Please send us your response as the answers our team recieves from you will greatly help us with our research.")

