##7-4:
prompt = "Hello young customer!!!"
prompt += "Welcome to pizza bro, the first automated pizza takeout service."
prompt += "What crust style and topping do you want on your pizza this evening? "
while topping != "quit":
	topping = input(prompt)
	print("Adding " + topping + " to your pizza.")
#This loop works, but it's rather crude. Will modify the code assembly a 
#little more.

print("Hello young customer!!!")
print("Welcome to pizza bro, the first automated pizza takeout service.")
prompt = "What topping do you want on your pizza this evening? "
condition = True
while condition == True:
	topping = input(prompt)
	if topping == 'quit':
		condition = False
	else: 
		print("Adding " + topping + " to your pizza!")
#This while loop is more polished than the one above.

##7-5:
print("Welcome to movie me!!!")
print("Before we get started with which movie you") 
print("would like to watch this evening.")
while True:
	age = input("How old are you? ")
	age = int(age)
	if age < 3:
		print("Your movie charge this evening is $0.")
		break
	elif age < 12:
		print("Your movie charge this evening is $10.")
		break
	elif age > 12:
		print("Your movie charge this evening is $15.")
		break
#this loop works just fine, but the three different break commands is a little too
#clunky. will need to think of another alternative.

print("Welcome to movie me!!!")
print("Before we get started with which movie you") 
print("would like to watch this evening.")
charge = int()
while True:
	age = input("How old are you? ")
	age = int(age)
	if age < 3:
		charge = 0
	elif age <= 12:
		charge = 10
	elif age > 12:
		charge = 15
	break
print("Your charge this evening is $" + str(charge) + ".")
#Important addition, the charge object needed to be defined before 
#being rewritten within while loops. This little addition is just like R 
#programming.

##7-6:
#condition while loop:
print("Hello young customer!!!")
print("Welcome to pizza bro, the first automated pizza takeout service.")
prompt_1 = "What style crust would you like? "
prompt_2 = "What topping do you want on your pizza this evening? "
condition = True
crust = input(prompt)
print("You have ordered " + crust + " pizza!")
while condition == True:
	topping = input(prompt_2) 
	if topping == 'quit':
		condition = False
	else: 
		print("Adding " + topping + " to your pizza!")
		print("Please enter 'quit' if you don't require anymore toppings.")
#Will need to think a little more about what to do with the crust loop and
#how to display the customer's order once they are done with the while loop.

#Active variable while loop:
#this time topping will be a list 'toppings'.
print("Hello young customer!!!")
print("Welcome to pizza bro, the first automated pizza takeout service.")
prompt_1 = "What toppings would you like? "
toppings = []
while len(toppings) <= 10:
	topping = input(prompt_1)
	toppings.append(topping) 
	print("Adding " + topping + " to your pizza!")
	print("Please enter another topping. ")
#the loop stops after 11 topping inputs. I can't believe this works. 

#break statement:
print("Hello young customer!!!")
print("Welcome to pizza bro, the first automated pizza takeout service.")
prompt_1 = "What toppings would you like? "
toppings = []
while len(toppings) <= 10:
	topping = input(prompt_1)
	if topping == "quit":
		break
	toppings.append(topping) 
	print("Adding " + topping + " to your pizza!")
	print("Please enter another topping. ")
	print("Or enter 'quit' if you don't require anymore toppings.")
	

##7-7:
print("Hello young customer!!!")
print("Welcome to pizza bro, the first automated pizza takeout service.")
prompt_1 = "What toppings would you like? "
toppings = []
while len(toppings) <= 10:
	topping = input(prompt_1)
	toppings.append(topping) 
	print("Adding " + topping + " to your pizza!")
	print("Please enter another topping. ")
	print("Or enter 'quit' if you don't require anymore toppings.")
	if len(toppings) == 10:
		toppings.pop()#this command make sure that the loop will never end.
#len(toppings) will never reach the while loop break condition.





