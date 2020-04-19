"""
	Filename: BCselector.py
	Programmer: Sean Thompson
	Date Created: 01/02/2020
	Last Update: created file
	Description: This file contains functions for retrieving the base columns of a
     dataframe and validating their contents"""

import pandas as pd 
import glob as gb 
from lcc_assessment.validators import MIXED_TEXT, PLAIN_TEXT, DATE, NUMERIC_ID, CRN
from lcc_assessment.cleaners import FUZZY_MATCHING, BOOLEAN_CLEANER
from lcc_assessment.main import Worker, WorkerSignals
# from src.main.python.lcc_assessment.validators import MIXED_TEXT, PLAIN_TEXT, DATE, NUMERIC_ID, CRN
# from src.main.python.lcc_assessment.cleaners import FUZZY_MATCHING, BOOLEAN_CLEANER
from collections import namedtuple
#from cleaners import GRADE_ITEM_NAME


def get_base_column(dataframe, selectedColumns, signal):

    for column in selectedColumns:
        pass
        # if column == "CourseSectionCode":
            # selectedColumns.remove('CourseSectionCode')
            # selectedColumns.append('section')
            # selectedColumns.append('crn')
            # selectedColumns.append('term')
            
    #convert column headers in dataframe and selectedColumns to lowercase 
    dataframe.columns = map(str.lower, dataframe.columns)
    count = 0
    #Re-order and split the data.
    orderedData = split_and_reorganize(dataframe)
    signal.progress2.emit(10)
    #preserve the sections and termcodes from the dataframe for use in validating CRNs
    allSections = orderedData[["section", "crn","term"]]
    signal.progress2.emit(25)


    #check if the user wants to validate multiple columns
    if isinstance(selectedColumns, list): 
        vInfo = []
        for x in selectedColumns:
            selectedColumns[count] = x.lower()
            count += 1
        if(count == 18):
            df = orderedData.iloc[ : , :20]
        else:
            df = orderedData.reindex(columns = selectedColumns)
        percentage = 65//(count)
        remainder = 65%(count)
        for oneColumn in df:
            columnSeries = df[oneColumn]
            callValidators(oneColumn, columnSeries, df, allSections, vInfo, percentage, signal)

    else: #user only wants to validate one column
        selectedColumns = selectedColumns.lower()
        df = orderedData.loc[ :,selectedColumns]
        callValidators(selectedColumns, df, df, allSections, vInfo, percentage, signal) #df is also passed in for columnseries since only one column was selected(a series)
    
    signal.progress2.emit(remainder)
    signal.dataframe.emit(df)
    return (vInfo) #Return the processed data frame.
    
