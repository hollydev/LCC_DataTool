import source.output as testTarget
import unittest
from contextlib import contextmanager

#Import libraries for use in tests
import pandas
import pickle
import os

@contextmanager
def mockOverwriteInput(mock):
	original_check_overwrite = __builtins__.check_overwrite
	__builtins__.check_overwrite = lambda _: mock
	yeild
	__builtins__.check_overwrite = original_check_overwrite

class FILE_WRITER_TEST_CASE(unittest.TestCase):
	def setUp(self):
		"""Verify they integrity of tests by creating a temporary
		local directory for testing. This ensures that tests will run
		in all Windows systems."""

		try:
			self.file  = os.mkdir("C:/SampleFolder")
		except OSError:
			print("Failed to create testing directory, some tests might fail.")

		testFile = open("C:/SampleFolder/testfile.csv", "w")
		testFile.write("This, is, A, CSV")

		testFile.close()

	#INIT test
	def test_empty_init(self):

		#init and validation
		writer = testTarget.FILE_WRITER("C:/SampleFolder")

		#Object assertions
		with self.assertRaises(FileNotFoundError):
			testTarget.FILE_WRITER("broken path string")
	
		self.assertIsNotNone(writer)
		self.assertIsInstance(writer, testTarget.FILE_WRITER)

		#Attribute assertions
		self.assertIsNotNone(writer.outName)
		self.assertIsNotNone(writer.outPath)
		self.assertEqual(writer.outPath, 'C:/SampleFolder')
		self.assertEquals(writer.outName, "combined_gradebook")

	#Validate Path test
	def test_validatePath(self):
		writer = testTarget.FILE_WRITER("C:/")
	
		#Check invalid paths
		self.assertFalse(writer.validate_path("testing lol"))
		self.assertFalse(writer.validate_path("Thisisntapath"))
		self.assertFalse(writer.validate_path("''''"))
		self.assertFalse(writer.validate_path("\.\/s\s\ds"))
		self.assertFalse(writer.validate_path("213123123213"))
		self.assertFalse(writer.validate_path("C:/Idontexist"))
		self.assertFalse(writer.validate_path("C:/%username%"))
		self.assertFalse(writer.validate_path("~%"))
		self.assertFalse(writer.validate_path("/%"))
		self.assertFalse(writer.validate_path("--"))
		self.assertFalse(writer.validate_path("echo testing"))
		self.assertFalse(writer.validate_path("ls"))
		self.assertFalse(writer.validate_path(""))
		self.assertFalse(writer.validate_path("  "))
		self.assertFalse(writer.validate_path("                           "))

		#Check valid paths
		self.assertTrue(writer.validate_path("C:/"))
		self.assertTrue(writer.validate_path("C:\\"))
		self.assertTrue(writer.validate_path("C:/SampleFolder"))
		self.assertTrue(writer.validate_path("C:\\SampleFolder"))
		self.assertTrue(writer.validate_path("C:\\Users\\"))
		self.assertTrue(writer.validate_path("C:\\Windows\\System32"))

		#Check wrong type
		with self.assertRaises(TypeError):
			writer.validate_path(int(5))
			writer.validate_path(dict({1:"string"}))
			writer.validate_path(True)
			writer.validate_path(pd.DataFrame())
			writer.validate_path(pd.Series())
			writer.validate_path()


	#Get Path test
	def test_getPath(self):
		writer = testTarget.FILE_WRITER("C:/")

		self.assertIsInstance(writer.get_path(), str)
		self.assertNotEqual(len(writer.get_path()), 0)

		with self.assertRaises(TypeError):
			writer.get_path("too many params")
	
	#Set Path test
	def test_setPath(self):
		writer = testTarget.FILE_WRITER("C:/")
		originalPath = "C:/"
	
		#Check invalid paths are not set
		self.assertFalse(writer.set_path("testing lol"))
		self.assertFalse(writer.set_path("Thisisntapath"))
		self.assertFalse(writer.set_path("''''"))
		self.assertFalse(writer.set_path("\.\/s\s\ds"))
		self.assertFalse(writer.set_path("213123123213"))
		self.assertFalse(writer.set_path("C:/Idontexist"))
		self.assertFalse(writer.set_path("C:/%username%"))
		self.assertFalse(writer.set_path("~%"))
		self.assertFalse(writer.set_path("/%"))
		self.assertFalse(writer.set_path("--"))
		self.assertFalse(writer.set_path("echo testing"))
		self.assertFalse(writer.set_path("ls"))
		self.assertFalse(writer.set_path(""))
		self.assertFalse(writer.set_path("  "))
		self.assertFalse(writer.set_path("                           "))


		#Check valid paths are set
		self.assertTrue(writer.set_path("C:/"))
		self.assertTrue(writer.set_path("C:\\"))
		self.assertTrue(writer.set_path("C:/SampleFolder"))
		self.assertTrue(writer.set_path("C:\\SampleFolder"))
		self.assertTrue(writer.set_path("C:\\Users\\"))
		self.assertTrue(writer.set_path("C:\\Windows\\System32"))


		# Check wrong type
		with self.assertRaises(TypeError):
			writer.set_path(int(5))
			writer.set_path(dict({1:"string"}))
			writer.set_path(True)
			writer.set_path(pd.DataFrame())
			writer.set_path(pd.Series())
			writer.set_path()

	#Check Overwrite test
	def test_checkOverwrite(self):
		freeWriter = testTarget.FILE_WRITER(outPath="C:/SampleFolder/", outName="IDontExist")
		overWriter = testTarget.FILE_WRITER(outPath="C:/SampleFolder/", outName="testfile")
		invalidWriter = testTarget.FILE_WRITER(outPath="C:/", outName="")

		#Check non-overwrites
		self.assertTrue(freeWriter.check_overwrite())

		freeWriter.outName = "anotherFakeFile"
		self.assertTrue(freeWriter.check_overwrite())

		#Check valid overwrites
		self.assertTrue(overWriter.check_overwrite())

		#Invalid Filename
		# with self.assertRaises(ValueError):
		self.assertTrue(invalidWriter.check_overwrite())

	#Write CSV test
	def test_writeCSV(self):
		writer = testTarget.FILE_WRITER("C:/SampleFolder")

		sampleCSV = ["This", "is", "A", "CSV"]
		simpData = [[1,2,3,4,5], ["A","B","C","D","E"]]
		namedData = {"Nums":[1,2,3,4,5], "Letters":["A","B","C","D","E"]}
		panData = pandas.DataFrame([[1,2,3,4,5],["A","B","C","D","E"]])

		#Test normal writes.
		# self.assertTrue(writer.write_csv(simpData))
		self.assertTrue(writer.write_csv(namedData))
		self.assertTrue(writer.write_csv(panData))

		#Test locked file
		lock = open("combined_gradebook.csv", "rw")
		lock2 = open("combined_gradebook.h5", "rw")
		with self.assertRaises(OSError):
			self.assertTrue(testTarget.write_csv(namedData))
			self.assertTrue(testTarget.write_csv(panData))



	#Write Pickle test
	
	#SQL Writer test


	def tearDown(self):
		file = open("C:/SampleFolder/testfile.txt", "r")
		content = file.readlines()
		file.close()

		print("File contents should list: [{}]".format("This content should stay intact throughout the tests."))
		print("File output during tearDown method is:\n{}".format(content))
