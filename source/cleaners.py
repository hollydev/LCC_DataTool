"""
	Filename: cleaners.py
	Programmer: Holly Locke
	Date Created: 01/02/2020
	Last Update: File Created

	Description: This file contains all cleaning logic that may be applied to the columns. 
	Built to work with the rest of the data tool, cleaners are created as classes.

"""
import pandas as pd
import numpy as np

from tqdm import tqdm
from fuzzywuzzy import fuzz, process

from messages.cleaners import CLEANERS
from messages.system import SYSTEM, LOG

class FUZZY_MATCHING:
	def __init__(self, column):
		self.values = column

		self.messages = list()
		self.errors = list()
		self.items = 0


	def run(self, threshold):

		#Get a unique list of existing names
		choices = set()
		for word in self.values: choices.add(word)
		
		#Simple process command
		values = self.values
		
		matches = self.get_choice_matches(choices)
		
		for val in values:
			match = matches[val]
			self.messages.append(CLEANERS.matchResult.format(val, match[0], match[1]))
		
		#Return matches past a threshold
		for i, val in enumerate(self.values):
			match, confidence = matches[val]

			if(confidence >= threshold):
				self.values[i] = match
				self.items += 1 #Count items cleaned
			else:
				continue

		return self.values

	def get_choice_matches(self, choices):
		matches = dict()
	
		progBar = tqdm(total = len(choices))
		
		for value in choices:
			otherChoices = set(choices)
			otherChoices.remove(value)
			progBar.update(1)
			progBar.display()
			
			chosen = process.extractOne(value, otherChoices, scorer=fuzz.token_sort_ratio)
			
			matches.update({value:chosen})
			 
		progBar.close()
		return matches

	def statistics(self):
		return SYSTEM.cleanerStats.format("Fuzzy Matching", self.items, len(self.messages), len(self.errors))

	def get_warnings(self):
		return(self.messages)

	def get_errors(self):
		return(self.errors)


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