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
import validators
#from cleaners import GRADE_ITEM_NAME

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
    gradeItemCategoryID = 10
    gradeItemCategoryName = 11
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
#pd.set_option('display.max_colwidth', -1)

#this method accepts a string that is then used to compare against the enum values
def get_base_column(theColumn):
    #using glob to find all files in the subdirectory 'GBinfo' that have the .csv extension
    
    for file in gb.glob("./GBinfo/*.csv"):

        #call method for rearranging the columns..?
        df = pd.read_csv(file, usecols = list(range(0,18)), sep = ',')

        tempdf = df[['name', 'number', 'term']] = df.CourseOfferingCode.str.split("-", expand = True)

        pd.concat([df, tempdf], axis=1)

        df.to_csv('./testing.csv')

        print(df)


        
        for column in BASE_COLUMN:
            if(theColumn == column.name):
                x = column.value - 1  
                
                                              #Target column
        df = pd.read_csv(file, usecols = list(range(x, x+1)), sep = ',')
        
        if(theColumn == "userName"):
            print(df)

        elif(theColumn == "firstName"):
            print(df)

        elif(theColumn == "lastName"):
            print(df)

        elif(theColumn == "roleID"):
            print(df)

        elif(theColumn == "courseOfferingID"):
            print(df)

        elif(theColumn == "courseOfferingCode"):
            print(df)

        elif(theColumn == "courseOfferingName"):
            print(df)

        elif(theColumn == "courseSectionCode"):
            print(df)
        
        elif(theColumn == "gradeItemCategoryID"):
            print(df)

        elif(theColumn == "gradeItemCategoryName"):
            validateMixedID = validators.MIXED_ID(df)
            validateMixedID.run()
            info = validateMixedID.statistics()
            print(info)
            #print(df)

        elif(theColumn == "gradeItemID"):
            validateNumeric = validators.NUMERIC_ID(df)
            validateNumeric.run(7)
            info = validateNumeric.statistics()
            print(info)
        
        elif(theColumn == "gradeItemName"):
            print(df)
        
        elif(theColumn == "gradeItemWeight"):
            print(df)

        elif(theColumn == "pointsNumerator"):
            print(df)
        
        elif(theColumn == "pointsDenominator"):
            print(df)
        
        elif(theColumn == "gradeValue"):
            print(df)
        
        elif(theColumn == "gradeLastModified"):
            print(df)
                
    return df
        

if __name__ == '__main__':
    get_base_column("gradeItemCategoryName")
    get_base_column("gradeItemID")