##Chapter 6 Dictionaries:
#I have a feeling the dictionaries can be conceptualized as data.frames() within 
#the R computing language. Will need to check into this setiment.

##A Simple Dicionary:
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])# Just as I suspected, this structure works just like 
#data.frames(). 

##Working with dictionaries:
##Accessing Values in a dictionary:
alien_0 = {"color": "green"}
#Most likely the R equivalent can be written as 
#alien <- data.frame(color = c("green"), points = 5) 
#or rather alien <- list(alien_0 = c("green", 5)).
print(alien_0["color"])
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print("you just earned " + str(new_points) + " points!")

##Adding New key-value pairs:
alien_0 = {"color": "green", "points": 5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)#just like subsetting data.frames and lists().

##Starting with an empty dictionary:
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

##modifying values in a dictionary:
alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x_position: " + str(alien_0["x_position"]))
alien_0["speed"] = "fast"

if alien_0["speed"] == "slow":
	x_increment = 1
elif alien_0["speed"] == "medium":
	x_increment = 2
else: 
	x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x-position: " + str(alien_0["x_position"]))

##Removing Key_value pairs:
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]# I would assume that this command would be written as 
#alien.del("points"). I guess there must be a remove() variant. 
print(alien_0)

##A dictionary of similar objects:
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

print("Sarah's favorite language is " + 
	favorite_languages["sarah"].title() + 
	".")

##Looping through a dictionary:
##Looping through all key-value pairs:
user_0 = {
	"username": "efermi",
	"first": "enrico",
	"last": "fermi",
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " 
		+ language.title() + ".")

##Looping through all the keys in a Dictionary:
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name in favorite_languages.keys():
	print(name.title())

#the adove code snippet is the default behavior of dictionaries placed in 
#loops:
for name in favorite_languages:
	print(name)
#Hence this line has the same output.

favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + 
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")
#super smart idea using the index object for friends as a key for the values 
#in the dictionary favorite_languages.

favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

if "erin" not in favorite_languages.keys():
	print("Erin, please take our poll.")

##Looping through a dictionary's keys in order:
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

##Looping through all values in a dictionary:
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

##Using the set() method to omit repeatition:
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

##Nesting:
##A list of dictionaries:
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

#Creating a fleet of 30 aliens:
aliens = []

#make 30 aliens
for alien_number in range(30):
	new_alien = {"color": "green", "points": 5, "speed": "slow"}
	aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created:
print("Total number of aliens: " + str(len(aliens)))

##Modifying the alien fleet using for loops and nested dictionaries
aliens = []
for alien_number in range(30):
	new_alien = {"color": "green", "points": 5, "speed": "slow"}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien["color"] == "green":
		alien["color"] = "yellow"
		alien["speed"] = "medium"
		alien["points"] = 10

for alien in aliens[0:5]:
	print(alien)
print("...")
#this code modified the green aliens in index position [0:3] to be color 
#yellow, speed medium and points 10. 

##Using an elif statement as a efficient coding strategy:
for alien in aliens[0:5]:
	if alien["color"] == "green":
		alien["color"] = "yellow"
		alien["speed"] = "medium"
		alien["points"] = 10
	elif alien["color"] == "yellow":
		alien["color"] = "red"
		alien["speed"] = "fast"
		alien["points"] = 15

for alien in aliens[:]:
	print(alien)

##A list in a dictionary:
pizza = {
	"crust": "thick",
	"toppings": ["mushrooms","extra cheese"],
}

print("you ordered a " + pizza["crust"] + "-crust pizza " +
	"with the following toppings:")
for topping in pizza["toppings"]:
	print("\t" + topping)

##Using the favorite computer languages list again except with nested dictionary
#and list.
favorite_languages = {
	"jen": ["python", "ruby"],
	"sarah": ["c"],
	"edward": ["ruby","go"],
	"phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite computer languages are:")
	for language in languages:
		print("\t" + language.title())

#Cool this line of code works perfectly. And sadly I don't know how to write
#this line in R.

##If statement alternative:
favorite_languages = {
	"jen": ["python", "ruby"],
	"sarah": ["c"],
	"edward": ["ruby","go"],
	"phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print("\n" + name.title() + "'s favorite computer languages are:")
		for language in languages:
			print("\t" + language.title())
	elif len(languages) == 1:
		for language in languages:
			print("\n" + name.title() + "'s favorite computer language is:")
			print("\t" + language.title())
#this line of code is a little convoluted but it still works.

##A dictionary in a dictionary:
users = {
	"aeinstein": {
		"first": "albert",
		"last": "einstein",
		"location": "princeton",
		},
	"mcurie": {
		"first": "marie",
		"last": "curie",
		"location": "paris",
		},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info["first"] + " " + user_info["last"]
	location = user_info["location"]

	print("\tfull name: " + full_name.title())
	print("\tLocation: " + location.title())