##5-1:
car = "mclaren f1"
supercar = ["mclaren f1","audi r8","mercedes slr","ford gt","keoniggzag","ferrari f12"]
economy_car = ["ford fiesta","mini cooper","chevy sonic","toyota prius","toyota corolla"]
print("Is car == supercar? I predict true.")
print(car in supercar)

print("\nIs car == economy car? I predict False.")
print(car in economy_car)

car = "mini cooper"
print("\nIs car == economy? I predict true.")
print(car in economy_car)

car = "ford gt"
print("\nIs Ford gt not an economy car? I predict true.")
print(car not in economy_car)

car = "chevy sonic"
print("\nIs chevy sonic not a supercar? I predict false.")
print(car not in supercar)

car = "ford fiesta"
print("\nIs car == 'ford fiesta'? I predict true.")
print(car == "ford fiesta")

car = "toyota prius"
print("\nIs car == mini cooper? I predict false")
print(car == "mini cooper")

car = "ford fiesta"
print("\nIs ford fiesta a supercar? I predict false.")
print(car in supercar)

car = "keoniggzag"
print("\nIs keoniggzag an economy car? I predict false.")
print(car in economy_car)

car = "toyota prius"
print("\nIs toyota prius an supercar car? I predict false.")
print(car in supercar)

##5-2
#in operator commands:
fav_foods = ["pizza","cake","steak","salmon","lamb"]
not_favs = ["crab","chicken","hot pockets","ramen"]
print("crab" not in fav_foods)
print("pizza" in fav_foods)
print("chicken" in fav_foods)

#equality and unequality:
not_food = "humans"
food = "fish"
print(not_food == "dogs")
print(not_food == "humans")
print(food != "fish")

#Numerical tests:
grade_0 = 3.8
grade_1 = 2.0
grade_2 = 0.2
grade_3 = 3.4
print(grade_0 == grade_1)
print(grade_0 > grade_3)
print(grade_1 != grade_2)
print(grade_3 >= 3.6)
print(grade_3 <=3.8)
print(grade_3 < grade_1)

#Using lower() function:
cars = ["bmw","mercedes","toyota","mazda"]
car_0 = "BMW"
car_1 = "Toyota"
car_2 = "Ford"
car_3 = "Mazda"
car_4 = "Jeep"
print(car_0.lower() in cars)
print(car_1.lower() and car_3.lower() in cars)
print(car_2.lower() and car_0.lower() in cars)# that's weird this command should
#have been assessed as false. Will need to look into this.
print(car_2.lower() in cars)
print("jeep" and "chrysler" in cars)# Interestingly this command works perfectly.
print(car_4.lower() not in cars)

#Using and or key syntax:(I think I have an idea of how I can fix the upper 
#and / or commands.)
print(car_2.lower() in cars or car_0.lower() in cars)
print(car_2.lower() in cars and car_0.lower() in cars)#This is the proper way
#to combine in list commands and the or/and syntax.
print(car_0.lower() == "toyota" or car_2.lower() == "ford")
print(car_0.lower() == "toyota" and car_2.lower() == "ford")








