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
                
        #Save data to their respective objects
        self.column = column
        self.values = column.values

        self.messages = list()
        self.errors = list()
        self.items = len(column)


    def run(self, threshold=80, n_match=None):
        #Set default parameter at 10% of data
        pct_10 = int(len(self.column)*0.10)
        if(pct_10 == 0):
            pct_10 = 1
        
        #Set number match list on none specified
        if(n_match == None):
            n_match = pct_10
        
        master = self.get_master_list(self.column, n_match)
        matches = self.get_choice_matches(self.values, master.keys(), threshold)
        
        matchedList = list()
        for val in self.values:
            match = matches[val]

            if(match != None):
                matchedList.append(match[0])
            else:
                matchedList.append(val)

            self.messages.append(CLEANERS.matchResult.format(val, match[0], match[1]))
                    
        return matchedList


    def get_choice_matches(self, column, master, threshold=80):
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
            
            chosen = process.extractOne(value, master, scorer=fuzz.token_sort_ratio, score_cutoff = threshold)
            
            if(chosen == None):
                matches.update({value:("None", "X")})
            else:
                matches.update({value:chosen})

            
        progBar.close()
        return matches
    
    def get_master_list(self, column, n_match):
        #Get the count of values over the entire list.
        master = dict()
        
        #Normalize to reduce duplication chance
        column = column.str.lower()
        column = column.str.strip()
        
        #Normalize to string before saving to object
        column = column.apply(str)
        
        iterator = 0
        
        for key, val in tqdm(column.value_counts().items()):
            master.update({key : val})
            iterator += 1
            
            if(iterator == n_match):
                break
                
        return master

    
    def statistics(self):
        return SYSTEM.cleanerStats.format("Fuzzy Matching", self.items, len(self.messages), len(self.errors))

    def get_warnings(self):
        return(self.messages)

    def get_errors(self):
        return(self.errors)



class DATE:
    messages = list()
    errors = list()
    

    def __init__(self, column):
        self.items = len(columns)
        self.column = column

    def run(self,gradeItemName):
        self.read_gradeItemName(gradeItemName)
         
#removes date from GradeItemName and returns (date, GradeItemName)
# param - gradeItemName (from 'gradeItemName' column in dataframe)
# return - (date, GradeItemName) 
#       returned GradeItemName does NOT have date in it
    def read_gradeItemName(self,gradeItemName):
        gradeItemName = gradeItemName.strip()
    
        spot = len(gradeItemName)-8
        date = 'N/A'
        end = gradeItemName[spot:]
    
        if end.isdigit() and len(end) > 4:
            date = end
            gradeItemName = gradeItemName[:spot]
        else:
            spot = len(gradeItemName)-6
            end = gradeItemName[spot:]
        
            if end.isdigit() and len(end) > 4:
                date = end
                gradeItemName = gradeItemName[:spot]
            
        gradeItemName = gradeItemName.strip()
        return date, gradeItemName

    def create_date_column(self,dataFrame, list_of_dates):
        dataFrame['Date'] = list_of_dates
        return dataFrame
    

#remove date from grade item name and appends it in a new column titled 'Date'
#   param - pandas dataframe
#   return - pandas dataframe (with Date column)
    def clean_gradeItemName(self,data):
        list_of_dates = []
        for index, row in data.iterrows():
            grade_name = row['GradeItemName']
            date = self.read_gradeItemName(grade_name)[0]
            list_of_dates.append(date)
        
            data.replace(to_replace = grade_name, value = self.read_gradeItemName(grade_name)[1])
    
        data = self.create_date_column(data, list_of_dates)
            
    
        return data
   
class BOOLEAN_CLEANER:
    messages = list()
    errors = list()
    
    def __init(self, column):
        self.items = len(columns)
        self.column = column
       
    def run(self):        
        return self.column.notna()
    
    def statistics(self):
        return SYSTEM.cleanerStats.format("Boolean Cleaner", self.items, len(self.messages), len(self.errors))

    def get_warnings(self):
        return(self.messages)

    def get_errors(self):
        return(self.errors)
    