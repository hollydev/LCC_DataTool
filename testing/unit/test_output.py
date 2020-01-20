import source.output as testTarget
import unittest

#Import libraries for use in tests
import pandas
import pickle

class FILE_WRITER_TEST_CASE(unittest.TestCase):

	def test_empty_init(self):
		writer = testTarget.FILE_WRITER()

		#Object assertions
		self.assertIsNotNone(writer)
		self.assertIsInstance(testTarget.FILE_WRITER())

		#Attribute assertions
		self.assertIsNotNone(writer.outName)
		self.assertIsNotNone(writer.path)
		self.assertIsEqual(writer.outName, "combined_gradebook")


	#INIT test

	#Validate Path test
	def test_validatePath(self):
		pass

	#Set Path test

	#Get Path test

	#Check Overwrite

	#Get types test

	#Write CSV test

	#Write Pickle test