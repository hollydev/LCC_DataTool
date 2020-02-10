"""
	Filename: BCselector.py
	Programmer: Sean Thompson
	Date Created: 01/02/2020
	Last Update: created file
	Description: This file contains functions for retrieving the base columns of a
     dataframe that is created from a csv file"""

import pandas as pd 
import glob as gb 
from source.validators import MIXED_TEXT, PLAIN_TEXT, DATE, NUMERIC_ID
#from cleaners import GRADE_ITEM_NAME

#setting for the displayed output (For testing)
# pd.set_option('display.max_columns', 5)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)


#this method accepts a string that is then used to compare against the enum values
def get_base_column(dataframe, theColumn):

    
    # #using glob to find all files in the subdirectory 'GBinfo' that have the .csv extension
    # for file in gb.glob("source/GBinfo/*.csv"):

    #     #grab the base columns from the csv file
    #     df = pd.read_csv(file, usecols = list(range(0,18)), sep = ',')

    #     #send the dataframe to split_and_reorganize so it can be modified
    #     df = split_and_reorganize(df)

    #Re-order and split the data.
    orderedData = split_and_reorganize(dataframe)
    
    #convert column headers to lowercases
    orderedData.columns = map(str.lower, orderedData.columns)


    #Get only the base columns from the data frame
    df = orderedData.loc[ : , "username":"gradelastmodified"]
    
   
    for theColumn in df:
        columnSeries = df[theColumn]
    #Determine the name of the column and call appropriate validators
        if(theColumn.lower() == "username"):
            validateMixed(columnSeries.values)
        elif(theColumn.lower() == "firstname"):
            validatePlain(columnSeries.values)
        elif(theColumn.lower() == "lastname"):
            validatePlain(columnSeries.values)
        elif(theColumn.lower() == "roleid"):
            validateNum(columnSeries.values, 3)
        elif(theColumn.lower() == "rolename"):
            validatePlain(columnSeries.values)
        elif(theColumn.lower() == "courseofferingid"):
            validateNum(columnSeries.values, 6)
        elif(theColumn.lower() == "courseofferingcode"):
            validateMixed(columnSeries.values)
        elif(theColumn.lower() == "courseofferingname"):
            validateMixed(columnSeries.values)
        elif(theColumn.lower() == "name"):
            validateMixed(columnSeries.values)
        elif(theColumn.lower() == "number"):
            validateNum(columnSeries, 5)
        elif(theColumn.lower() == "term"):
            validateNum(columnSeries, 6)
        elif(theColumn.lower() == "gradeitemcategoryid"):
            validateNum(columnSeries, 7)
        elif(theColumn.lower() == "gradeitemcategoryname"):
            validateMixed(columnSeries.values)
        elif(theColumn.lower() == "gradeitemid"):
            validateNum(columnSeries.values, 7)
        elif(theColumn.lower() == "gradeitemname"):
            print("no validator for %s", theColumn)
        elif(theColumn.lower() == "gradeitemweight"):
            print("no validator for %s", theColumn)
        elif(theColumn.lower() == "pointsnumerator"):
            print("no validator for %s", theColumn)
        elif(theColumn.lower() == "pointsdenominator"):
            print("no validator for %s", theColumn)
        elif(theColumn.lower() == "gradevalue"):
            print("no validator for %s", theColumn)
        elif(theColumn.lower() == "gradelastmodified"):
            validateDate(columnSeries.values)


    
    


#splits CourseOfferingCode into three columns and replaces it with the new columns
def split_and_reorganize(theDataFrame):

    #df1 takes all the columns up to CourseOfferingCode
    df1 = pd.DataFrame(theDataFrame.iloc[:, :9])

    #CourseOfferingCode is split, new columns are appended and CourseOfferingCode is dropped
    df1[['name', 'number', 'term']] = theDataFrame.CourseSectionCode.str.split("-", expand = True)
    df1 = df1.drop(['CourseSectionCode'], axis = 1)

    #df2 takes all the columns after CourseOfferingCode
    df2 = pd.DataFrame(theDataFrame.iloc[:, 9:])

    #df1 and df2 are concatenated and returned
    frames = [df1, df2]
    theDataFrame = pd.concat(frames, sort = False, axis = 1)
    return theDataFrame

def validateMixed(df):
    validateMixedID = MIXED_TEXT(df)
    validateMixedID.run()
    info = validateMixedID.statistics()
    warnings = validateMixedID.get_warnings()
    errors = validateMixedID.get_errors()

    print(info)
   

def validatePlain(df):
    validatePlainText = PLAIN_TEXT(df)
    validatePlainText.run()
    info = validatePlainText.statistics()
    warnings = validatePlainText.get_warnings()
    errors = validatePlainText.get_errors()

    print(info)


def validateNum(df, length):
    validateNumeric = NUMERIC_ID(df)
    validateNumeric.run(length)
    info = validateNumeric.statistics()
    warnings = validateNumeric.get_warnings()
    errors = validateNumeric.get_errors()

    print(info)


def validateDate(df):
    validateDate = DATE(df)
    validateDate.run()
    info = validateDate.statistics()
    warnings = validateDate.get_warnings()
    errors = validateDate.get_errors()

    print(info)




