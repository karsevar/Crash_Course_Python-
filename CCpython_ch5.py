### Chapter 5 If statements:
##A simple Example
cars = ["bmw","audi","subaru","toyota"]
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())
#pretty cool piece of code, and it's way more straight forward than the R
#language alternative:
#R sample:
#cars <- c("bmw","audi","subaru","toyota")
#for (i in 1:length(cars)){
	#if(cars[i] == "bmw"){
		#print(paste(toupper(substr(cars[i],1,3)), sep = ""))
	#}else{
		#print(paste(toupper(substr(cars[i],1,1)), substr(cars[i], 2, nchar(cars[i])), sep = ""))
	#}
#}
# As you can see R is more complicated to deal with than python.

##conditional tests:
##Checking for equality (or rather boolean mathematics)
car = "bmw"
print(car == "bmw")# the result was true.
car = "audi"
print(car == "bmw")#The result was false since the car object was set to audi.

##Ignoring Case when checking for equality:
car = "Audi"
print(car == "audi")#the result was false. 
#Boolinean mathematics is case sensitive.

car = "Audi"
print(car.lower()=="audi")
print(car)

##Checking for inequality:
requested_topping = "mushroom"
if requested_topping != "achovies":
	print("Hold the anchovies")
#cool the != operator is the same as r.

##Numerical comparisons:
age = 18
print(age==18)
answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again.")
age = 19
print(age < 21)
print(age <=21)
print(age > 21)
print(age >= 21)

##Checking multiple conditions: (Sweet the author is finally talking about
#or / and statements with boolean mathematics)
##Using and to check multiple conditions:
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
#In R programming this statement is written as:
#age_0 >= 21 & age_1 >= 21: in this case the & symbol needs to be used.

age_1 = 21
print(age_0 >= 21 and age_1 >= 21)#this time the command was assessed as true.
#With that said though, I wonder if python has elemental and singular and / or 
#commands like R. singular (&&/||) and elemental (&/|).
print((age_0 >= 21) and (age_1 >= 22))

##Using or to check multiple conditions.
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

##Checking whether a value is in a list:
requested_toppings = ["mushrooms","onions","pineapple"]
print("mushrooms" in requested_toppings)# The R equivalent of this command is 
#mushrooms %in% requested_toppings.
print("pepperoni" in requested_toppings)

##checking whether a value is not in a list:
banned_users = ["andrew","carolina","david"]
user = "marie"
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
#the R equivalent:
#banned_users <- c("andrew","caronlina","david")
#user <- "marie"
#for(i in 1:length(banned_users)){
#	if(user != banned_users[i]){
#		print("you can post a response if you wish.")
#	}
#} 
# Found something really interesting with R if() statements, will need to
#experiment further.

##Boolean Expressions:
game_active = True
can_edit = False

##If statements:
age = 19
if age >= 18:
	print("You are old enough to vote!")

age = 19
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")

#fun little alternative to the preceeding code strings:
age = 17
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")
else:
	print("You are not old enough.")
	print("Please register in " + str(18-age) + " years.")

##If-else statements:
age = 17 
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18.")

##The if-elif-else chain:
#idea for how the elseif python equivalent syntax is written.
age = 12
if age < 4:
	print("Welcome to Hell!!!")
	print("Due to your age being below 4, your admission is $0.")
	print("I hope you enjoy your visit.")
elif 4 <= age and age <= 18:
	print("Welcome to Hell!!!")
	print("Since you age is " + str(age) + ",")
	print("your admissions fee will be 5 dollars.")
	print("I hope you enjoy your stay.")
else:
	print("Welcome to Hell!!!")
	print("Due to your age being " + str(age) + ",")
	print("your admission fee will be 10 dollars.")
	print("I hope you enjoy your stay.")
#Nice this actually worked!!! This almost has the same syntax as the R 
#programming language.

age = 3
if age < 4:
	print("Welcome to Hell!!!")
	print("Due to your age being below 4, your admissions fee is $0.")
	print("I hope you enjoy your visit.")
elif 4 <= age and age <= 18:
	print("Welcome to Hell!!!")
	print("Since you age is " + str(age) + ",")
	print("your admissions fee will be 5 dollars.")
	print("I hope you enjoy your stay.")
else:
	print("Welcome to Hell!!!")
	print("Due to your age being " + str(age) + ",")
	print("your admission fee will be 10 dollars.")
	print("I hope you enjoy your stay.")

age = 17
if age < 4:
	print("Welcome to Hell!!!")
	print("Due to your age being below 4, your admission is $0.")
	print("I hope you enjoy your visit.")
elif 4 <= age and age <= 18:
	print("Welcome to Hell!!!")
	print("Since you age is " + str(age) + ",")
	print("your admissions fee will be 5 dollars.")
	print("I hope you enjoy your stay.")
else:
	print("Welcome to Hell!!!")
	print("Due to your age being " + str(age) + ",")
	print("your admission fee will be 10 dollars.")
	print("I hope you enjoy your stay.")


#Author's if-elif-else statement idea:
age = 12
if age < 4:
	price = 0 
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + ".")# Awesome idea!! I can't believe
#I didn't think of this.

#if-elif-else remake:
age = 40
if age < 4:
	price = 0 
elif age < 18:
	price = 5
else:
	price = 10
print("Welcome to Hell!!!")
print("Due to your age being " + str(age) + ",")
print("your admissions fee is $"+str(price)+".")
print("We hope you enjoy your stay.")
print("Sincerely,\nmanagement")

##Using mutliple blocks:
age = 70
if age < 4:
	price = 0 
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".")
#This modification creates a senior discount option.

##omitting the else block:
age = 12
if age < 4:
	price = 0 
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
print("Your admission cost is $" + str(price) + ".")

##Testing multiple Conditions:(This looks similar to lazy nested if() statements
#(or rather evaluation)).
requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
	print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
	print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
	print("Adding extra cheese")

print("\nFinished making your pizza.")

#if-elif-else statement alternative:
requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
	print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
	print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
	print("Adding extra cheese")

print("\nFinished making your pizza.")# Only mushrooms was assessed and not
#extra cheese. 

##Using if statements with lists:
requested_toppings = ["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
	print("adding " +requested_topping + ".")
print("\nFinished making your pizza.")

#Nested if statement within a for loop:
requested_toppings = ["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
	if requested_topping == "green peppers.":
		print("Sorry, we're out of green peppers.")
	else:
		print("adding " +requested_topping + ".")
print("\nFinished making your pizza.")

##Checking that a list is not empty:
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

##Using multiple lists:
available_toppings = ["mushrooms","olives","green peppers","pepperoni",
"pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries ","extra cheese"]

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza.")








