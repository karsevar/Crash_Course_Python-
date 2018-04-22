##Storing your functions in modules:
##importing an entire module:
#(important) A module is a file ending in .py that contains the code you 
#want to import into your program. 

#Ok just created a new file called pizza.py (let's see if this works without)
#configuring my work directory).
import pizza 

pizza.make_pizza(16, "pepperoni")#Wow this actually worked.
pizza.make_pizza(12, "mushroom","green peppers","extra cheese")

##importing specific functions:
from CCpython_ch8_exer4 import car

toyota = car("toyota","mr2","white",year = 1989, vin = 222930384)
print(toyota)#this import statement worked just fine, but the only 
#problem is that the print() statements were imported into the session as 
#well. 

from pizza import make_pizza

make_pizza(16, "pepperoni")
#this function call seems to work just fine. Will need to 
#keep an eye on this.

##Using as to give a function an alias:
from pizza import make_pizza as mp 

mp(26, "pepperoni")
mp(12, "mushroom","cheese","goat cheese")

##Using as to give a module an alias:
import CCpython_ch8_exer2 as exer2

exer2.describe_city(city = "new york")# Now I understand, through the 
#from module import function syntax.
#The console imports the function's code base as well as all the instances 
#it is called in the module.

import pizza as p

p.make_pizza(16, "mushroom","pepperoni","olives")
p.make_pizza(12, "cheese")

##Importing all functions in a module:
from pizza import *

make_pizza(16, "pepperoni")

from CCpython_ch8_exer4 import *

mason = build_profile("mason", "karsevar", location = "spokane", 
				major = "american ethnic studies")
print(mason)#Interesting this function all only imported the base function code
#not the instances the function was called in the module.

##Styling functions:

