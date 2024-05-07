class CircularArray:
  """! 
    The CircularArray

    This class implements a circular array

    @type _data: list
    @param _data: The attribute that stores the data

    @type _cap: int
    @param _cap: The lenght of the array, i.e. its capacity
  """

  def __init__(self, capacity=2):
    """!
      CircularArray initializer

      This initializer should initialize the circular array's data with the input capacity

      @type capacity: int
      @param capacity: the capacity of the array
    """
    if capacity <= 0:
      raise ValueError
    self._data = [None] * capacity
    self._cap = capacity

  def __len__(self):
    """!
      CircularArray length function

      This returns the length of the array, i.e. the capacity of the array

      @rtype: int
      @return: Returns the array capacity
    """
    return self._cap

  def __getitem__(self, index):
    """!
      CircularArray [index] operator (getter)

      This returns the object in the array stored at index modolus the array size

      @rtype: object
      @return: Returns the object stored at index modolus the array size
    """
    return self._data[index % self._cap]

  def __setitem__(self, index, value):
    """!
      CircularArray [index] operator (setter)

      This stores the object to the array at index modolus the array size

      @type index: int
      @param index: the target index

      @type value: object
      @param value: the object to store
    """
    self._data[index % self._cap] = value

  def __str__(self):
    """!
      CircularArray str function

      This returns a string representation of the array

      @rtype: str
      @return: Returns a serialized string that describes the array
    """
    s = '['
    for i in range(self._cap):
      s += str(self[i]) + ", "
    return s.rstrip().rstrip(',') + ']'