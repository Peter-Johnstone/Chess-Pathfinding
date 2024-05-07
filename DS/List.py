from logging import exception
from DS.Node import Node
    
class LinkedList:
  """! 
    The LinkedList
    
    This class implements a list using Node to store a sequence of objects

    @type _head: Node
    @param _head: The attribute that stores the first node. It is None if no first node.

    @type _tail: Node
    @param _tail: The attribute that stores the last node. It is None if no last node.

    @type _size: int
    @param _size: The total number of objects stored in the list
  """

  def __init__(self):
    """!
      LinkedList initializer

      This initializer should initialize the _head and _tail nodes to None and set the _size to zero
    """
    self._head = None
    self._tail = None
    self._size = 0


  def __len__(self):
    """!
      LinkedList class length method

      @rtype: int
      @return: Returns a total number of objects/nodes stroed in the list
    """
    return self._size

  def insert(self, obj, idx = 0):
    tempNode = Node(obj)
    self._size+=1
    if self._size == 1: #if empty list
       self._head = tempNode
       self._tail = self._head
    else:#navigates to correct start position in LL
      key = self._head
      for i in range(0, idx):
        key = key._next
      tempNode._next = key._next
      key._next = tempNode
      if idx==0:
        self._head = tempNode
      if idx == self._size:
        self._tail = tempNode


  def delete(self, idx=0):
    key = self._head
    if idx==0:
      self._head = key._next
      return
    for i in range(0, idx-1):
      key = key._next
    if idx != self._size:
      key.next = key._next._next
    else:
      key.next = None
    print("All deleted :D")
    pass

  def peek(self, idx):
    """!
      LinkedList class peek
      
      Return the object stored in the node at the input idx

      @type idx: int
      @param idx: the position in the list where the object should return

      @rtype: object
      @return: Returns the stored in the node at the specified index
    """
    return self._tail
    
  def __str__(self):
    s = "[" + str(self._head._data) + ", "
    key = self._head
    for i in range(0, self._size-1):
      key = key._next
      s += str(key._data) + ", "
    return s.strip(", ") + "]"
