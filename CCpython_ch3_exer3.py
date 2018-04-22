##3-8
locations = ["meru", "mt.everest", "mt.olympia", "antarctica", "montana", "glacier peak"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse = True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse = True)
print(locations)

##3-9
guest = ["Squirt", "Stegmeier", "Rain on the Earth", "McKinny", "Marilyn"]
guest.insert(0, "Daryl Jumbo")
guest.insert(2, "Ari Encombe")
guest.append("Gary Busy")
print(guest)
none_guest = ["Squirt", "Stegmeier", "McKinny", "Gary Busy", "Daryl Jumbo", "Marilyn"]
for none_guest in none_guest:
	guest.remove(none_guest)
	print("Hi " + none_guest + ", \nI'm sad to say this, but due to my new table not being in in time for the party, you are not allowed to be apart of my get to gather. \nI so sorry for any inconvenience this put you through and hopefully I'll see you soon.\n")
#I found out that remove() works way better than pop() for this application.
none_guest = ["Squirt", "Stegmeier", "McKinny", "Gary Busy", "Daryl Jumbo", "Marilyn"]
#Again I need to remind the console of the none_guest list. After running a for loop
#a particular list that's used as an index needs to be reset. 
print("\nThe number of people who were removed from the list is " + str(len(none_guest)) + ".")
#For this command the len(none_guest) command needed to be wrapped in the str() function 
#for the print() command to work properly. 
for guest in guest:
	print("Hi " + guest + "!!!\n I just wanted to say that I'm very excited about seeing you this week. \nattached to this message are the directions to my new house. See you soon!!!\n") 

guest = ["Ari Encombe", "Rain on the Earth"]#Used to remind the console of the length of guest. 
print("\nThe number of people going to the party is " + str(len(guest)) + ".")
#The len(guest) command is again wrapped in a str() function. 

##3-10 
vehicle = ["Ford Fiesta ST", "VW Golf Type R", "Dodge Omni GLHS", "Hudson Hornet", "Packard Super Deluxe", "mazda rx7", "toyota mr2"]
print(vehicle)
print(vehicle[-2].title())
print(vehicle[-1].title())
print("I would really love to drive a mid-engined car like an " +vehicle[-1] + ".")
vehicle.append("Dodge Charger Shelby")
print(vehicle)
vehicle.insert(3, "VW Golf GTI")
none_vehicle = vehicle.pop()
vehicle.remove("toyota mr2")
print(none_vehicle)
print(vehicle)
print(sorted(vehicle))
vehicle.reverse()
print(vehicle)
vehicle.reverse()
print(vehicle)



