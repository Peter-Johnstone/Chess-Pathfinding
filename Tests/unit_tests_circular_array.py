import unittest
from DS.CircularArray import CircularArray

class TestCircularArray(unittest.TestCase):
    def testInit(self):
        # Test 1
        a = CircularArray()
        self.assertEqual(a._cap, 2)
        self.assertEqual(a._data, [None, None])
        # Test 2
        b = CircularArray(3)
        self.assertEqual(b._cap, 3)
        self.assertEqual(b._data, [None, None, None])
        # Test 3
        c = CircularArray(100)
        self.assertEqual(c._cap, 100)
        self.assertEqual(c._data, [None] * 100)
        
    def testLen(self):
        # Test 1
        a = CircularArray()
        self.assertEqual(len(a), 2)
        # Test 2
        b = CircularArray(3)
        self.assertEqual(len(b), 3)
        # Test 3
        c = CircularArray(100)
        self.assertEqual(len(c), 100)
        
    def testGetItem(self):
        # Test 1
        a = CircularArray()
        a._data[0] = 'a'
        self.assertEqual(a[0], 'a')
        self.assertEqual(a[2], 'a')
        self.assertEqual(a[-2], 'a')
        # Test 2
        b = CircularArray(3)
        b._data[2] = [None]
        self.assertEqual(b[2], [None])
        self.assertEqual(b[5], [None])
        self.assertEqual(b[-1], [None])
        # Test 3
        c = CircularArray(100)
        c._data[56] = [None]
        self.assertEqual(c[56], [None])
        self.assertEqual(c[156], [None])
        self.assertEqual(c[-44], [None])
            
    def testSetItem(self):
        # Test 1
        a = CircularArray()
        a[0] = 'a'
        self.assertEqual(a._data[0], 'a')
        a[2] = 'b'
        self.assertEqual(a._data[0], 'b')
        a[-2] = 'c'
        self.assertEqual(a._data[0], 'c')
        # Test 2
        b = CircularArray(3)
        b[2] = [None]
        self.assertEqual(b._data[2], [None])
        b[5] = ['abc']
        self.assertEqual(b._data[2], ['abc'])
        b[-1] = ['def']
        self.assertEqual(b._data[2], ['def'])
        # Test 3
        c = CircularArray(100)
        c[56] = [None]
        self.assertEqual(c._data[56], [None])
        c[156] = ['abc']
        self.assertEqual(c._data[56], ['abc'])
        c[-44] = ['def']
        self.assertEqual(c._data[56], ['def'])
    
    def testStr(self):
        # Test 1
        a = CircularArray()
        a[0] = 'a'
        self.assertEqual(str(a), '[a, None]')
        # Test 2
        b = CircularArray(3)
        b[2] = [None]
        self.assertEqual(str(b), '[None, None, [None]]')
        # Test 3
        c = CircularArray(100)
        c[56] = [None]
        self.assertIn('[None]', str(c))
    
if __name__ == '__main__':
    unittest.main()
    
# Run this test file (at the root project directory) with the command:
#   python -m unittest Tests.unit_tests_circular_array