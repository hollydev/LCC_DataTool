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

	def __init__(self, outpath=None):
		if(outpath == None):
			self.path = get_output_path()

		#Validate the path on initialization.
		validate_path(self.path)

	def validate_path(cls):
		#Validate empty path
		if(self.path.strip() == ''):
			#Trim extra spaces and see if the path minimized to empty.
			self.messages.append(messages.SYSTEM.emptyPath)

		#

	""" Provide a list of file types which are available to save.
		TODO: Provide a list based on the filetype of the parameter.

		@Params:
			file - The file to be saved. For file type checking.

		@Returns:
			types - A list of file types which are available for the file.
	"""
	def available_types(cls, file):
		#If the file is a data frame
		if(isinstance(file, pd.DataFrame)):
			return(["CSV, XLSX"])
		else:
			return(["No saving functionality exists for this file."])

	""" This function handles the saving of csv files for files produced by
		the application.

		@Params:
			file - The file to be saved.
			path - The path where the file should be saved.
		
		@Returns:
			Saved - Boolean - Indicates whether the file was saved successfully.
	"""
	def write_csv(cls, file)
		if(isinstance(file, pd.DataFrame)):
			pd.to_csv(file, cls(path), index=False, sort=False)
		
		elif (isinstance(file, dict)):
			#Use the csv package to handle writing dicts to files.
			writer = csv.Writer(cls(path))

			for row in file:
				writer.WriteRow(line)

	def write_pickle(cls, file)
		if(isinstance(file, pd.))
