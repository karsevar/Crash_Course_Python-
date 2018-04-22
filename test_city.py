##the following module contains a unittest function that is used to unit test 
#function city_country() found in the module city_functions.py.

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

unittest.main()