print("hello world")
message = "hello humans"
print(message)# this is again just like the object oriented environment with R, but faster
message = "hello humans, greetings from python world"
print(message)# wow the interpreter processes the objects in the console sequencially

##error practice:
mesage = "hello python world dude"
print(mesage)#important detail to keep in mind, python can't ignore errors. Hence error
#ridden lines have to be removed before creating new lines of code. 

##strings 
"This is a string."
'This is also a string'# important to keep in mind, strings can't be printed onto the 
#console through the interpreter without the function print() this is different from R.

##changing Case in a string with methods:
name = "ada lovelace"
print(name.title())#the title displays each word in lowercase, where each word begins
#with a capital letter. this is especially helpful with names.

#the methods upper() and lower():
print(name.lower())# this method is good for storing names and titles within a dataframe.
print(name.upper())

##combining or Concatenating strings:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + "" + last_name
print(full_name)#no it's important to write "" as " " because you might want a space 
#between the first and last names. this is the same thing as sep = " " in R.
full_name = first_name + " " + last_name
print(full_name.title())
#this method is called concatenation.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

##Adding Whitespace to strings with Tabs or Newlines:
print("Python")
print("\tPython")# this is almost the same as R except the \t command is written in escape 
#notation and you need to use the command cat() for it to work properly.
print("Languages: \nPython\nC\nJava")# The same as R except again the cat() function 
#needs to be used.

##Stripping whitespace:
#the method used to strip whitespace in python is rstrip() and lstrip() for the right side
#and left side respectively.
favorite_language = '  python  '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())#strip() is used to take away white space from both sides.

##Numbers
##integers
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

print(3 ** 2)# the R equivalent is 3^2 
print(3 ** 3)
print(10 ** 6)

#order of operations:
print(2 + 3*4)
print((2+3) * 4)

##floats:
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

##Avoiding Type Errors with the str() function:
#This command resulted in an error message.
# Now I understand, within the python language age = 23 is an integer and 
#can't be combined with a string message.

#You can change age from a integer into a string through the str() method
age = 23 
message = "Happy " + str(age) + "rd Birthday"
print(message)

##comments:
#Say hello to everyone.
print("Hello Python people")

##The Zen of python programming 
import this #this command gives you the passages of the philosophy.










