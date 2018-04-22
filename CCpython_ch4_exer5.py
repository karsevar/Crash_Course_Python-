##4-15: Following code is from exercise 3-6:
guest = ["Squirt", "Stegmeier", "Rain on the Earth", "McKinny", "Marilyn"]
guest.insert(0, "Daryl Jumbo")
guest.insert(2, "Ari Encombe")
guest.append("Gary Busy")
print(guest)
none_guest = ["Squirt", "Stegmeier", "McKinny", "Gary Busy", "Daryl Jumbo", "Marilyn"]
for none_guest in none_guest:
	guest.remove(none_guest)
	print("Hi " + none_guest)
	print("I'm sad to say this, but due to my new table not being in in time for the party,")
	print("you are not allowed to be apart of my get to gather.")
	print("I so sorry for any inconvenience this put you through and hopefully I'll see you soon.\n")
#I found out that remove() works way better than pop() for this application.
none_guest = ["Squirt", "Stegmeier", "McKinny", "Gary Busy", "Daryl Jumbo", "Marilyn"]
#Again I need to remind the console of the none_guest list. 
print("\nThe number of people who were removed from the list is ")
print(str(len(none_guest)) + ".")
#For this command the str(len(none_guest)) was used. 
for guest in guest:
	print("Hi " + guest + "!!!")
	print("I just wanted to say that I'm very excited about seeing you this week.") 
	print("attached to this message are the directions to my new house. See you soon!!!\n") 

guest = ["Ari Encombe", "Rain on the Earth"]#Used to remind the console of the length of guest. 
print("\nThe number of people going to the party is " + str(len(guest)) + ".")
#The len(guest) command is again wrapped in a str() function. 