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
    userName = 1
    firstName = 2
    lastName = 3
    roleID = 4
    roleName = 5
    courseOfferingID = 6
    courseOfferingCode = 7
    courseOfferingName = 8
    CourseSectionCode = 9
    gradeItemCateoryID = 10
    gradeItemCateoryName = 11
    gradeItemID = 12
    gradeItemName = 13
    gradeItemWeight = 14
    pointsNumerator = 15
    pointsdenominator = 16
    gradeValue = 17
    gradeLastModified = 18
    

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
        grade_item_cleaned = GRADE_ITEM_NAME(df)
        grade_item_cleaned.run(2)

        #print(df) -for testing
        return df
        

get_base_column("firstname")


