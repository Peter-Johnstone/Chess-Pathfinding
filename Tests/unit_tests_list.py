import unittest
from DS.List import LinkedList

class TestList(unittest.TestCase):
    def testInit(self):
        listy = LinkedList()
        listy.insert("dog")
        self.assertTrue(listy.__str__()=="[dog]")
        
    def testLen(self):
        listy = LinkedList()
        listy.insert("dog")
        listy.insert("weirdFish")
        listy.insert("cat")
        self.assertTrue(listy.__len__() == 3)
        
    def testInsert(self):
        listy = LinkedList()
        listy.insert("dog")
        self.assertTrue(listy.__str__()=="[dog]")
        
    def testDelete(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        self.assertTrue(False)
        
    def testPeek(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        self.assertTrue(False)
        
    # add more test functions for other methods you have added (except simple gettter and setters methods)
    
if __name__ == '__main__':
    unittest.main()
    
# Run this test file (at the root project directory) with the command:
#   python -m unittest Tests.unit_tests_list