from messages.system import SYSTEM, LOG

import source.getFiles as inputs
import source.BCselector as base_selector
import source.output as outputs

import pandas
import numpy
import tqdm
import os


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


def main():
	""" 
		Serves as a controller for the system as a whole. Manages the messages of
		different components, and handles data calls to the GUI.
	"""

	#Getting the data
	#####
	## TODO: Add GUI call to windows explorer to get the reading path
	#####
	readPath = input("Path: ").lower()
	readPath = readPath.replace("\"", "")
	while(readPath != "exit" and readPath != "quit"):
		if(validate_path(readPath) == True):
			#Get the list of valid CSV files to read.
			files = inputs.get_files(readPath)

			if(len(files) == 0):
				print(SYSTEM.noFilesFound)
				break

			frames = inputs.get_data_frames(files)
			data = inputs.concat_data_frames(frames)

			break
		else:
			readPath = input("Path: ").lower()
			readPath = readPath.replace("\"", "")

	#Calling the Base Column Selector to handle cleaning and validation.
	base_selector.get_base_column(data) #Handle data validation.

	#Handle data cleaning.

	



if __name__ == '__main__':
	main()
