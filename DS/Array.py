class Array:
  """! 
    The Array

    This class implements an array

    @type _data: list
    @param _data: The attribute that stores the data

    @type _cap: int
    @param _cap: The lenght of the array, i.e. its capacity
  """

  def __init__(self, capacity=2):
    if capacity <= 0:
      raise ValueError
    self._data = [None] * capacity
    self._cap = capacity
    self._size = 0

  def __len__(self):
    return self._cap

  def __getitem__(self, index):
    """!
      Array [index] operator (getter)

      This returns the object in the array stored at index
      IndexError is rasied if index is out of bound

      @rtype: object
      @return: Returns the object stored at index
    """
    if index < 0 or index >= self._cap:
        raise IndexError
    return self._data[index]

  def __setitem__(self, index, value):
    if index < 0 or index >= self._cap:
      tempArr = [None]*(self._cap * 2)  
      self._cap = self._cap *2
      for a in range(self._size):
        tempArr[a] = self._data[a]
      self._data = tempArr
    self._data[index] = value
    self._size +=1

  def __str__(self):
    s = '['
    for i in range(self._cap):
      s += str(self[i]) + ", "
    return s.rstrip().rstrip(',') + ']'

  def search(self, target):
    for a in self._data:
      if a:
      # :D
        if a == target:
            return True
    return False

  def search2(self, target):
    for index, a in enumerate(self._data):
      if a:
        if a == target:
            return index
    return -1