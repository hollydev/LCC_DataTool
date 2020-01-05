"""
	Filename: warnings.py
	Programmer: Holly Locke
	Date Created: 01/03/2020
	Last Update: File Created

	Description: This file contains warning messages to be used throughout the program. Using
	this file will provide a central place to modify, add, or remove error messages. Additionally
	classes are created to display warning messages.
"""



################
## Validators ##
################
class VALIDATORS:
	def __init__(self):
		#Numeric ID
		self.success = "Validator [%s] ran successfully."
		self.failure = "Validator [%s] failed to pass."
		self.notNumeric = "%s contains a non-numeric character."
		self.notUniqueDup = "%i ID is not unique. Duplicate entry found at %i"
		self.notUniqueMult = "Multiple IDs found. Duplicate entries found at %s"
		self.length = "%i is of length %i, expected length %i"


		#Mixed ID
		self.expectMixedNum = "%s contains only numeric values, expected mixed values"
		self.expectMixedChar = "%s contains only character values, expected mixed values"



################
##  Cleaners  ##
################
class CLEANERS:

	def __init__(self):
		#Cleaners - Numeric ID
		self.changedNumeric = "Removed non-numeric character in %s. Changed to %i"


################
##   System   ##
################
class SYSTEM:
	def __init__(self):
		#System Warning Messages

		#System Statistics Messages
		self.validatorStats = "Validator [%s]: Items Validated [%i]\t Warnings: [%i]\t Errors: [%i]"
		 