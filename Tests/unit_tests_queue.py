import unittest
from DS.Queue import *
from DS.Node import *

class TestQueue(unittest.TestCase):
  def test_queue(self):
    queue = Queue()
    self.assertTrue(queue._size == 0) 
  def test_enqueue_empty(self):
    queue = Queue()
    queue.enqueue("Jonathan Smells")
    return queue._size == 1 and queue.first() == "Jonathan Smells"
  def test_enqueue_filled(self):
    queue = Queue()
    queue.enqueue("Jonathan Smells really bad")
    queue.enqueue("Jonathan Smells")
    self.assertTrue(queue._size == 2 and queue.first() == "Jonathan Smells really bad")
  def test_peek_empty(self):
    queue = Queue()
    self.assertTrue(queue._size == 0 and queue.first() == None)
  def test_peek_filled(self):
    queue = Queue()
    queue.enqueue("testing")
    queue.enqueue("testing again")
    self.assertTrue(queue._size == 2 and queue.first() == "testing")
  def test_dequeue_empty(self):
    queue = Queue()
    self.assertTrue(queue.dequeue() == None)
  def test_dequeue_full(self):
    queue = Queue()
    queue.enqueue("testing")
    queue.enqueue("testing again")
    queue.dequeue()
    print(queue._size == 1 and queue.first() == "testing again")
    self.assertTrue(queue._size == 1 and queue.first() == "testing again")
  def test_length_empty(self):
    queue = Queue()
    self.assertTrue(len(queue) == 0)
  def test_length_filled(self):
    queue = Queue()
    queue.enqueue("testing")
    self.assertTrue(len(queue) == 1)
  def test_emptiness_when_empty(self):
    queue = Queue()
    self.assertTrue(queue._size == 0)
  def test_emptiness_when_full(self):
    queue = Queue()
    queue.enqueue("testing")
    self.assertTrue(queue._size != 0)
    
if __name__ == '__main__':
    unittest.main()
    
# Run this test file (at the root project directory) with the command:
#   python -m unittest Tests.unit_tests_queue