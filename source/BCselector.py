"""
	Filename: BCselector.py
	Programmer: Sean Thompson
	Date Created: 01/02/2020
	Last Update: created file
	Description: This file contains functions for retrieving the base columns of a
     dataframe that is created from a csv file"""

import pandas as pd 
import glob as gb 
from source import validators
#from cleaners import GRADE_ITEM_NAME

#setting for the displayed output (For testing)
pd.set_option('display.max_columns', 8)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


#this method accepts a string that is then used to compare against the enum values
def get_base_column(theColumn):


    #using glob to find all files in the subdirectory 'GBinfo' that have the .csv extension
    for file in gb.glob("source/GBinfo/*.csv"):

        #grab the base columns from the csv file
        df = pd.read_csv(file, usecols = list(range(0,18)), sep = ',')

        #send the dataframe to split_and_reorganize so it can be modified
        df = split_and_reorganize(df)
        #convert column headers to lowercase
        df.columns = [x.lower() for x in df.columns]
        
        #Target column
        df = df.loc[:,theColumn.lower()]


        #Determine the name of the column and call appropriate validators
        if(theColumn.lower() == "username"):
            validateMixed(df)
           
            

        elif(theColumn.lower() == "firstname"):
            validatePlain(df)
            

        elif(theColumn.lower() == "lastname"):
            validatePlain(df)
            
        elif(theColumn.lower() == "roleid"):
            validateNum(df, 3)

        elif(theColumn.lower() == "rolename"):
            validatePlain(df)

        elif(theColumn.lower() == "courseofferingid"):
            validateNum(df, 6)
            
        elif(theColumn.lower() == "name"):
            validateMixed(df)

        elif(theColumn.lower() == 'number'):
            validateNum(df, 5)

        elif(theColumn.lower() == 'term'):
            validateNum(df, 6)

        elif(theColumn.lower() == "courseofferingname"):
            validateMixed(df)

        elif(theColumn.lower() == "coursesectioncode"):
            validateMixed(df)
        
        elif(theColumn.lower() == "gradeitemcategoryid"):
            validateNum(df, 7)

        elif(theColumn.lower() == "gradeitemcategoryname"):
            validateMixed(df)
            
        elif(theColumn.lower() == "gradeitemid"):
            validateNum(df, 7)
        
        elif(theColumn.lower() == "gradeitemname"):
            validateMixed(df)
            
        elif(theColumn.lower() == "gradeitemweight"):
            print(df)

        elif(theColumn.lower() == "pointsnumerator"):
            print(df)
        
        elif(theColumn.lower() == "pointsdenominator"):
            validateNumeric = validators.NUMERIC_ID(df)
            validateNumeric.run(7)
            info = validateNumeric.statistics()
            warnings = validateNumeric.get_warnings()
            errors = validateNumeric.get_errors()

            print(info)
            print(warnings)
            print(errors)
        
        elif(theColumn.lower() == "gradevalue"):
            print(df)
        
        elif(theColumn.lower() == "gradelastmodified"):
            validateDate(df)
                
        return df


#splits CourseOfferingCode into three columns and replaces it with the new columns
def split_and_reorganize(theDataFrame):

    #df1 takes all the columns up to CourseOfferingCode
    df1 = pd.DataFrame(theDataFrame.iloc[:, :7])

    #CourseOfferingCode is split, new columns are appended and CourseOfferingCode is dropped
    df1[['name', 'number', 'term']] = theDataFrame.CourseOfferingCode.str.split("-", expand = True)
    df1 = df1.drop(['CourseOfferingCode'], axis = 1)

    #df2 takes all the columns after CourseOfferingCode
    df2 = pd.DataFrame(theDataFrame.iloc[:, 7:])

    #df1 and df2 are concatenated and returned
    frames = [df1, df2]
    theDataFrame = pd.concat(frames, sort = False, axis = 1)
    return theDataFrame

def validateMixed(df):
    validateMixedID = validators.MIXED_TEXT(df)
    validateMixedID.run()
    info = validateMixedID.statistics()
    warnings = validateMixedID.get_warnings()
    errors = validateMixedID.get_errors()

    print(info)
    print("warnings: ", warnings)
    print("errors ", errors)

def validatePlain(df):
    validatePlainText = validators.PLAIN_TEXT(df)
    validatePlainText.run()
    info = validatePlainText.statistics()
    warnings = validatePlainText.get_warnings()
    errors = validatePlainText.get_errors()

    print(info)
    print("warnings: ", warnings)
    print("errors: ", errors)

def validateNum(df, length):
    validateNumeric = validators.NUMERIC_ID(df)
    validateNumeric.run(length)
    info = validateNumeric.statistics()
    warnings = validateNumeric.get_warnings()
    errors = validateNumeric.get_errors()

    print(info)
    print("warnings: ", warnings)
    print("errors: ", errors)

def validateDate(df):
    validateDate = validators.DATE(df)
    validateDate.run()
    info = validateDate.statistics()
    warnings = validateDate.get_warnings()
    errors = validateDate.get_errors()

    print(info)
    print(warnings)
    print(errors)



if __name__ == '__main__':


   get_base_column("firstname")

