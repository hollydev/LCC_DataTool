import unittest
import example_program

class test_program(unittest.TestCase):

	#This is a system test because it tests the whole program rather than just single functions.
	def test_calculate(self):
		input_string = '6+2'
		self.assertEqual(example_program.calculate(input_string),
						 8)

		input_string = '10-20'
		self.assertEqual(example_program.calculate(input_string),
						 -10)

		input_string = '600/6'
		self.assertEqual(example_program.calculate(input_string),
						 100)

		input_string = '230*2'
		self.assertEqual(example_program.calculate(input_string),
						 460)

		input_string = 'lolwat'
		self.assertEqual(example_program.calculate(input_string),
						 None)