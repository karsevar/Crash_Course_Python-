##11-3:
class Employee():
	"""Creates a class named employee"""
	def __init__(self, first, last, salary):
		"""Initializes the arguments first, last, and salary"""
		self.first = first 
		self.last = last 
		self.salary = salary

	def format_name(self):
		"""Formats first and last name"""
		self.full_name = self.first + " " + self.last
		 

	def give_raise(self, increase = 5000):
		"""Gives raise to employee if called. Default 5000."""
		self.increase = increase 
		self.salary += increase
		

employee1 = Employee("mason","karsevar",10000)
print(employee1.format_name())#Cool format name works
employee1.give_raise()#the give_raise() function works with the default 
#amount 
employee1.give_raise(1000)#The give_raise() method also works with a custom 
#amount. 

#According to primitive tests, this class functions perfectly. 

##Unittest class:
import unittest

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""

	def setUp(self):
		"""
		Create test employee data for all methods in Employee class.
		"""
		self.mason = Employee("mason","karsevar",10000)

	def test_give_default_raise(self):
		"""Test that give raise function actuall gives 5000 by default"""
		self.mason.give_raise() 
		self.assertEqual(self.mason.salary, 15000)

	def test_give_raise_custom(self):
		self.mason.give_raise(1000)
		self.assertEqual(self.mason.salary, 11000)

	def test_format_name(self):
		self.mason.format_name()
		self.assertEqual(self.mason.full_name, "mason karsevar")

unittest.main()






