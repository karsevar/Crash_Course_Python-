##6-7:
persons = {"first name": "Kyle", "last name": "Hicks", "city": "Bellevue"}
friend_1 = {"first": "kyle", "last": "hicks", "city": "bellevue"}
friend_2 = {"first": "ari", "last": "ecombe", "city": "seattle"}
friend_3 = {"first": "alice", "last": "karsevar", "city": "san francisco"}
people = [friend_1, friend_2, friend_3]
print(people)
for person in people:
	print(person)

##6-8:
rudy = {"animal": "dog", "owner": "mason karsevar"}
val = {"animal": "dog", "owner": "chris r"}
alle = {"animal": "dog", "owner": "jim riems"}
pets = [rudy, val, alle]

for pet in pets:
	print(pet) 
#Not really sure if I can do anything with this answer (or rather exercise).
#Will need to come back to this problem later on through my studies.

favorite_places = {
	"chris r": ["san francisco", "seattle"],
	"mason karsevar": ["seattle", "tokyo"],
	"alice karsevar": ["san fransisco", "seattle", "tokyo"],
	"aaron champion": ["seattle"],
	"gabe gibson": ["seattle"],
}

for name, places in favorite_places.items():
	if len(places) > 1:
		print("\n" + name.title() +"'s favorite places to visit are: ")
		for place in places:
			print("\t" + place.title())
	elif len(places) == 1:
		for place in places:
			print("\n" + name.title() +"'s favorite place to visit is")
			print("\t" + place.title())

##6-10:
favorite_numbers = {
	"chris r": [2,5,17],
	"mason karsevar": [64, 69, 39],
	"doug glatt": [69],
	"phil johnson": [0,1],
	"kieth mosher": [0,1],
	"alice karsevar": [7],
}

for name, numbers in favorite_numbers.items():
	if len(numbers) > 1:
		print("\n" + name.title() + "'s favorite numbers are:")
		for number in numbers:
			print("\t" + str(number))
	elif len(numbers) == 1:
		for number in numbers:
			print("\n" + name + "'s favorite number is:")
			print("\t" + str(number))

##6-11:
cities = {
	"seattle": {
		"pop": 1000000,
		"country": "united states",
		"fact": "established in 1860",
		},
	"spokane": {
		"pop": 500000,
		"country": "united states",
		"fact": "was larger than seattle during the 1800s",
		},
	"manila": {
		"pop": 15000000,
		"country": "philippines",
		"fact": "unknown",
		},
}

for city, city_info in cities.items():
	print("\nCity name: " + city.title())
	population = city_info["pop"]
	countries = city_info["country"]
	info = city_info["fact"]

	print("\tPopulation: " + str(population))
	print("\tCountry: " + countries.title())
	print("\tInteresting fact: " + info)

##6-12:
persons = {"first name": "Kyle", "last name": "Hicks", "city": "Bellevue"}
friend_1 = {"first": "kyle", "last": "hicks", "city": "bellevue"}
friend_2 = {"first": "ari", "last": "ecombe", "city": "seattle"}
friend_3 = {"first": "alice", "last": "karsevar", "city": "san francisco"}

persons = {
	"akarse": {
		"first": "alice",
		"last": "karsevar",
		"occupation": "project manager",
		"company": "twitch",
		"location": "san francisco",
		},
	"khicks": {
		"first": "kyle",
		"last": "hicks",
		"occupation": "unknown",
		"company": "unknown",
		"location": "bellingham",
		},
	"mkarse": {
		"first": "mason",
		"last": "karsevar",
		"occupation": "unemployed",
		"company": "unknown",
		"location": "spokane",
		},
	"acomb": {
		"first": "ari",
		"last": "encombe",
		"occupation": "bike manufacturer",
		"company": "unknown",
		"location": "seattle",
		},
}

for username, info in persons.items():
	print("\n" + username)
	full_name = info["first"] + " " + info["last"]
	occupat = info["occupation"]
	companies = info["company"]
	area = info["location"]

	print("\tName: " + full_name.title())
	print("\tOccupation: " + occupat.title())
	print("\tEmployer: " + companies.title())
	print("\tlocation: " + area.title())

