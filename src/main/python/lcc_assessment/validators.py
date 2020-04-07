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
from messages.validators import VALIDATORS
from messages.system import SYSTEM, LOG
import datetime
import re

class NUMERIC_ID:
	def __init__(self, column):
		self.validate = VALIDATORS()
		self.validated = SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.values = column
		self.name = column.name
		self.length = len(self.values)
		self.items  = 0

	def run(self, length):

		for value in self.values:
			#Count Items
			self.items += 1
			
			#Validate Numeric (convert to string and remove brackets)
			if not numpy.char.isnumeric(str(value)[1:-1]):
				self.warnings.append(self.validate.notNumeric % (value, self.items))
				

			#Validate Length (convert value to string and remove the brackets)
			if len(str(value)) != length:
				self.warnings.append(self.validate.length % (value, len(str(value)), length, self.items))

	def statistics(self):
		return(self.validated.validatorStats % (self.name, "Numeric ID", self.items, len(self.warnings), len(self.errors)))

	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)

class MIXED_TEXT:

	def __init__(self, column):
		self.validate = VALIDATORS()
		self.validated = SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.values = column
		self.name = column.name
		self.items = 0

	def run(self):

		for value in self.values:
			
			self.items += 1

			#Check that the cell is not empty
			if value != value:
				self.warnings.append(self.validate.expectedNonEmpty % (value, self.items))

	def statistics(self):
		return(self.validated.validatorStats % (self.name, "Mixed ID", self.items, len(self.warnings), len(self.errors)))
	
	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)


class PLAIN_TEXT:

	def __init__(self, column):
		self.validate = VALIDATORS()
		self.validated = SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.values = column.values
		self.name = column.name
		self.items = 0

	def run(self):

	
		for value in self.values:

			self.items += 1

			#check that the cell is not empty
			if(value != value):
				self.warnings.append(self.validate.expectedNonEmpty % (str(value)[1:-1], self.items))

			#check that it contains no digits
			if(bool(re.search(r'\d', str(value))) == True):
				self.warnings.append(self.validate.expectedTextOnly % (value, self.items))

			#check that it contains no symbols
			if(bool(re.search(r'[@_!#$%^&*()<>?/\|}{~:\"]', str(value)[1:-1])) == True):
				self.warnings.append(self.validate.expectedNoSymbols % (value, self.items))

	def statistics(self):
		return(self.validated.validatorStats % (self.name, "PlainText", self.items, len(self.warnings), len(self.errors)))

	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)

class DATE:

	def __init__(self, column):

		self.validate = VALIDATORS()
		self.validated = SYSTEM()

		self.warnings = list()
		self.errors = list()
		self.values = column
		self.name = column.name
		self.r = re.compile(r'\d{4,4}-\d{2,2}-\d{2,2}T\d{2,2}:\d{2,2}:\d{2,2}.\d{3,3}')
		self.items = 0

	def run(self):

		
		for value in self.values:
			self.items += 1
			if(self.r.match(str(value)) == None):
				self.warnings.append(self.validate.unexpectedFormat % (value, self.items))

	
	def statistics(self):
		return(self.validated.validatorStats % (self.name, "Date", self.items, len(self.warnings), len(self.errors)))

	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)


class CRN:
	def __init__(self, column, allSections):
		self.validate = VALIDATORS()
		self.validated = SYSTEM()
		self.warnings = list()
		self.errors = list()
		self.values = column
		self.name = column.name
		self.items = 0

	def run(self):

		print("validate CRN")	

	def statistics(self):
		return(self.validated.validatorStats % (self.name, "CRN", self.items, len(self.warnings), len(self.errors)))

	def get_warnings(self):
		return(self.warnings)

	def get_errors(self):
		return(self.errors)


		


# class SECTION_CODE:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# def run(cls, termColumn):

# class GRADE_ITEM_CATEGORY:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():

# class GRADE_ITEM_NAME:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):

# 	def run():
		
# class GRADE_VALUE:
# 	warnings = list()
# 	errors = list()

# 	def __init__(self, column):
# 		self.column = column

# 	def run():
