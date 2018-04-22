##4-10:
pizzas = ["greek","hawaiian","vegetarian","meat lover","sausage","canadian bacon"]
print("The first three pizza styles are:")
for pizza in pizzas[:3]:
	print(pizza)
#That's weird, the command pizza[:3] actually printed the first three pizza styples
#I that the index should be written pizzas[:2].
print("Three items from the middle of the list:")
for pizza in pizzas[1:4]:
	print(pizza)

#Another interpretation of what the middle of the list entails.
print("\nThree items from the middle of the list:")
for pizza in pizzas[2:5]:
	print(pizza)

print("\nThe last three styles in the list are:")
for pizza in pizzas[-3:]:
	print(pizza)

##4-11:
pizzas = ["greek","hawaiian","vegetarian","meat lover","sausage","canadian bacon"]
pizzas.append("onion")
friend_pizzas = pizzas[:]
friend_pizzas.append("chocolate chip")
print("\nMy favorite styles are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizza styles are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

