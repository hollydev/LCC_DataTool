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
		self.column = column
		self.values = column.values

		self.messages = list()
		self.errors = list()
		self.items = 0


	def run(self, threshold, master_n=1500):
		
		master = self.get_master_list(self.column, master_n)
		matches = self.get_choice_matches(self.values, master.keys(), threshold)
		
		matchedList = list()
		for val in self.values:
			match = matches[val]

			if(match != None):
				matchedList.append(match[0])
			else:
				matchedList.append(val)

			self.messages.append(CLEANERS.matchResult.format(val, match[0], match[1]))
			
		#Return matches past a threshold
		# for i, val in enumerate(self.values):
		# 	match, confidence = matches[val]

		# 	if(confidence >= threshold):
		# 		self.values[i] = match
		# 		self.items += 1 #Count items cleaned
		# 	else:
		# 		continue


		return matchedList


	def get_choice_matches(self, column, master, threshold=95):
		#Get a unique list of existing names
		choices = set()
		for word in self.column: choices.add(word)
		
		#Generate a master list (top n) to match choices to
		master = set(master)
		
		matches = dict()
		
		progBar = tqdm(total = len(choices))
		
		for value in choices:
			progBar.update(1)
			progBar.display()
			"""
			#Remove the current matched value if 
			try:
				fixedMaster = set(master)
				fixedMaster.remove(value) #Remove the current value from the search list
			except KeyError:
				continue
			"""
			
			chosen = process.extractOne(value, master, scorer=fuzz.token_sort_ratio, score_cutoff = 80)
			
			if(chosen == None):
				matches.update({value:("None", "X")})
			else:
				matches.update({value:chosen})

			
		progBar.close()
		return matches
	
	def get_master_list(self, column, n):
		#Get the count of values over the entire list.
		master = dict()
		
		iterator = 0
		
		for key, val in tqdm(self.column.value_counts().items()):
			master.update({key : val})
			iterator += 1
			
			if(iterator == n):
				break
				
		return master

	
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