##8-1:
def display_message():
	"""displays a simple message on chapter 8"""
	print("In chapter 8 I'm learning about functions.")
	print("Mainly how to write proper functions and use these function calls")
	print("as modules within larger code chunks. This chapter will allow me")
	print("to write more intelligeable code that is easier to debug.")

display_message()

##8-2:
def favorite_books(books):
	"""Displays list of favorite books"""
	if len(books) > 1:
		print("\nMy favorite books are: ")
		for book in books:
			print("\t" + book)
	else:
		book = str(books)
		print("\n My favorite book is: ")
		print("\t" + book)


favorite_books(books = ["Book of R", "R for Data Science", "Crash Course Python", 
						"Introduction to statistical learning"])
favorite_books(books = ["Book of R"])
#The list function calls work just fine, but the single string function calls
#might need so work. The function prints each letter of a string object. 