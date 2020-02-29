import unittest
<<<<<<< HEAD


from source.getFiles import check_file


=======
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from source.getFiles import check_file

>>>>>>> d78d6fb027db8b821ec35d338b673811fb398a15

class test_getFiles(unittest.TestCase):
    def test_checkFiles(self):
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160411_ELTE274-52356-201920.csv'
<<<<<<< HEAD
        self.assertEqual(check_file(fileName),True)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD125-51373-201920_Test195'
        self.assertEqual(check_file(fileName),False)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD115-51731-201920.csv'
        self.assertEqual(check_file(fileName),False)
        
        fileName = r'.\D2l Data\A&S\CTL\Archived\Spring 17\AllGradesExport_AAST290-82669-201720.csv'
        self.assertEqual(check_file(fileName),True)
        
        fileName = r'.\D2l Data\A&S\AAST\Spring 19\AllGradesWithWithdrawnStudents_20190509_182624_AAST290-51671-201920_Test406.csv'
        self.assertEqual(check_file(fileName),False)
        
        
        
=======
        self.assertEqual(check_File(fileName),True)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD125-51373-201920_Test195'
        self.assertEqual(check_File(fileName),False)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD115-51731-201920.csv'
        self.assertEqual(check_File(fileName),False)
        
        fileName = r'.\D2l Data\A&S\CTL\Archived\Spring 17\AllGradesExport_AAST290-82669-201720.csv'
        self.assertEqual(check_File(fileName),True)
        
        fileName = r'.\D2l Data\A&S\AAST\Spring 19\AllGradesWithWithdrawnStudents_20190509_182624_AAST290-51671-201920_Test406.csv'
        self.assertEqual(check_File(fileName),False)
>>>>>>> d78d6fb027db8b821ec35d338b673811fb398a15
        
        
if __name__  == "__main__":
    unittest.main()
