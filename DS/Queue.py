from DS.CircularArray import CircularArray
from DS.Node import *
    
class Queue:
  """! 
    The Queue
    
    This class implements a queue using CircularArray to store a sequence of objects with FIFO access

    @type _array: CircularArray
    @param _array: The attribute that stores objects in a circular array

    @type size: int
    @param size: The total number of objects stored in the queue
  """

  def __init__(self):
    """!
      Queue initializer

      This initializer should initialize the _array and set the _size to zero
    """
    self._front = None
    self._back = None
    self._size = 0

  def __len__(self):
    """!
      Queue class length method

      @rtype: int
      @return: Returns a total number of objects stroed in the queue
    """
    return self._size

  def enqueue(self, obj):
    """!
      Queue class enqueue
      
      Enqueue a new object (the input obj) to the back of the queue

      @type obj: object
      @param obj: an input object
    """
    newNode = Node(obj)
    if self._size == 0:
      self._back = newNode
      self._front = newNode
    else:
      self._back._next = newNode
      self._back = self._back._next
    self._size += 1

  def dequeue(self):
    """!
      Queue class dequeue
      
      Dequeue and return the object at the front of the queue

      @rtype: object
      @return: Returns the object that was stored at the front of the queue
    """
    if self._size == 0:
      return None
    temp = self._front._data
    self._front = self._front._next
    self._size -= 1
    return temp

  def first(self):
    """!
      Queue class first
      
      Return the object stored at the front of the queue

      @rtype: object
      @return: Returns the object stored at the front of the queue
    """
    if self._size == 0:
      return None
    return self._front._data
