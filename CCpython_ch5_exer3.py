##5-8:
usersnames = ["admin","mkarse","rats","gil193","phil_me","cap_hatred","admin"]
for usersname in usersnames:
	if usersname == "admin":
		print("Welcome Back, admin!!")
	else:
		print("Welcome Back, " +usersname+ ".")

##5-9:
usersnames = []
if usersnames:
	for usersname in usersnames:
		if usersname == "admin":
			print("Welcome Back, admin!!")
		else:
			print("Welcome Back, " + usersname+ ".")
else:
	print("No Usersnames detected at this time.")
# This command works with both filled lists and empty lists.
new_users = ["eatMe","Dr.Bitch","cannibal","Mkarse","savage",
"godzilla","monster_man","rush"]
old_users = ["mkarse","dr.bitch","sleeper","ralph","eat_me","flier"]

for new_user in new_users:
	if new_user.lower() in old_users:
		print("\nI'm sorry but " + new_user + " is already taken.")
		print("Please pick another username.")
	else:
		print("\nWelcome to alcoholic's anonymous " +new_user+ "!!!")
		print("The first dating site made specifically for recovering alcoholics.")

##5-11:
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(str(number) + "th")



