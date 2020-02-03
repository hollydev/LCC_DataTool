
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

        #testing for username with mixedID validator
        x = get_base_column("uSerName")
        print(x, '\n')
       
        assert len(x) != 0, "the list is empty"

        #testing for firstname with plainText validator
        x = get_base_column("fIRStnamE")
        print(x, '\n')
        
        assert len(x) != 0, "the list is empty"
        
        #testing for gradeitemcategoryID with Numeric validator
        x = get_base_column("graDeitemcategoryId")
        print(x,'\n')
        
        assert len(x) != 0, "the list is empty"
       
       #testing for gradeLastmodified with Date validator
        x = get_base_column("gradeLastModifIed")
        print(x, '\n')
        
        assert len(x) != 0, "the list is empty"
        
    
if __name__  == "__main__":

    unittest.main()