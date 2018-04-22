##Chapter 11 Testing your code:
##Testing a function:
def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + " " + last
	return full_name.title()

print("enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == "q":
		break 
	last = input("Please give me your last name. ")
	if last == "q":
		break
	formatted_name = get_formatted_name(first, last)
	print("\tNeatly formatted name: " + formatted_name + ".")

def get_formatted_name(first, middle, last):
	"""Generate a neatly formatted full name."""
	full_name = first + " " + middle + " " + last 
	return full_name.title() 


##Unit tests and test cases:
#The module unittest is used to test one's code for wide spread use.

##A passing test:
import unittest
class NamesTestCase(unittest.TestCase):
	"""Tests for the get_formatted_name function"""
	def test_first_last_name(self):
		"""Do names like "janis joplin work?"""
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name, "Janis Joplin")

unittest.main()

##A failing test:
#rewritting the get_formatted_name() so that it can receive middle names.
#the following function is break when users want to only input their 
#first and last names.

import unittest
class NamesTestCase(unittest.TestCase):
	"""Tests for the get_formatted_name function"""
	def test_first_last_name(self):
		"""Do names like "janis joplin work?"""
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name, "Janis Joplin")

unittest.main()
#As such the program failed the janis joplin test.

##Responding to a failed test:
#Creating a default middle name value to fix the get_formatted_name() function
#call.
def get_formatted_name(first, last, middle = ""):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = first + " " + middle + " " + last 
	else:
		full_name = first + " " + last 
	return full_name.title()

import unittest
class NamesTestCase(unittest.TestCase):
	"""Tests for the get_formatted_name function"""
	def test_first_last_name(self):
		"""Do names like "janis joplin work?"""
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name, "Janis Joplin")

unittest.main()

##Adding New tests:
#Testing instances with middle names:
import unittest

class NamesTestCase(unittest.TestCase):
	"""Tests for the get_formatted_name function"""
	def test_first_last_name(self):
		"""Do names like "janis joplin work?"""
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name, "Janis Joplin")
	def test_first_last_middle_name(self):
		"""Do names like 'Wolf Amadeus Mozart' work?"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart") 

unittest.main()

##Testing a class:
##A Variety of Assert methods:
#Look at page 223 to see the six different assert functions used for verifying 
#classes.

##A Class to test:
class Anonymous_Survey():
	"""Collect anonymous answers to a survey question."""
	def __init__(self, question):
		"""Store a question, and prepare to store responses."""
		self.question = question 
		self.responses = []
	def show_question(self):
		"""show the survey question."""
		print(self.question)
	def store_response(self, new_response):
		"""Store a single response to the survey."""
		self.responses.append(new_response)
	def show_results(self):
		"""show all the responses that have been given."""
		print("Survey results:")
		for response in self.responses:
			print("- " + response)

#Define a question, and make a survey:
question = "What language did you first learn to speak? "
my_survey = Anonymous_Survey(question)

#Show the question, and store responses to the question.
my_survey_question()
print("Enter 'q' at any time a quit. \n")
while True:
	response = input("Language: ")
	if response == "q":
		break 
	else:
		my_survey.store_response(response)

#show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

##Testing the AnonymousSurvey class:
#unittest test of the Anonymous_Survey() class.
import unittest

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the class AnonymousSurvey"""

	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response("English")

		self.assertIn("English", my_survey.responses)

unittest.main()

#multiple response storage test:
import unittest

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the class AnonymousSurvey"""

	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response("English")

		self.assertIn("English", my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		question = "What language did you learn first? "
		my_survey = AnonymousSurvey(question)
		responses = ["English","Spanish","Mandarin"]
		for response in responses:
			my_survey.store_responses(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)

unittest.main()
#Both tests run perfectly without any errors.

##The setup() method:
import unittest

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""
	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ["English","Spanish","Mandarin"]

	def test_store_single_response(self):
		"""Test that a single response is stored properly"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self_responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()





