import unittest

import src.main.python.lcc_assessment.analyzePath as analyzePath

class Test_analyzeData(unittest.TestCase):
    
    def test_ProgramArea(self):
        path = r"D2L Data\A&S\AAST\Spring 19\fileName"
        self.assertEqual(analyzePath.get_program_area(path),'A&S')
        path = r"D2L Data\A&S\English-SocialScience\Archived\Fall 15\fileName"
        self.assertEqual(analyzePath.get_program_area(path),'A&S')
        self.assertEqual(analyzePath.get_program_area(""),'N/A')
        path = "D2L Data\HHS\Spring 2019\fileName"
        self.assertEqual(analyzePath.get_program_area(path),'HHS')
        path = r"D2L Data\TC\Archived\Spring 16\fileName"
        self.assertEqual(analyzePath.get_program_area(path),'TC')
        
    def test_Department(self):
        path = r"D2L Data\A&S\English-SocialScience\Archived\Summer 17\fileName"
        self.assertEqual(analyzePath.get_department(path),'English-SocialScience')
        path = r"D2L Data\A&S\AAST\Spring 19\fileName"
        self.assertEqual(analyzePath.get_department(path),'AAST')
        path = r"D2L Data\A&S\Science-Math\Archived\Fall 16\fileName"
        self.assertEqual(analyzePath.get_department(path),'Science-Math')
        path = r"D2L Data\A&S\Science-Math\Fall 19\fileName"
        self.assertEqual(analyzePath.get_department(path),'Science-Math')
        path = r"D2L Data\TC\Archived\Fall 15\fileName"
        self.assertEqual(analyzePath.get_department(path),'N/A')
        
if __name__ == '__main__':
    unittest.main()