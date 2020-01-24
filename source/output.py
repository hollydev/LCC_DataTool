"""
    Filename: output.py
    Programmer: Holly Locke
    Date Created: 01/13/2020
    Last Update: File Created

    Description: This script provides functionality for saving a data frame to a memory object.
    Available memory types include: CSV, (Excel?), Oracle SQL

"""

import pandas as pd
import numpy as np
import csv
import pickle
import os

from messages.system import SYSTEM, LOG

# class InvalidPathError(Error):
# 	def __init__(self, expression, message):
# 		self.expression = expression
# 		self.messages = message

class FILE_WRITER():
	messages = []
	log = []

	def __init__(self, outPath=None, outName=None):
		""" Writer init function. Handles all file writing capabilites. Performs path validation
		on each instance. 

		@Params:
			self  - self object allows access to set path and outName.
			outPath - A string indicating the name of the output file.
			outPath (optional) - A path indicating the output location.
			
		@Raises:
			FileNotFoundError - Indicates the given path does not point to a valid file or directory.
		"""
		self.outName = "combined_gradebook"

		#Validate the path on initialization.
		if outPath == None:
			self.path = os.getcwd()
		
		elif not self.validate_path(outPath):
			raise FileNotFoundError("Writer points to invalid file or path. Entered path was {}".format(outPath))
		

	def validate_path(cls, checkPath):
		""" Check if the given path is valid. Checks emptp paths and path.exists() errors.

		@Params:
			cls - self object allows access to set path and outName.
			checkPath - A string indicating the path to check for validity.
			

		@Returns:
			BOOLEAN - Indicates whether new path is valid.
		"""

		#Validate empty path, trim extra spaces and see if the path minimized to empty.
		if(checkPath.strip() == ''):
			cls.messages.append(SYSTEM.emptyPath)
			cls.log.append(LOG.emptyPath)
			return False

		#Check if the path exists
		if(not os.path.exists(checkPath)):
			try:
				os.stat(checkPath)
			except:
				cls.log.append(LOG.notPath_stat)
				return False
		
			cls.messages.append(SYSTEM.notPath)
			cls.log.append(LOG.notPath)
			return False

		return True
	
	def get_path(cls):
		""" Get a path to initialize the writer."""
		return input("No Path provided. Enter a path: ")

	def set_path(cls, newPath):
		""" Setter method ensuring that new path is valid.

		@Params:
			cls - self object allows access to set path and outName.
			newPath - A string indicating the new path given

		@Returns:
			BOOLEAN - Indicates whether new path was set.
		"""
		if(not isinstance(newPath, str)):
			cls.log.append(SYSTEM.notStringPath)
			return False
		
		if(cls(path) == newPath):
			cls.log.append(SYSTEM.newPathSame.format(newPath))
			return True

		if(self.validate_path(newPath)):
			cls.path = newPath
			return True

		print("uncaught case")
		return False

	
	def check_overwrite(cls):
		""" Check if the path points to an existing file. If so verify if okay to overwrite.

		@Params:
			cls - self object allows access to set path and outName.

		@Returns:
			BOOLEAN - Indicates whether okay to overwrite. True = okay.
		"""
		
		#Get the path and name lengths
		nameLength = len(cls.outName)
		pathLength = len(cls.path)

		#Get the start and end index. 4 indicates a file type .XXX
		iStart = pathLength - nameLength - 4
		iEnd = pathLength - 4

		#Check if path points to a file.
		if(os.path.isfile(cls.path)):
			"""TODO: When GUI change overwrite handler to Windows"""
			#Check if the file has the same name, check overwrite ok.
			if(self.path.endswith(cls.outName, iStart, iEnd)):
				overwriteOkay = input(SYSTEM.overwrite % cls.outName).lower()
				if (overwriteOkay == "yes" or\
					overwriteOkay == "y"):
					return True
				elif (overwriteOkay == "no" or\
					  overwriteOkay == "n"):
					return False
				else:
					return False

			self.messages.append(SYSTEM.existingFile)
		else:
			return True


	def available_types(cls, file):
		""" Provide a list of file types which are available to save.
			TODO: Provide a list based on the filetype of the parameter.

			@Params:
				cls - self object allows access to set path and outName.
				file - The file to be saved. For file type checking.

			@Returns:
				types - A list of file types which are available for the file.
		"""

		#If the file is a data frame
		if(isinstance(file, pd.DataFrame)):
			return(["CSV, XLSX, Pickle"])
		else:
			return(["Pickle"])

	
	def write_csv(cls, file):
		""" Saving of csv files for files produced by
		the application.

		@Params:
			cls - self object allows access to set path and outName.
			file - The file to be saved.
			path - The path where the file should be saved.
		
		@Returns:
			Saved - Boolean - Indicates whether the file was saved successfully.
		"""

		#Save Pandas DF using Pandas
		if(isinstance(file, pd.DataFrame)):
			pd.to_csv(file, cls.path, index=False, sort=False)
		
		#Save dict object using CSV
		elif (isinstance(file, dict)):
			#Use the csv package to handle writing dicts to files.
			writer = csv.Writer(cls.path)

			for row in file:
				writer.WriteRow(line)

	def write_pickle(cls, file):
		""" Saving of pickle objects for later use by the python program.

		@Params:
			file - The file to be pickled.
		"""

		#Save the pickle object, a serialized representation.
		if(isinstance(file, pd.DataFrame)):
			cls.fileName = cls.fileName + "_pandasDataFrame"
		elif (isinstance(file, pd.Series)):
			cls.fileName = cls.fileName + "_pandasSeries"
		
		if(check_overwrite(cls.outPath) == True):
			try:
				outFile = open(cls.outPath + cls.fileName, 'rw')
				pickle.dump(file, outFile)
				outFile.close()

			except OSError as e:
				print("Unable to open file, please try again.", e)
