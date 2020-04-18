import unittest
import system as system

class test_system(unittest.TestCase):
    def test_get_last(self):
        name = "Joe Smith"
        self.assertEqual(system.get_last(name), "Smith")
        name = "John Doe"
        self.assertEqual(system.get_last(name), "Doe")
        name = "Jim"
        self.assertEqual(system.get_last(name), "Jim")
        name = "Bob John Joe"
        self.assertEqual(system.get_last(name), "Joe")
        name = "This is a test"
        self.assertEqual(system.get_last(name), "test")
        
    
if __name__  == "__main__":
    unittest.main()