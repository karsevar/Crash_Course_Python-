## Chapter 4 Working with Lists:
##Looping through entire lists: I hope that I learn how to control the looping index 
#position (just like in the R programming language).
magicians = ["alice","david","caroline"]
for magician in magicians:
	print(magician)
#Interesting in place of the index [i] within the loop assembly, 
#for(i in 1:length(magicians)), all you need to do is change magicians into 
#the singular tense. Very interesting. 
#According to the author the for loop allows you to create a new object within 
#the assembly, unlike R. So in other words, the index elements of magicians are 
#being stored within the new object magician. This is why my previous loops 
#were stuck on the last index position of the list.
print(magicians)
print(magician)#As suspected the magician object only stored the last name from 
#the list "caroline"

#(important) Using singular and plural names can help you identify whether a 
#section of code is working with a single element from the list or the entire
#list.

##Doing more work within a for loop:
magicians = ["alice","david","caroline"]
for magician in magicians:
	print(magician.title() + ", that was a great trick!")

magicians = ["alice","david","caroline"]
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("thank you, everyone. This was a great magic show!")#It's important 
#to keep in mind that indentation within python is just like the {} 
#operators within R. This means that indentation tells the console 
#which elements you want included within a loop. 

##Using the range() function:
for value in range(1,5):
	print(value)
#the output of range() is the same as the seq() function in R and the :
#syntax.

#remember that due to python's staggered indexing characteristic. The preceeding
#range() string ends at 4 in place of 5.

for value in range(1,6):
	print(value)# To offset this quirk, you need to end the sequence by 
	#going over one value. Like the operation above.

##Using range() to make a list of numbers:
numbers = list(range(1,6))
print(numbers)# the list method is just like the as.list() and as.vector() function
#in R.

even_numbers = list(range(2,11,2))
print(even_numbers)# just like seq(from = 2, to = 10, by = 2) operation in R.

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)
#Again python doesn't really care if the square or value objects existed before
#the loop. This is a very useful characteristic to this language.

squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)
#This has the same output as the loop above with less lines.

digits = list(range(0, 11))
print(min(digits))
print(max(digits))# Same functions as R.
print(sum(digits))
print(digits)

##List Comprehensions:
squares = [value**2 for value in range(1,11)]
print(squares)#It has the same output as the for loops above. 

##working with part of a list:
##Slicing a list: (This sounds a lot like indexing)
players = ["charles","martina","michael","florence","eli"]
print(players[0:3])#prints the firs three positions in the list.

print(players[1:4])#this line is for the second and third positions in the list.

print(players[:4])#this characteristic looks a lot like the matrix computation
#computer language (matlab). Without a starting index, the command starts at 
#the beginning of the list by default.

print(players[2:])#Same characteristic as the omitting the beginning index.

print(players[-3:])#This prints the names of the last three players as well.

##Looping through a slice:
players = ["charles","martina","michael","florence","eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

##copying a list:
my_food = ["pizza","falafel","carrot cake"]
friend_foods = my_food[:]#This copies the entire list of my_food into the new
#list object.
print("My favorite foods are:")
print(my_food)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

##Not using the index syntax [:] 
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods #This will cause friend_foods and my_foods to mirror
#each other. They will both share ice cream and cannoli. 
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#Interesting, this really isn't a problem with R as the command my_food = friend_foods 
#will just assume that you want to elements to be copied into my_food at that 
#moment. They are both regarded a separate entities within the R console.

##Tuples:
##Defining a Tuple: They are immutable (they can not be changed):
dimensions = (200,50)# Tuples are created through the () syntax.
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)

##Writing over a tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)











