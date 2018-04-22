##Chapter 3 Introducing Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)# This data structure can be accessed through the [] syntax.

##Accessing Elements in a list:
print(bicycles[0])#this pulls out the object in the first index position.
print(bicycles[0].title())# Capitalizes the first letter of the first object.

##Index positions Start at 0, not 1:
print(bicycles[1])
print(bicycles[3])

#processing of the last element in a list.
print(bicycles[-1])
print(bicycles[-2])

##Using individual values from a list:
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

##Changing, Adding, and Removing Elements
##Modifying Elements in a List
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)#Just like in R.

##Adding elements to a list:
##Appending Elements to the end of a list:
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")# remember than when using append() you are placing 
#the new object at the end of the list.
print(motorcycles)

motor = []
motor.append("honda")
motor.append("yamaha")
motor.append("suzuki")
print(motor)

##Inserting Elements into a List
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)#through the insert() method you can insert a new object
#into any index position of an assigned list.

##Removing Elements from a list:
##Removing an item using the del statement:
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)# This removed the honda label (which was in index position
#1)

motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[1]
print(motorcycles)

##Removing an item using the pop() method:
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)# Now I understand the pop() method removes the 
#last object in the list and stores it within a new object.

##practical application:
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

##Popping items from any position in a list:
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print("the first motorcycle I owned was a " + first_owned.title() + ".")

##Removing an item by value:
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

##Organizing a list:
##Sorting a list permanently with the sort() Method:
cars = ["bmw","audi","toyota","subaru"]
cars.sort()#This method works just like the sort() function in R.
print(cars)# Sorts by default according to alphabetical order.
cars.sort(reverse = True)# Note to self, you don't have to capitalize true in 
#python. 
print(cars)#As you can see the order was reversed through the reverse = True
#argument.

##Sorting a list temporarily with the sort() function:
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again")
print(cars)

##Printing a List in reverse order:
cars = ["bmw","audi","toyota","subaru"]
print(cars)
cars.reverse()
print(cars)# Notice that this command simply reverses the order of the original 
#list. You can convert the list back to its original order through using 
#reverse() again.

##Finding the length of a list:
cars = ["bmw","audi","toyota","subaru"]
len(cars)
print(len(cars))

##Avoiding index errors when working with lists:
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[-1])





