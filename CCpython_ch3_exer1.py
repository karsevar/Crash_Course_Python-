##3-1 
friends = ["Ari Encombe", "Robert Grey", "Masanori", "Masa", "Kenji", "Jonny Phan", "Brian Miller"]
print(friends)
for friends in friends:
	print(friends)# Is is way simpler than R programming. To make a comparible 
	#loop you need to write for(i in 1:friends){ print(friends[i])}

##3-2 
friends = ["Ari Encombe", "Robert Grey", "Masanori", "Masa", "Kenji", "Jonny Phan", "Brian Miller"]
message = "How's everything going bro?"
for friends in friends:
	print(friends + "!")
	print(message)
#For loops have an odd characteristic where after the indexed list is used 
#the list is over written by the last indexed object. 
#I was forced to rewrite the friends list as a result.

##3-3
trans = ["Hudson Hornet", "trains", "planes", "city buses"]
for trans in trans:
	messages = ["I would like to purchase a " + str(trans) + " once I become a data scientist.", "Interestingly enough " + trans + " don't make me sick.", "I hate riding in " + trans + " for long periods of time.", "I miss riding " + trans + " to the end of the line."]
	print(messages)
	#this wasn't what I had in mind. Will need to find a way to combine the 
	#index positions of messages with trans.

for messages in trans:
	print(messages)
#This is somewhat better. The trans list objects were printed in the proper
#messages but in the end the letters of city buses were printed onto the console.
