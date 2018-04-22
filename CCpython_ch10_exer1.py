##10-1:
filename = "in_python.txt"

#Once in an enclosed with statement without the for loop:
with open(filename) as file_object:
	lines = file_object.read()
	print(lines)

#Once in an enclosed with statement with a for loop:
with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.strip())

#Once working with the object outside of the with statement:
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

##10-2:
#python substitution function example:
message = "I really like dogs."
message.replace("dog","cat")
#almost like gsub() but a little more straightforward.

with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.replace("python","R"))#Now I understand, unlike gsub()
		#the modifications with replace() are not permanent.





