import unittest
from DS.Node import Node

class TestNode(unittest.TestCase):
    def testInit(self):
        # Test 1
        node = Node('a')
        self.assertEqual(type(node.data), type('a'))
        self.assertEqual(node.data, 'a')
        self.assertEqual(node.next, None)
        # Test 2
        node = Node(2)
        self.assertEqual(type(node.data), type(2))
        self.assertEqual(node.data, 2)
        self.assertEqual(node.next, None)
        # Test 3
        node = Node(['abc', 'def'])
        self.assertEqual(type(node.data), type([]))
        self.assertEqual(node.data, ['abc', 'def'])
        self.assertEqual(node.next, None)
    
if __name__ == '__main__':
    unittest.main()
    
# Run this test file (at the root project directory) with the command:
#   python -m unittest Tests.unit_tests_node
