import pandas as pd

import numpy as np
from pprint import pprint
from tqdm import tqdm

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def get_choice_matches(choices):
	
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
		
"""Read in a pandas column and perform fuzzy matching."""
def clean(pdColumn):
	#Get a unique list of existing names
	choices = set()
	for word in pdColumn: choices.add(word)
	
	#Simple process command
	values = pdColumn.values
	print(values)
	matches = get_choice_matches(choices)
	
	for val in values:
		match = matches[val]
		print("Matched '{}' to [{}];\tConfidence {}".format(val, match[0], match[1]))
	
