"""
	Filename: system.py
	Programmer: Holly Locke
	Date Created: 01/03/2020
	Last Update: File Created

	Description: This file contains messages to be used by cleaning functions.
"""

################
##  Cleaners  ##
################
class CLEANERS:

	def __init__(self):
		pass
		
	#Cleaners - Numeric ID
	changedNumeric = "Removed non-numeric character in %s. Changed to %i"

	#Fuzzy Matching
	matchResult = "Matched '{}' to [{}];\tConfidence {}"