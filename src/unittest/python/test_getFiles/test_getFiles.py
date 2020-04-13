import unittest
import src.unittest.python.test_getFiles.mock_getFiles as getFiles

class test_getFiles(unittest.TestCase):
    def test_checkFiles(self):
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160411_ELTE274-52356-201920.csv'
        self.assertEqual(getFiles.check_file(fileName),True)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD125-51373-201920_Test195'
        self.assertEqual(getFiles.check_file(fileName),False)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD115-51731-201920.csv'
        self.assertEqual(getFiles.check_file(fileName),True)
        
        fileName = r'.\D2l Data\A&S\CTL\Archived\Spring 17\AllGradesExport_AAST290-82669-201720.csv'
        self.assertEqual(getFiles.check_file(fileName),True)
        
        fileName = r'.\D2l Data\A&S\AAST\Spring 19\AllGradesWithWithdrawnStudents_20190509_182624_AAST290-51671-201920_Test406.csv'
        self.assertEqual(getFiles.check_file(fileName),False)
        
    def test_check_file_name(self):
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160411_ELTE274-52356-201920.csv'
        unwanted = [r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160411_ELTE274-52356-201920.csv']
        self.assertEqual(getFiles.check_file_name(fileName,unwanted), False)
        
        fileName = r'.\Good file name'
        unwanted = ['bad files']
        self.assertEqual(getFiles.check_file_name(fileName,unwanted), True)
        
        fileName = r'.\D2l Data\A&S\CTL\Archived\Spring 17\AllGradesExport_AAST290-82669-201720.csv'
        unwanted = []
        self.assertEqual(getFiles.check_file_name(fileName,unwanted), True)
        
        fileName = r'.\D2l Data\A&S\CTL\Archived\Spring 17\AllGradesExport_AAST290-82669-201720.csv'
        unwanted = [r".\D2l Data"]
        self.assertEqual(getFiles.check_file_name(fileName,unwanted), False)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD115-51731-201920.csv'
        unwanted = [r'.\D2l Data\TC\Spring 19']
        self.assertEqual(getFiles.check_file_name(fileName,unwanted), False)
        
        
if __name__  == "__main__":
    unittest.main()
