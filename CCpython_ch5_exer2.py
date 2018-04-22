##5-3:
alien_color = "green"
if alien_color == "red":
	print("Player 1 earned 5 points.")
if alien_color != "red":
	print()

##5-4:
alien_color = "green"
if alien_color == "green":
	print("Alien ship destroyed.")
	points = 5
elif alien_color != "green":
	print("critical hit!")
	points = 10 
print("Plus " + str(points))

alien_color = "red"
if alien_color == "green":
	points = 5
else:
	points = 10
print("alien ship destroyed")
print("+"+str(points))

##5-5:
alien_color = "green"
if alien_color == "green":
	points = 5
elif alien_color == "yellow":
	points = 10
else:
	points = 15
print("alien ship destroyed")
print("+"+str(points))
#This command works with all three different colors.

##5-6:
age = 19
if age < 2:
	type = "baby"
elif age < 4:
	type = "toddler"
elif age < 13:
	type = "kid"
elif age < 20:
	type = "teenager"
elif age < 65:
	type = "adult"
else:
	type = "elder"
print("Person type for age " +str(age) + " is " +type+".")
#this line of code works perfectly for all age groups.

##5-7:
favorite_fruits = ["apples","grapes","figs","water melon","bananas"]
if "apples" in favorite_fruits:
	print("You really like apples.")
if "oranges" not in favorite_fruits:
	print("You don't like oranges.")
if "figs" in favorite_fruits:
	print("You like figs.")
if "mangos" not in favorite_fruits:
	print("You don't like mangos.")
if "water melon" in favorite_fruits:
	print("You really like water melons.")







