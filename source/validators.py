"""
	Filename: validators.py
	Programmer: Holly Locke
	Date Created: 01/02/2020
	Last Update: File Created

	Description: This file contains all validation logic that may be applied to the columns. 
	Built to work with the rest of the data tool, validators are created as classes.

"""
import numpy
import pandas

import messages

class NUMERIC_ID:
	def __init__(self, column, length, unique=True):
		warnings = list()
		errors = list()

		self.column = column
		self.values = column.values
		self.length = length
		self.unique = unique
		self.items  = 0

	def run():
		#Check unique values using pandas
		if self.unique == True and not self.column.nunique() == len(self.column):
			findUnique = True
					
		for value in self.values:
			#Count Items
			items += 1
			
			#Validate Numeric
			if not numpy.char.numeric(value):
				warnings.append(warnings.VALIDATORS.notNumeric % value)

			#Validate Unique 
			if findUnique == True:
				indexes = numpy.where(self.values == value)
				if len(indexes) == 2:
					warnings.append(warnings.VALIDATORS.notUniqueDup % (indexes[1],
																		indexes[2]))
				elif len(indexes) > 2:
					warnings.append(warnings.VALIDATORS.notUniqueMult % (indexes))

			#Validate Length
			if len(value) != self.length:
				warnings.append(warnings.VALIDATORS.length % (len(value), length))

	def statistics():
		return(warnings.SYSTEM.validatorStats % ("Numeric ID", self.items, len(self.warnings), len(self.errors)))

# class MIXED_ID:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class PLAIN_TEXT:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class MIXED_TEXT:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class SECTION_CODE:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class GRADE_ITEM_CATEGORY:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class GRADE_ITEM_NAME:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column)::

# 	def run():
		
# class GRADE_VALUE:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class DATE:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():