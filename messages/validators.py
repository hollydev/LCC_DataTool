
################
## Validators ##
################
class VALIDATORS:
	def __init__(self):
		pass

	#Numeric ID
	success = "Validator [%s] ran successfully."
	failure = "Validator [%s] failed to pass."
	notNumeric = "%s contains a non-numeric character."
	notUniqueDup = "%i ID is not unique. Duplicate entry found at %i"
	notUniqueMult = "Multiple IDs found. Duplicate entries found at %s"
	length = "%i is of length %i, expected length %i"


	#Mixed ID
	expectMixedNum = "%s contains only numeric values, expected mixed values"
	expectMixedChar = "%s contains only character values, expected mixed values"