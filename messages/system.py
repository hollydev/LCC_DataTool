"""
	Filename: messages.py
	Programmer: Holly Locke
	Date Created: 01/03/2020
	Last Update: File Created

	Description: This file contains warning messages to be used throughout the program. Using
	this file will provide a central place to modify, add, or remove error messages. Additionally
	classes are created to display warning messages.
"""

################
##   System   ##
################
class SYSTEM:
	def __init__(self):
		pass

	#System Statistics Messages
	validatorStats = "Validator [%s]: Items Validated [%i]\t Warnings: [%i]\t Errors: [%i]"
	 
	#System Output Messages
	emptyPath = "Found empty path, enter a valid path."
	notPath = "Entered path is invalid. Please check to make sure the folder exists."
	notPath_stat = "Unable to check status of the given path. Contact the analyst."
	overwrite = "File {} already exists. Do you want to overwrite the file? (Yes/No)"
	newPathSame = "Given path '{}' matches current output path."

class LOG:
	def __init__(self):
		pass


	notPath = "User entered {}. Failed to validate file path using 'os' package."
	notPath_stat = "User entered {}. os.stat() call failed. Check permissions of path."
	emptyPath = "User entered {}. When stripped string is empty."