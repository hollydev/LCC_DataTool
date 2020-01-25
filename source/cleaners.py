"""
	Filename: cleaners.py
	Programmer: Holly Locke
	Date Created: 01/02/2020
	Last Update: File Created

	Description: This file contains all cleaning logic that may be applied to the columns. 
	Built to work with the rest of the data tool, cleaners are created as classes.

"""
from messages.cleaners import cleaners

# """Remove all non-numeric values."""
# class NUMERIC_ID:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class MIXED_ID:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class PLAIN_TEXT:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class MIXED_TEXT:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class SECTION_CODE:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class GRADE_ITEM_CATEGORY:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

class GRADE_ITEM_NAME:
	messages = list()
	errors = list()

	def __init__(self, column):
		self.column = column
		self.values = column.values

	def run(self, threshold):
		#Get lexicon
		uniqueWords = set()
		for word in self.values: uniqueWords.add(word)
		
		#Nearest Distance
		viableEdits = list()
		editList = dict()
		
		#Iterate over the lexicon, finding words that fit within the edit distance threshold
		for item in self.values:
			for word in uniqueWords:
				distance = editdistance.eval(item, word)
				if word != item and distance < threshold:
					viableEdits.append(word)
					
			editList[item] = viableEdits
			viableEdits = list()


# class GRADE_VALUE:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class DATE:
# 	messages = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():