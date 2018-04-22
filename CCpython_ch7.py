##Chapter 7 User input and while loops:
##How the input() function works:
message = input("Tell me something, and I will repeat it back to you: ")
print(message)# remember input() functions don't work on sublime text session. 
#Will need to use the system console.

name = input("Please enter name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)

##Using int() to accept numerical input:
age = input("How old are you? ")

#Using the input as a numeric value:
age = input("How old are you? ")
age >= 18# An error was the result of this line of code.
# To get around this problem the int() function allows you to convert,
#all character strings into integers.
int(age) >= 18# The output was assessed as true.

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nyou'll be able to ride when you're a little older.")

##The modulo operator:
#This operation uses the % syntax and is the same as the R syntax %/%. Which is 
#division with a remainder. 
print(4%3)
print(5%3)
print(6%2)
print(7%3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")