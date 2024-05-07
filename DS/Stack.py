from DS.Array import Array
from DS.Node import *


class Stack:
  """! 
    The Stack
    
    This class implements a stack using Array to store a sequence of objects with LIFO access

    @type _array: Array
    @param _array: The attribute that stores objects in an array

    @type size: int
    @param size: The total number of objects stored in the stack
  """

  def __init__(self):
    self._head = None
    self._size = 0

  def __len__(self):
    return self._size

  def push(self, obj):
    new_node = Node(obj, self._head)
    self._head = new_node
    self._size += 1
    pass

  def pop(self):
    if self._size == 0:
      return None
    top = self._head
    self._head = self._head._next
    self._size -= 1
    return top._data

  def top(self):
    if self._size == 0:
      return None
    return self._head._data