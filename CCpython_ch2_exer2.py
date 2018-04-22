##2-3.
first_name = "Eric"
last_name = "Schaffer"
message = "Hello, " + first_name + " " + last_name + ", \nI know that we didn't part in the best of terms. \nBut I'm just wondering, would you mind helping me with my CS problem sets?"
print(message)

##2-4 
first_name = "Eric"
last_name = "Schaffer"
print(first_name.lower() + " " + last_name.lower())
print(first_name.upper() + " " + last_name.upper())
first_name = "eric"
last_name = "schaffer"
print(first_name.title() + " " + last_name.title())

##2-5 
name = "a homeless guy"
message = 'once said, "You will be down here some day."'
print(name.title() + " " + message)

##2-6
famous_person = "a toilet stall message"
message = 'once said, "same shit different day."'
print(famous_person.title() + " " + message)
message = famous_person.title() + " " + message
print(message)

##2-7 
first_name = "\n\tPhil  "
last_name = "   Johnson   "
print(first_name + " " + last_name)
print(first_name.strip() + " " + last_name.strip())