##Chapter 7 part 2
##Introducing while loops:
##The while loop in action:
current_number = 1
while current_number <=5:
	print(current_number)
	current_number += 1

##Letting the user choose when to quit:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
	message = input(prompt)
	print(message)

#alternative code:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
	message = input(prompt)
	if message != "quit":
		print(message)

##Using the flag:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program. "

active = True 
while active:
	message = input(prompt)
	if message == 'quit':
		active = False 
	else:
		print(message)

#Using break to exit a loop:
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else: 
		print("I'd love to go to " + city.title() + "!")

##Using continue in a loop:
current_number = 0 
while current_number < 10:
	current_number += 1
	if current_number %2 == 0:
		continue
	print(current_number)


current_number = 0 
while current_number < 100:
	current_number += 1
	if current_number %10 != 0:
		continue
	print(current_number)
#Cool little code snippet. This is more straight forward than the range() method 
#alternative.
me = list(range(0, 11, 3))#I sadly don't remember how I calculated odd numbers through
#this method call. will need to look at my notes on this matter.

##Avoiding infinite loops:
x = 1 
while x <= 5:
	print(x)
	x += 1

#infinite loop example:
x = 1
while x <= 5:
	print(x) 
#As you can see this loop prints 1 forever because the counter value x was 
#never set to reach the stopping value 5.

##Using a while loop with lists and dictionaries:
unconfirmed_users = ["alice","brian","candace"]
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()#Interesting to pop() method 
	#fills the current_user object and ultimately the confirmed_users list.
	print("Verifying user : " + current_user.title())
	confirmed_users.append(current_user)# Same idea from exercise 7-6. 

print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

##Removing all instances of specific values from a list:
pets = ["dog","cat","dog","goldfish","cat","rabbit","cat"]
print(pets)

while "cat" in pets:
	pets.remove("cat")

print(pets)
#Ingenius idea of using a while loop to remove all instances of "cat" in the 
#pets list.

##Filling a dictionary with user input:
responses = {}
polling_active = True 

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	responses[name] = response#this tells the program to add key (name) and item
	#(response) to the dictionary. 
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == "no":
		polling_active = False
print("\n---Poll Results---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")


