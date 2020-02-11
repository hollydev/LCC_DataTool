import pandas as pd

import numpy as np
from pprint import pprint

import editdistance

threshold = 3

def summary(data):
	#Get lexicon
	uniqueWords = set()
	for word in data: uniqueWords.add(word)
	
	print("Unique Entries: [%i]" % (data.nunique()))
	print("Most Repeated Entries:")
	print(data.value_counts())
	
	
	
"""Parser will read from a PD column, manage sending the right data type"""
def read_column():
	data = pd.read_csv("testfile.txt")
	
	return(data["Grade Item Name"])
	
"""Read in a pandas column and perform fuzzy matching."""
def clean(pdColumn):
	#Get lexicon
	uniqueWords = set()
	for word in pdColumn: uniqueWords.add(word)
	
	#Nearest Distance
	minimumEdit = 20
	viableEdits = list()
	editList = dict()
	
	#Iterate over the lexicon, finding words that fit within the edit distance threshold
	for item in pdColumn:
		for word in uniqueWords:
			if(abs(len(item) - len(word)) > threshold):
				continue
			
			distance = editdistance.eval(item, word)
			if word != item and distance < threshold:
				viableEdits.append(word)
				
				#print("Matching [%s] to [%s]: Edit distance %s" % (item, word, distance))
			
			editList[item] = viableEdits
			viableEdits = list()
	pprint(editList)
	
	#Print summary of uncleaned data
	summary(pdColumn)
	

if __name__ == "__main__":
	#data = read_column()
	pass
	#clean(data)
