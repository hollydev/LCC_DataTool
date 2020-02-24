import pandas as pd

import numpy as np
from tqdm import tqdm

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def get_master_list(pdColumn, n):
	#Get the count of values over the entire list.
	master = dict()
	
	iterator = 0
	
	for key, val in tqdm(pdColumn.value_counts().items()):
		master.update({key : val})
		iterator += 1
		
		if(iterator == n):
			break
			
	return master


def get_choice_matches(pdColumn, master):
	#Get a unique list of existing names
	choices = set()
	for word in pdColumn: choices.add(word)
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
		
"""Read in a pandas column and perform fuzzy matching."""
def clean(pdColumn, n):
	
	#Simple process command
	values = pdColumn.values
	
	master = get_master_list(pdColumn, n)
	matches = get_choice_matches(values, master.keys())
	print(len(matches), len(values))
	
	for val in values:
		match = matches[val]
		print("Matched '{}' to [{}];\tConfidence {}".format(val, match[0], match[1]))
	
