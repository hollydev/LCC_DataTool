import source.output as testTarget
import unittest
from contextlib import contextmanager

#Import libraries for use in tests
import pandas
import pickle


@contextmanager
def mockOverwriteInput(mock):
	original_check_overwrite = __builtins__.check_overwrite
	__builtins__.check_overwrite = lambda _: mock
	yeild
	__builtins__.check_overwrite = original_check_overwrite

class FILE_WRITER_TEST_CASE(unittest.TestCase):

	def test_empty_init(self):
		try:
			writer = testTarget.FILE_WRITER("C:\\invalid;pathname,.;'.csv")
			self.assertEqual(e == "Writer points to invalid file or path. Entered path was C:/SampleFolder")
		finally:
			writer = testTarget.FILE_WRITER("C:\\SampleFolder")


		#Object assertions
		self.assertIsNotNone(writer)
		self.assertIsInstance(writer, testTarget.FILE_WRITER("test"))

		#Attribute assertions
		self.assertIsNotNone(writer.outName)
		self.assertIsNotNone(writer.path)
		self.assertEqual(writer.path, 'C:\\SampleFolder')
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