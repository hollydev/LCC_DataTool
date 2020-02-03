import math

def addition(a, b):
	a, b = float(a), float(b)
	return(a+b)

def subtraction(a, b):
	a, b = float(a), float(b)
	return(a-b)

def multiplication(a, b):
	a, b = float(a), float(b)
	return(a*b)

def division(a, b):
	a, b = float(a), float(b)
	return(a/b)

def calculate(input_string):

	if '+' in input_string:
		a = input_string.split('+')[0]
		b = input_string.split('+')[1]
		ans = addition(a, b)

	elif '-' in input_string:
		a = input_string.split('-')[0]
		b = input_string.split('-')[1]
		ans = subtraction(a, b)

	elif '*' in input_string:
		a = input_string.split('*')[0]
		b = input_string.split('*')[1]
		ans = multiplication(a, b)

	elif '/' in input_string:
		a = input_string.split('/')[0]
		b = input_string.split('/')[1]
		ans = division(a, b)

	else:
		ans = None

	return ans