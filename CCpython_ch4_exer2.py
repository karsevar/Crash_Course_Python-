##4-3:
#for loop idea:
for value in range(1,21):
	print(value)

#list comprehension idea:
values = [value for value in range(1,21)]
print(values)# cool this worked.

##4-4:
print(1e6)# cool scientific notion is recognized in python.
for value in range(1, 1000001):
	print(value)# this is faster than R. 7.2 seconds.

##4-5:
million = [value for value in range(1, 1000001)]
print(min(million))
print(max(million))
print(sum(million))

##4-6:
odds = list(range(1, 21, 2))# Weird I had to use 2 for the third argument value.
print(odds)
for odd in odds:
	print(odd)

##4-7:
multiples = [value*3 for value in range(3, 31)]
print(multiples)
for multiple in multiples:
	print(multiple)

##4-8:
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
	print(cube)

##4-9:
cubes = [value**3 for value in range(1,11)]
print(cubes)



