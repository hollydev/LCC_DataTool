import unittest
import example_program #Import the file that you want to test!

class test_program(unittest.TestCase):

	#Optional set up statement
	def set_up(self):
		#Create mock objects
		mock_object = 1

	def test_addition(self):
		a, b = 1, 3
		self.assertEqual(example_program.addition(a, b), 4)

		a, b = 1, -3
		self.assertEqual(example_program.addition(a, b), -2)

		a, b = 1, float("nan")
		#NaN != NaN
		self.assertNotEqual(example_program.addition(a, b), float("nan"))

		a, b = float("inf"), 5
		self.assertEqual(example_program.addition(a, b), float("inf"))

		a, b = float("inf"), 5
		self.assertEqual(example_program.addition(a, b), float("inf"))

	def test_will_fail(self):
		a, b = None, None
		self.assertEqual(example_program.addition(a, b), None)
		
	#test subtraction()
	#test multiplication()
	#test division()

	def tear_down(self):
		#Tear down any objects as needed
		mock_object = None