
"""
	Filename: BCselector_test.py
	Programmer: Sean Thompson
	Date Created: 01/06/2020
	Last Update: created file
	Description: This file is for testing of the BCselector module"""

import unittest
import pandas as pd 
import glob as gb 
from enum import Enum 
from source.BCselector import get_base_column
#from cleaners import GRADE_ITEM_NAME


#setting for the displayed output (For testing)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


class TestBCselector(unittest.TestCase):

    def test_get_base_column(self):

         for file in gb.glob("testing/mock_data/*.csv"):
            #grab the base columns from the csv file
            df = pd.read_csv(file, usecols = list(range(0,18)), sep = ',')

            print(file)
            #testing split_and_reorganize with mis-ordered columns
            theData = get_base_column(df, "all")
            #print(x, '\n')
            allColumns = ["username", "firstname", "lastname", "roleid", "rolename", 
                            "courseofferingid", "courseofferingcode", "courseofferingname",
                            "name", "number", "term", "gradeitemcategoryid", "gradeitemcategoryname",
                            "gradeitemid", "gradeitemname", "gradeitemweight", "pointsnumerator", "pointsdenominator",
                            "gradevalue", "gradelastmodified"]

            assert theData.empty == False, "the dataframe is empty" #make sure the dataframe is not empty

            assert len(theData.columns) == 20, "not all columns were recovered" #check that the correct number of columns are returned
      
            #check for each of the base column headers by checking against/removing from allColumns array
            for oneColumn in theData:
                wholeColumn = theData[oneColumn]
                try:
                    allColumns.remove(wholeColumn.name)
                except:
                    self.fail('redundant column headers')

            #testing for username with mixedID validator
            x = get_base_column(df, "uSerName")
            print(x, '\n')
        
            assert x.empty == False, "the dataframe is empty"

            #testing for firstname with plainText validator
            x = get_base_column(df, "fIRStnamE")
            print(x, '\n')
            
            assert x.empty == False, "the dataframe is empty"
            
            #testing for gradeitemcategoryID with Numeric validator
            x = get_base_column(df, "graDeitemcategoryId")
            print(x,'\n')
            
            assert x.empty == False, "the dataframe is empty"
        
            #testing for gradeLastmodified with Date validator
            x = get_base_column(df, "gradeLastModifIed")
            print(x, '\n')
            
            assert x.empty == False, "the dataframe is empty"
        
    
if __name__  == "__main__":

    unittest.main()