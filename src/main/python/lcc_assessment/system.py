from messages.system import SYSTEM, LOG
import lcc_assessment.BCselector as base_selector
import lcc_assessment.output as outputs
import os
import numpy as np

def remove_duplicates(lst):
    '''
    Removes duplicates from given list
    @Params:
        lst - a list
    
    @Returns:
        re_list - a list of strings without duplicates
    '''
    ret_list = list(set(lst))
    for element in ret_list:
        if type(element) != str:
            ret_list.remove(element)
    return ret_list


def get_last(element):
    '''
    Returns the last word in the string
    @Params:
        element - a string (an instructor name)
    @Returns:
        names[-1] - the last word in the string (the instructors last name)
    '''
    names = element.split()
    if(len(names) == 0):
        ret = ""
    else:
        ret = names[-1]
    return ret
    
def get_instructors(data):
    '''
    Takes a data frame and returns a list of unique instructor names
    @Params:
        data - the pandas data frame
        
    @Returns:
        ret_list - a list of all unique instructor names
    '''
    ret_list = []
    try:
        names = data['GraderFirstName'] + ' ' + data['GraderLastName']
        names = names.fillna('')
    except KeyError:
        names = ["No instructors found"]
    
    ret_list = remove_duplicates(names) #Use a set to remove duplicates.
    ret_list.remove('') #Remove blank entries if they exist.
    ret_list.sort(key=get_last)
    
    return ret_list

def get_termcodes(data):
    '''
    Takes a pandas data frame and returns a list of unique termcodes
    
    @Params:
        data - The pandas data frame
        
    @Returns:
        ret_list - a list of all unique termcodes with 
        (Spring/Fall/Summer) + year appended to each termcode
    '''
    ret_list = []
    dates = data['CourseSectionCode']
    
    for date in dates:
        if type(date) == str:
            date = date[-6:]
            
            if date[-2:] == '10':
                term = 'Fall'
            elif date[-2:] == '20':
                term = 'Spring'
            else:
                term = 'Summer'
            
            date = date + ' - ' + term + ' ' + date[:4] 
            ret_list.append(date)    

    ret_list = remove_duplicates(ret_list)  
    ret_list.sort()
    
    return ret_list
    
def validate_path(checkPath):
        """ Check if the given path is valid. Checks emptp paths and path.exists() errors.

        @Params:
            cls - self object allows access to set path and outName.
            checkPath - A string indicating the path to check for validity.
            

        @Returns:
            BOOLEAN - Indicates whether new path is valid.
            
        @Raises:
            TypeError - Indicates the given path variable is not a string.
        """
        #Check type
        if(not isinstance(checkPath, str)):
            raise TypeError(SYSTEM.TypeException.format(type(str), type(checkPath))) #{} Expected, {} Got
        
        #Validate empty path, trim extra spaces and see if the path minimized to empty.
        if(checkPath.strip() == ''):
            print(SYSTEM.emptyPath)
            print(LOG.emptyPath)
            return False

        #Check if the path exists
        if(not os.path.exists(checkPath)):
            try:
                os.stat(checkPath)
            except:
                print(LOG.notPath_stat.format(checkPath))
                return False
        
            print(SYSTEM.notPath)
            print(LOG.notPath)
            return False

        return True

def cleaned_data(df):
    """
        Get the data frame that has been validated and perform final processing steps, prior to outputting.
        
        @Params:
            df - The dataframe to be cleaned update.
            
        @Returns
            cleaned_df - The processed data frame to be output.
    """        
    return base_selector.output_processing(df)
    
def clean(df, signal):
    """
        Calls the call_cleaner function from BCSelector to get the cleanedColumn
        @Params:
            df - The column to be cleaned
            signal - 
        @Returns:
            the cleaned column
    """
    cleanedColumn = base_selector.call_cleaner(df, signal)
    return cleanedColumn
    
def get_cleaners_list():
    """
        Calls the cleaners_list function from BCSelector to be list of cleaners
        set to a column name
        @Params:
            
        @Returns:
            a named dictionary being applied
    """
    return base_selector.cleaners_list()

def main(selectedColumns, data, signal):
    """ 
		Serves as a controller for the system as a whole. Manages the messages of
		different components, and handles data calls to the GUI.
	"""
	#Calling the Base Column Selector to handle validation.
    theInfo = base_selector.get_base_column(data, selectedColumns, signal)
    return theInfo

	