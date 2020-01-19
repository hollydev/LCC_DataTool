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

import messages

class FILE_WRITER():
	self.messages = []
	self.log = []

	def __init__(self, outName=None, outPath=None):
		if(outPath == None):
			self.path = get_path()
			self.outName = "combined_gradebook"

		#Validate the path on initialization.
		validate_path(self.path)

	def validate_path(cls, checkPath):
		""" Check if the given path is valid. Checks emptp paths and path.exists() errors.

		@Params:
			cls - self object allows access to set path and outName.
			outName (optional) - A string indicating the name of the output file.
			outPath (optional) - A path indicating the output location.
			

		@Returns:
			BOOLEAN - Indicates whether new path is valid.
		"""
		#Validate empty path, trim extra spaces and see if the path minimized to empty.
		if(checkPath.strip() == ''):
			cls.messages.append(messages.SYSTEM.emptyPath)
			cls.log.append(messages.SYSTEM.emptyPath_log)
			return False

		#Check if the path exists
		if(not os.path.exists(checkPath)):
			try:
				os.stat(checkPath)
			except:
				cls.log.append(messages.SYSTEM.notPath_stat_log)
				return False
		
			cls.messages.append(messages.SYSTEM.notPath)
			cls.log.append(messages.SYSTEM.notPath_log)
			return False

		return True
	
	def get_path(cls):
		""" Get a path to initialize the writer."""

	def set_path(cls, newPath):
		""" Setter method ensuring that new path is valid.

		@Params:
			cls - self object allows access to set path and outName.
			newPath - A string indicating the new path given

		@Returns:
			BOOLEAN - Indicates whether new path was set.
		"""
		if(not isinstance(newPath, str)):
			cls.log.append(messages.SYSTEM.notStringPath)
			return False
		
		if(cls(path) == newPath):
			cls.log.append(messages.SYSTEM.newPathSame.format(newPath))
			return True

		if(validate_path(newPath)):
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
				overwriteOkay = input(messages.SYSTEM.overwrite % cls.outName).lower()
				if (overwriteOkay == "yes" or\
					overwriteOkay == "y"):
					return True
				elif (overwriteOkay == "no" or\
					  overwriteOkay == "n"):
					return False
				else:
					return False

			self.messages.append(messages.SYSTEM.existingFile)
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
		
