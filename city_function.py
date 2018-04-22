#The following module contains a function that formats a city and country string 
#into (city, country). Function from chapter 11 page 222

def city_country(city, country):
	result = city + ", " + country
	return result.title()

def city_country_pop(city, country, population):
	result = city + ", " + country + " - population " + str(population)
	return result.title()

def city_country_pop2(city, country, population = ""):
	if population:
		result = city + ", " + country + " - population " + str(population)
	else:
		result = city + ", " + country
	return result 
	


