"""
	Filename: BCselector.py
	Programmer: Sean Thompson
	Date Created: 01/02/2020
	Last Update: created file
	Description: This file contains functions for retrieving the base columns of a
     dataframe that is created from a csv file"""

import pandas as pd 
import glob as gb 

#setting for the displayed output (For testing)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)



def get_username():
    #using glob to find all files in the subdirectory 'GBsample' that have the .csv extension
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(0, 1)), sep = ',')


        #TODO: add logic for cleanup/validation



        return df
        # print(file)
        # print(df)


def get_firstname():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(1, 2)), sep = ',')


        #TODO: add logic for cleanup/validation


        return df
        # print(file)
        # print(df)

def get_lastname():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(2, 3)), sep = ',')

        #TODO: add logic for cleanup/validation



        return df
        # print(file)
        # print(df)

def get_role_id():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(3, 4)), sep = ',')

        #TODO: add logic for cleanup/validation



        return df
        # print(file)
        # print(df)

def get_role_name():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(4, 5)), sep = ',')


        #TODO: add logic for cleanup/validation



        return df
        # print(file)
        # print(df)


def get_course_offering_id():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(5, 6)), sep = ',')

        #TODO: add logic for cleanup/validation



        return df
        # print(file)
        # print(df)

def get_course_offering_code():
    for file in gb.glob("./GBinfo/*.csv"):
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(6, 7)), sep = ',')

        #TODO: add logic for cleanup/validation



        return df
        # print(file)
        # print(df)

def get_course_offering_name():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(7, 8)), sep = ',')

        #TODO: add logic for cleanup/validation


        return df
        # print(file)
        # print(df)
       

def get_course_section_code():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(8, 9)), sep = ',')

        #TODO: add logic for cleanup/validation

        return df
        # print(file)
        # print(df)

def get_grade_item_category_id():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(9, 10)), sep = ',')

        #TODO: add logic for cleanup/validation

        return df
        # print(file)
        # print(df)

def get_grade_item_category_name():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(10, 11)), sep = ',')

        #TODO: add logic for cleanup/validation

        return df
        # print(file)
        # print(df)

def get_grade_item_id():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(11, 12)), sep = ',')

        #TODO: add logic for cleanup/validation


        return df
        # print(file)
        # print(df)

def get_grade_item_name():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(12, 13)), sep = ',')

        #TODO: add logic for cleanup/validation


        return df
        # print(file)
        # print(df)

def get_grade_item_weight():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(13, 14)), sep = ',')

        #TODO: add logic for cleanup/validation

        return df
        # print(file)
        # print(df)

def get_points_numerator():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(14, 15)), sep = ',')


        #TODO: add logic for cleanup/validation

        return df
        # print(file)
        # print(df)

def get_points_denominator():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(15, 16)), sep = ',')

        #TODO: add logic for cleanup/validation


        return df
        # print(file)
        # print(df)

def get_grade_value():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(16, 17)), sep = ',')

        #TODO: add logic for cleanup/validation


        
        print(file)
        print(df)

def get_grade_last_modified():
    for file in gb.glob("./GBinfo/*.csv"):
       
                                         #targeted column
        df = pd.read_csv(file, usecols = list(range(17, 18)), sep = ',')

        #TODO: add logic for cleanup/validation


        
        print(file)
        print(df)



