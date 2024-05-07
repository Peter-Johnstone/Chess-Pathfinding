import unittest
from DS.Array import Array

class TestArray(unittest.TestCase):
    def testInit(self):
        # Test 1
        a = Array()
        self.assertEqual(a._cap, 2)
        self.assertEqual(a._data, [None, None])
        # Test 2
        b = Array(3)
        self.assertEqual(b._cap, 3)
        self.assertEqual(b._data, [None, None, None])
        # Test 3
        c = Array(100)
        self.assertEqual(c._cap, 100)
        self.assertEqual(c._data, [None] * 100)
        
    def testLen(self):
        # Test 1
        a = Array()
        self.assertEqual(len(a), 2)
        # Test 2
        b = Array(3)
        self.assertEqual(len(b), 3)
        # Test 3
        c = Array(100)
        self.assertEqual(len(c), 100)
        
    def testGetItem(self):
        # Test 1
        a = Array()
        a._data[0] = 'a'
        self.assertEqual(a[0], 'a')
        with self.assertRaises(IndexError):
            a[-1]
        with self.assertRaises(IndexError):
            a[2]
        # Test 2
        b = Array(3)
        b._data[2] = [None]
        self.assertEqual(b[2], [None])
        with self.assertRaises(IndexError):
            b[-1]
        with self.assertRaises(IndexError):
            b[3]
        # Test 3
        c = Array(100)
        c._data[56] = [None]
        self.assertEqual(c[56], [None])
        with self.assertRaises(IndexError):
            c[-1]
        with self.assertRaises(IndexError):
            c[100]
            
    def testSetItem(self):
        # Test 1
        a = Array()
        a[0] = 'a'
        self.assertEqual(a._data[0], 'a')
        with self.assertRaises(IndexError):
            a[-1] = 'a'
        with self.assertRaises(IndexError):
            a[2] = 'a'
        # Test 2
        b = Array(3)
        b[2] = [None]
        self.assertEqual(b._data[2], [None])
        with self.assertRaises(IndexError):
            b[-1] = 'a'
        with self.assertRaises(IndexError):
            b[3] = 'a'
        # Test 3
        c = Array(100)
        c[56] = [None]
        self.assertEqual(c._data[56], [None])
        with self.assertRaises(IndexError):
            c[-1] = 'test'
        with self.assertRaises(IndexError):
            c[100] = 'test'
    
    def testStr(self):
        # Test 1
        a = Array()
        a[0] = 'a'
        self.assertEqual(str(a), '[a, None]')
        # Test 2
        b = Array(3)
        b[2] = [None]
        self.assertEqual(str(b), '[None, None, [None]]')
        # Test 3
        c = Array(100)
        c[56] = [None]
        self.assertIn('[None]', str(c))
    
if __name__ == '__main__':
    unittest.main()
    
# Run this test file (at the root project directory) with the command:
#   python -m unittest Tests.unit_tests_array