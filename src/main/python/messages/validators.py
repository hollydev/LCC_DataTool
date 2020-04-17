"""
	Filename: validators.py
	Programmer: Holly Locke
	Date Created: 01/03/2020
	Last Update: File Created

	Description: This file contains messages to be used by validation functions.
"""

################
## Validators ##
################
class VALIDATORS:
	def __init__(self):
		#Numeric ID
		self.success = "Validator [%s] ran successfully."
		self.failure = "Validator [%s] failed to pass."
		self.notNumeric = "%s contains a non-numeric character. (%s)"
		self.notUniqueDup = "%i ID is not unique. Duplicate entry found at %i"
		self.notUniqueMult = "Multiple IDs found. Duplicate entries found at %s"
		self.length = "%s is of length %i, expected length %i. (%s)"


		#Mixed ID
		self.expectMixedNum = "%s contains only numeric values, expected mixed values. (%s)"
		self.expectMixedChar = "%s contains only character values, expected mixed values. (%s)"
		self.expectedNonEmpty = "%s contains no values. (%s)"


		#PlainText
		self.expectedTextOnly = "%s contains a digit. (%s)"
		self.expectedNoSymbols = "%s contains a symbol. (%s)"

		#Date
		self.unexpectedFormat = "%s is not in the correct format. (%s)"

		#CRN
		self.wrongCRN = "%s is not the correct CRN/term for section %s, at %i"
