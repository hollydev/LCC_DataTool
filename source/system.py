from messages.system import SYSTEM, LOG

import source.getFiles as inputs
import source.BCselector as base_selector
import source.output as outputs

import pandas
import numpy
import tqdm
import os

def get_instructors(data):
    ret_list = []
    names = data['GraderFirstName'] + ' ' + data['GraderLastName']
    
    for name in names:   
        if type(name) == str:
            duplicate = False
    
            if name in ret_list:
                duplicate = True
                    
            if duplicate == False:
                ret_list.append(name)
              
    return ret_list

def get_termcodes(data):
    ret_list = []
    dates = data['CourseSectionCode']
    
    for date in dates:
        if type(date) == str:
            duplicate = False
            date = date[14:]
            
            if date[-2:] == '10':
                term = 'Fall'
            elif date[-2:] == '20':
                term = 'Spring'
            else:
                term = 'Summer'
            
            date = date + ' - ' + term + ' ' + date[:4] 
                
            
            if date in ret_list:
                duplicate = True
            if duplicate == False:
                ret_list.append(date)
            
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


def main(selectedColumns, data):
	""" 
		Serves as a controller for the system as a whole. Manages the messages of
		different components, and handles data calls to the GUI.
	"""

	#Calling the Base Column Selector to handle validation.
	theInfo = base_selector.get_base_column(data, selectedColumns) #Handle data validation.


	#Save files to directory
	writePath = input("Path: ").lower()
	writePath = writePath.replace("\"", "")

	if(validate_path(writePath) == True):
		#Create a file writer
		fileWriter = outputs.FILE_WRITER(outPath= writePath, outName= "TestingFile")

		#Write a CSV to the output path.
		fileWriter.write_csv(data)

		#TODO Implement Oracle writer
	return theInfo


