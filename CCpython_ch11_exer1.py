##11-1:
#For the module the contains the city_country function look at city_function.py.
#function city_country() found in the module city_functions.py.

import unittest 

from city_function import city_country

class CityCountryTest(unittest.TestCase):
	"""Tests for "city_function.py"."""

	def test_city_country(self):
		"""Does Santiago, Chile Work?"""
		formatted_city_country = city_country("santiago","chile")
		self.assertEqual(formatted_city_country, "Santiago, Chile")

unittest.main()#The following test passed.

##11-2

import unittest 

from city_function import city_country, city_country_pop

class CityCountryPopTest(unittest.TestCase):
	"""Tests for "city_function.py"."""

	def test_city_country_pop(self):
		"""Does Santiago, Chile Work?"""
		formatted_city_country = city_country_pop("santiago","chile")
		self.assertEqual(formatted_city_country, "Santiago, Chile")

unittest.main()#The following test failed because I forget to disclose 
#a population value with the city and country. (Or rather) I forgot to 
#create an if and else statement for instances that do have a population 
#and those that don't.

import unittest 

from city_function import city_country_pop

class CityCountryPopTest(unittest.TestCase):
	"""Tests for "city_function.py"."""
	def test_city_country(self):
		"""Does Santiago, Chile Work?"""
		formatted_city_country = city_country_pop("santiago","chile")
		self.assertEqual(formatted_city_country, "Santiago, Chile")

	def test_city_country_population(self):
		"""Does Santiago, Chile - population 500000 work?"""
		formatted_city_country = city_country_pop("santiago", "chile", 500000)
		self.assertEqual(formatted_city_country, "Santiago, Chile - Population 500000")

unittest.main()#Both tests seem to be running ok. 





