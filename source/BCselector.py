"""
	Filename: BCselector.py
	Programmer: Sean Thompson
	Date Created: 01/02/2020
	Last Update: created file
	Description: This file contains functions for retrieving the base columns of a
     dataframe that is created from a csv file"""

import pandas as pd 
import glob as gb 
from enum import Enum 
from cleaners import GRADE_ITEM_NAME

class BASE_COLUMN(Enum):
    username = 1
    firstname = 2
    lastname = 3
    roleid = 4
    rolename = 5
    courseofferinid = 6
    courseofferincode = 7
    courseofferingcode = 8
    courseofferingname = 9
    coursesectioncode = 10
    gradeitemcategoryid = 11
    gradeitemcategoryname = 12
    gradeitemid = 13
    gradeitemname = 14
    gradeitemweight = 15
    pointsnumerator = 16
    pointsdenominator = 17
    gradevalue = 18
    gradelastmodified = 19

#setting for the displayed output (For testing)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#this method accepts a string that is then used to compare against the enum values
def get_base_column(theColumn):
    #using glob to find all files in the subdirectory 'GBinfo' that have the .csv extension
    for file in gb.glob("./GBinfo/*.csv"):
       
        for column in BASE_COLUMN:
            if(theColumn == column.name):
                x = column.value - 1
        
                                             #targeted column
        df = pd.read_csv(file, usecols = list(range(x, x+1)), sep = ',')
        df = GRADE_ITEM_NAME(df)


        #print(df) -for testing
        return df
        