def callValidators(oneColumn, columnSeries, df, allSections, vInfo, percentage, signal):
    
    if(oneColumn.lower() == "username"):
        print("--username--")
        vInfo.append(validateMixed(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "firstname"):
        print("--firtname--")
        vInfo.append(validatePlain(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "lastname"):
        print("--lastname--")
        vInfo.append(validatePlain(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "roleid"):
        print("--roleid--")
        vInfo.append(validateNum(columnSeries, 3,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "rolename"):
        print("--rolename--")
        vInfo.append(validatePlain(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "courseofferingid"):
        print("--courseofferingid--")
        vInfo.append(validateNum(columnSeries, 6,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "courseofferingcode"):
        print("--courseofferingcode--")
        vInfo.append(validateMixed(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "courseofferingname"):
        print("--courseofferingname--")
        vInfo.append(validateMixed(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "section"):
        print("--section--")
        vInfo.append(validateMixed(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "crn"):
        print("--CRN--")
        vInfo.append(validateCRN(columnSeries,allSections,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "term"):
        print("--term--")
        vInfo.append(validateNum(columnSeries, 6,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "gradeitemcategoryid"):
        print("--gradeitemcategoryid--")
        vInfo.append(validateNum(columnSeries, 7,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "gradeitemcategoryname"):
        print("--gradeitemcategoryname--")
        vInfo.append(validateMixed(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
        # cleaned = cleanFuzzyMatching(columnSeries, n_match=50)
        # newName = columnSeries.name + "_cleaned"
        # df[newName] = cleaned #Save the new column with a suffix
    elif(oneColumn.lower() == "gradeitemid"):
        print("--gradeitemid--")
        vInfo.append(validateNum(columnSeries, 7,df))
        signal.progress2.emit(percentage)
        print("\n")
    elif(oneColumn.lower() == "gradeitemname"):
        print("--gradeitemname--")
        vInfo.append(validateMixed(columnSeries,df))
        signal.progress2.emit(percentage)
        print("\n")
        # cleaned = cleanFuzzyMatching(columnSeries, n_match=200)
        # newName = columnSeries.name + "_cleaned"
        # df[newName] = cleaned #Save the new column with a suffix
    elif(oneColumn.lower() == "gradeitemweight"):
        print("no validator for %s", oneColumn)
        signal.progress2.emit(percentage)
    elif(oneColumn.lower() == "pointsnumerator"):
        print("no validator for %s", oneColumn)
        signal.progress2.emit(percentage)
    elif(oneColumn.lower() == "pointsdenominator"):
        print("no validator for %s", oneColumn)
        signal.progress2.emit(percentage)
    elif(oneColumn.lower() == "gradevalue"):
        print("no validator for %s", oneColumn)
        signal.progress2.emit(percentage)
    elif(oneColumn.lower() == "gradelastmodified"):
        print("--gradelastmodified--")
        signal.progress2.emit(percentage)
        vInfo.append(validateDate(columnSeries,df))
        print("\n")
    elif(oneColumn.lower() == "gradercomment"):
        print("no validator for %s", oneColumn)
        signal.progress2.emit(percentage)
        df[oneColumn] = booleanCleaner(columnSeries) #Replace the column with the cleaned version.
        print("\n")
    else:
        #Fill the vInfo variable for columns that don't have validators.
        fakeInfo = ">Column [{}]>Validated with [{}]>Items Validated: [0] Warnings: [0] Errors: [0]".format(oneColumn.lower(), "Skipped")
        stat = namedtuple('name', 'err warn')
        fakeStats = stat(err = [], warn = [])        
        vInfo.append((fakeInfo, fakeStats))
        
    return(vInfo)

def call_cleaner(columntoclean, signal):
    """ This function defines which cleanings are to be run on which columns.
        
        @Params:
            columntoclean - A string indicating the column requested for cleaning.
            
        @Returns:
            cleanedColumn - A cleaned version of the given column with the same indexes.
            @None - When a column without a cleaner is requested, return None
    """
    if(columntoclean.columns[0] == 'gradeitemcategoryname'):
        cleanedColumn = fuzzyMatchingCleaner(columntoclean['gradeitemcategoryname'], signal, n_match=200)
        return cleanedColumn
    elif(columntoclean.columns[0] == 'gradeitemname'):
        cleanedColumn = fuzzyMatchingCleaner(columntoclean['gradeitemname'], signal,n_match=200)
        return cleanedColumn
    else:
        return None

def cleaners_list():
    """ This function returns a list of cleaners set to the column name. Used to 
        provide context to the GUI when navigating columns.
        
        @Returns
            cleanersList - A named dictionary of cleaners being applied.
    """
    
    cleanersList = {"gradeitemcategoryname": ["Fuzzy Matching"],\
                    "gradeitemname": ["Fuzzy Matching"]
                   }
                   
    return cleanersList
    

#splits CourseOfferingCode into three columns and replaces it with the new columns
def split_and_reorganize(theDataFrame):

    #df1 takes all the columns up to CourseSectionCode
    index = theDataFrame.columns.get_loc('coursesectioncode')
    df1 = pd.DataFrame(theDataFrame.iloc[:, :index+1])

    #CourseOfferingCode is split, new columns are appended and CourseSectionCode is dropped
    df1[['section', 'crn', 'term']] = theDataFrame.coursesectioncode.str.split("-", expand = True)
    df1 = df1.drop(['coursesectioncode'], axis = 1)

    #df2 takes all the columns after CourseSectionCode
    df2 = pd.DataFrame(theDataFrame.iloc[:, index+1:])

    #df1 and df2 are concatenated and returned
    frames = [df1, df2]
    theDataFrame = pd.concat(frames, sort = False, axis = 1)
    return theDataFrame

def output_processing(df):
    keptColumns = ["userid",	
                   "orgdefinedid",
                   "username",
                   "firstname",
                   "lastname",
                   "courseofferingname",
                   "section",
                   "crn",
                   "term",
                   "gradeitemcategoryname",
                   "gradeitemcategoryname_cleaned",
                   "gradeitemname",
                   "gradeitemname_cleaned",
                   "pointsnumerator",
                   "pointsdenominator",
                   "gradevalue",
                   "gradecomments"]
                          
    processedDf = df.reindex(columns = keptColumns) #Keep only the listed columns, if they don't exist just return a NaN column
    processedDf["gradevalue"] = processedDf["pointsnumerator"] / processedDf["pointsdenominator"]
    
    return processedDf
    

def validateMixed(df, data):
    validateMixedID = MIXED_TEXT(df,data)
    validateMixedID.run()
    info = validateMixedID.statistics()
    warnings = validateMixedID.get_warnings()
    errors = validateMixedID.get_errors()
    stat = namedtuple('name', 'err warn')

    theStats = stat(err = errors, warn = warnings)

    return(info, theStats)
   
def validatePlain(df,data):
    validatePlainText = PLAIN_TEXT(df,data)
    validatePlainText.run()
    info = validatePlainText.statistics()
    warnings = validatePlainText.get_warnings()
    errors = validatePlainText.get_errors()
    stat = namedtuple('name', 'err warn')

    theStats = stat(err = errors, warn = warnings)

    return(info, theStats)

def validateNum(df, length, data):
    validateNumeric = NUMERIC_ID(df,data)
    validateNumeric.run(length)
    info = validateNumeric.statistics()
    warnings = validateNumeric.get_warnings()
    errors = validateNumeric.get_errors()
    stat = namedtuple('name', 'err warn')

    theStats = stat(err = errors, warn = warnings)

    return(info, theStats)


def validateDate(df,data):
    validateDate = DATE(df,data)
    validateDate.run()
    info = validateDate.statistics()
    warnings = validateDate.get_warnings()
    errors = validateDate.get_errors()
    stat = namedtuple('name', 'err warn')

    theStats = stat(err = errors, warn = warnings)

    return(info, theStats)

def validateCRN(df, allSections,data):
    validateCRN = CRN(df, allSections)
    validateCRN.run()

    info = validateCRN.statistics()
    warnings = validateCRN.get_warnings()
    errors = validateCRN.get_errors()
    stat = namedtuple('name', 'err warn')

    theStats = stat(err = errors, warn = warnings)

    print(info)
    print(warnings)
    return(info, theStats)


def fuzzyMatchingCleaner(df, signal, threshold=80, n_match=None):
    cleanFuzzyMatching = FUZZY_MATCHING(df)
    cleanedColumn = cleanFuzzyMatching.run(signal, threshold= threshold, n_match = n_match)

    info = cleanFuzzyMatching.statistics()
    
    warnings = cleanFuzzyMatching.get_warnings()
    
    errors = cleanFuzzyMatching.get_errors()
    
    return cleanedColumn
    
def booleanCleaner(df):
    cleanBoolean = BOOLEAN_CLEANER(df)
    cleanedColumn = cleanBoolean.run()
    
    info = cleanBoolean.statistics()
    warnings = cleanBoolean.get_warnings()
    errors = cleanBoolean.get_errors()
    
    return cleanedColumn