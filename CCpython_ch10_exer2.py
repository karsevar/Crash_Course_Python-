##10-3:
filename = "guest.txt"

print("Welcome humble traveler!")
name = input("Please input your name to begin your journey: ")
with open(filename, "a") as file_object:
	file_object.write(name + "\n")#Cool this line records inputs.

##10-4:
print("Welcome humble traveler!")

while True:
	print("To quit this session simply enter 'q'.")
	name = input("Please input your name to begin your journey: ")
	if name == "q":
		break
	else:
		print("Hello " + name.title() + "!")
		print("Your name has been recorded in guest_book.txt")
		with open(filename, "a") as file_object:
			file_object.write(name + "\n")

#These lines of code actually work. Very good!

##10-5:
filename = "response.txt"
print("We are current carrying out a poll for young programming professionals.")

while True:
	answer = input("Would you like to be appear of this poll? (yes/no) ")
	if answer == "no":
		break
	else:
		print("would you mind giving us a reason why you like programming")
		reason = input("answer here: ")
		print("Your response has been recorded.")
		print("Thanks so much for your response!")
		with open(filename, "a") as file_object:
			file_object.write(reason + "\n")#The responses were recorded.

#This program works just fine, but I feel it's a little primitive. 
#this while loop can actually be attached to the preceeding while loop.
#Will need to look into this.

