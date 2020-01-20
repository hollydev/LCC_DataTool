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
	def __init__(self, column):
		self.validate = messages.VALIDATORS()
		self.validated = messages.SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.column = column
		self.values = column.values
		self.length = len(self.column)
		self.items  = 0

	def run(self, length):
		#Check unique values using pandas
		#if self.unique == True and not self.column.nunique() == len(self.column):
			#findUnique = True
					
		for value in self.values:
			#Count Items
			self.items += 1
			
			#Validate Numeric (convert to string and remove brackets)
			if not numpy.char.isnumeric(str(value)[1:-1]):
				self.warnings.append(self.validate.notNumeric % value)
				

			#Validate Unique 
			# if findUnique == True:
			# 	indexes = numpy.where(self.values == value)
			# 	if len(indexes) == 2:
			# 		warnings.append(messages.VALIDATORS.notUniqueDup % (indexes[1],
			# 															indexes[2]))
			# 	elif len(indexes) > 2:
			# 		warnings.append(warnings.VALIDATORS.notUniqueMult % (indexes))

			
			#Validate Length (convert value to string and remove the brackets)
			if len(str(value)[1:-1]) != length:
				self.warnings.append(self.validate.length % (value, len(value), length))

	def statistics(self):
		return(self.validated.validatorStats % ("Numeric ID", self.items, len(self.warnings), len(self.errors)))

class MIXED_ID:

	def __init__(self, column):
		self.validate = messages.VALIDATORS()
		self.validated = messages.SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.column = column
		self.items = 0
		self.values = column.values

	def run(self):

		for value in self.values:
			
			self.items += 1

			#Check for nan values
			if value != value:
				self.warnings.append(self.validate.expectedNonEmpty % str(value)[1:-1])

	def statistics(self):
		return(self.validated.validatorStats % ("Mixed ID", self.items, len(self.warnings), len(self.errors)))






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