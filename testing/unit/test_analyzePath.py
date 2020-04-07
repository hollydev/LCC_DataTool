import unittest
import analyzePath
import getFiles

class Test_analyzeData(unittest.TestCase):
    
    files = getFiles.get_files("./D2L Data")
    
    def test_ProgramArea(self):
        self.assertEqual(analyzePath.get_program_area(self.files[0]),'A&S')
        self.assertEqual(analyzePath.get_program_area(self.files[20]),'A&S')
        self.assertEqual(analyzePath.get_program_area(""),'N/A')
        self.assertEqual(analyzePath.get_program_area(self.files[11000]),'HHS')
        self.assertEqual(analyzePath.get_program_area(self.files[15000]),'TC')
        
    def test_Department(self):
        self.assertEqual(analyzePath.get_department(self.files[0]),'N/A')
        self.assertEqual(analyzePath.get_department(self.files[20]),'AAST')
        self.assertEqual(analyzePath.get_department(self.files[8000]),'Science-Math')
        self.assertEqual(analyzePath.get_department(self.files[9999]),'Science-Math')
        self.assertEqual(analyzePath.get_department(self.files[15000]),'N/A')
        
if __name__ == '__main__':
    unittest.main()