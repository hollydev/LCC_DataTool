import unittest
import os

class checkFiles():
# returns True if the file is not a duplicate or empty.
    def checkFile(fileName):
        ret = False
        if ('test' not in fileName.lower()) and (os.path.getsize(fileName) > 460):
            ret = True
    
        return ret

    # returns a list of all good files.
    def getFiles(myPath):
        
        files = []
        
        for root, dirs, f in os.walk(myPath):
            for file in f:
                if '.csv' in file:
                    fileName = os.path.join(root, file)
                    
                    if checkFile(fileName) == True:
                        files.append(fileName)
        return files 

class test_getFiles(unittest.TestCase):
    def test_checkFiles(self):
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160411_ELTE274-52356-201920.csv'
        self.assertEqual(checkFile(fileName),True)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD125-51373-201920_Test195'
        self.assertEqual(checkFile(fileName),False)
        
        fileName = r'.\D2l Data\TC\Spring 19\AllGradesWithWithdrawnStudents_20190509_160155_WELD115-51731-201920.csv'
        self.assertEqual(checkFile(fileName),False)
        
        fileName = r'.\D2l Data\A&S\CTL\Archived\Spring 17\AllGradesExport_AAST290-82669-201720.csv'
        self.assertEqual(checkFile(fileName),True)
        
        fileName = r'.\D2l Data\A&S\AAST\Spring 19\AllGradesWithWithdrawnStudents_20190509_182624_AAST290-51671-201920_Test406.csv'
        self.assertEqual(checkFile(fileName),False)
        
        
if __name__  == "__main__":
    unittest.main()
