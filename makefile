#Data tool make file. Automates key functions. Including a help function.
#
#
#run:
#	python3 source/solve.py

test-unit:
	pytest testing/unit/

test-system:
	pytest testing/system/

test-all:
	pytest testing/
tar:
	tar -czvf LCC_Data_Tool.tar.gz .

readme:

help:
		@echo "\trun"
		@echo "\t\tRun the program for user input"
		@echo "\ttest-"
			@echo "\t\ttest-unit - Perform unit tests"
			@echo "\t\ttest-system - Perform system tests"
			@echo "\t\ttest-all - Perform all tests"
		@echo "\ttar"
		@echo "\t\tCreates a tar file of the directory"

