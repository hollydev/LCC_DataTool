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
from messages.system import VALIDATORS, SYSTEM
import re

class NUMERIC_ID:
	def __init__(self, column):
		self.validate = system.VALIDATORS()
		self.validated = system.SYSTEM()

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
			# 		warnings.append(system.VALIDATORS.notUniqueDup % (indexes[1],
			# 															indexes[2]))
			# 	elif len(indexes) > 2:
			# 		warnings.append(warnings.VALIDATORS.notUniqueMult % (indexes))

			
			#Validate Length (convert value to string and remove the brackets)
			if len(str(value)[1:-1]) != length:
				self.warnings.append(self.validate.length % (value, len(value), length))

	def statistics(self):
		return(self.validated.validatorStats % ("Numeric ID", self.items, len(self.warnings), len(self.errors)))

	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)

class MIXED_TEXT:

	def __init__(self, column):
		self.validate = system.VALIDATORS()
		self.validated = system.SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.column = column
		self.values = column.values
		self.items = 0

	def run(self):

		for value in self.values:
			
			self.items += 1

			#Check that the cell is not empty
			if value != value:
				self.warnings.append(self.validate.expectedNonEmpty % value)
				

	def statistics(self):
		return(self.validated.validatorStats % ("Mixed ID", self.items, len(self.warnings), len(self.errors)))
	
	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)


class PLAIN_TEXT:

	def __init__(self, column):
		self.validate = system.VALIDATORS()
		self.validated = system.SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.column = column
		self.values = column.values
		self.items = 0

	def run(self):

		for value in self.values:

			self.items += 1

			#check that the cell is not empty
			if(value != value):
				self.warnings.append(self.validate.expectedNonEmpty % str(value)[1:-1])

			#check that it contains no digits
			if(bool(re.search(r'\d', str(value))) == True):
				self.warnings.append(self.validate.expectedTextOnly % value)

			#check that it contains no symbols
			if(bool(re.search(r'[@_!#$%^&*()<>?/\|}{~:\"]', str(value)[1:-1])) == True):
				self.warnings.append(self.validate.expectedNoSymbols % value)

	def statistics(self):
		return(self.validated.validatorStats % ("PlainText", self.items, len(self.warnings), len(self.errors)))

	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)


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