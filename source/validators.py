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

import warnings.VALIDATORS

class NUMERIC_ID:
	warnings = list()
	errors = list()

	def __init__(self, column, length, unique=True)
		self.column = column
		self.length = length
		self.unique = unique

	def run():
		#Assert Numeric
		values = column.values
		
		for value in values:
			if not numpy.char.numeric(value):
				warnings.append(warnings.VALIDATORS.notNumeric % value)

		#Assert Unique
		if unique == True:
			#Check unique values using pandas
			if not column.nunique() == len(column):
				warnings.append(warnings.VALIDATORS.notUnique % )

class MIXED_ID:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class PLAIN_TEXT:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class MIXED_TEXT:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class SECTION_CODE:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class GRADE_ITEM_CATEGORY:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class GRADE_ITEM_NAME:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class GRADE_VALUE:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():

class DATE:
	warnings = list()
	errors = list()

	def __init__(self, column)
		self.column = column

	def run():