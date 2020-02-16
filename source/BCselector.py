"""
	Filename: BCselector.py
	Programmer: Sean Thompson
	Date Created: 01/02/2020
	Last Update: created file
	Description: This file contains functions for retrieving the base columns of a
     dataframe and validating their contents"""

import pandas as pd 
import glob as gb 
from source.validators import MIXED_TEXT, PLAIN_TEXT, DATE, NUMERIC_ID
from source.cleaners import FUZZY_MATCHING
#from cleaners import GRADE_ITEM_NAME

#setting for the displayed output (For testing)
# pd.set_option('display.max_columns', 5)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)



def get_base_column(dataframe, column):

    
    #convert column headers to lowercases
    dataframe.columns = map(str.lower, dataframe.columns)

    #Re-order and split the data.
    orderedData = split_and_reorganize(dataframe)

    #grab user specified column
    if(column == "all"):
        df = orderedData.iloc[ : , :20]
    else:
        df = orderedData[[column.lower()]]
    
  
    #Determine the name of the column and call appropriate validators
    for oneColumn in df:
        columnSeries = df[oneColumn]
        if(oneColumn.lower() == "username"):
            print("username: ")
            validateMixed(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "firstname"):
            print("firtname: ")
            validatePlain(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "lastname"):
            print("lastname: ")
            validatePlain(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "roleid"):
            print("roleid: ")
            validateNum(columnSeries.values, 3)
            print("\n")
        elif(oneColumn.lower() == "rolename"):
            print("rolename: ")
            validatePlain(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "courseofferingid"):
            print("courseofferingid: ")
            validateNum(columnSeries.values, 6)
            print("\n")
        elif(oneColumn.lower() == "courseofferingcode"):
            print("courseofferingcode: ")
            validateMixed(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "courseofferingname"):
            print("courseofferingname: ")
            validateMixed(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "name"):
            print("name: ")
            validateMixed(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "number"):
            print("number: ")
            validateNum(columnSeries, 5)
            print("\n")
        elif(oneColumn.lower() == "term"):
            print("term: ")
            validateNum(columnSeries, 6)
            print("\n")
        elif(oneColumn.lower() == "gradeitemcategoryid"):
            print("gradeitemcategoryid: ")
            validateNum(columnSeries, 7)
            print("\n")
        elif(oneColumn.lower() == "gradeitemcategoryname"):
            print("gradeitemcategoryname: ")
            validateMixed(columnSeries.values)
            print("\n")
        elif(oneColumn.lower() == "gradeitemid"):
            print("gradeitemid: ")
            validateNum(columnSeries.values, 7)
        elif(theColumn.lower() == "gradeitemname"):
            validateMixed(columnSeries.values)

            cleaned = cleanFuzzyMatching(columnSeries.values)

            newName = columnSeries.name + "_cleaned"
            df[newName] = cleaned #Save the new column with a suffix
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
    
    return df #Return the processed data frame.


#splits CourseOfferingCode into three columns and replaces it with the new columns
def split_and_reorganize(theDataFrame):

    #df1 takes all the columns up to CourseSectionCode
    index = theDataFrame.columns.get_loc('coursesectioncode')
    df1 = pd.DataFrame(theDataFrame.iloc[:, :index+1])

    #CourseOfferingCode is split, new columns are appended and CourseSectionCode is dropped
    df1[['name', 'number', 'term']] = theDataFrame.coursesectioncode.str.split("-", expand = True)
    df1 = df1.drop(['coursesectioncode'], axis = 1)

    #df2 takes all the columns after CourseSectionCode
    df2 = pd.DataFrame(theDataFrame.iloc[:, index+1:])

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


def cleanFuzzyMatching(df):
    cleanFuzzyMatching = FUZZY_MATCHING(df)
    cleanedColumn = cleanFuzzyMatching.run(threshold=2)
    print(cleanedColumn)

    info = cleanFuzzyMatching.statistics()
    warnings = cleanFuzzyMatching.get_warnings()
    errors = cleanFuzzyMatching.get_errors()

    print(info)
    
    return cleanedColumn