class Node:
  """! 
    The Node
    
    This class implements a linked node that store an object and a link to the next node

    @type data: object
    @param data: The attribute that stores an object

    @type next: Node
    @param next: The attribute that points to the next node. It is None if there is no next node.
  """

  def __init__(self, data = None,next = None):
    """!
      Node initializer

      This initializer should initialize the node's data and next to None
    """
    self._data = data
    self._next = next