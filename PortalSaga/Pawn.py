from PortalSaga.Game import *
from GUI.graphics import Point
from PortalSaga.Game import Game
from DS.Array import *
import copy
import random


class Pawn():

  def __init__(self, enemyList, portalList, inventory):
    self.enemyList = enemyList
    self.portalList = portalList
    self._inventory = inventory

    # Initializes Pawn's starting Location
    self._pawnLocation = Point(self.returnClearXPath(), 6)

  def checkColumn(self, col, row, path=[]):
    a = self.enemyList.search([col - 1, row - 1])
    b = self.enemyList.search([col, row - 1])
    c = self.enemyList.search([col + 1, row - 1])
    # Add the current position to the path
    path.append([col, row])
    if row == 0:  # base case 1 (a solution)
      return True, path
    if a:  # if left can be captured, check it first, recursive case 1
      result, path = self.checkColumn(col - 1, row - 1, path)
      if result: return True, path
    if c:  # if right can also be captured, check it also, recursive case 2
      result, path = self.checkColumn(col + 1, row - 1, path)
      if result: return True, path
    if not b:  # if middle is an empty space, we can advance one step, recursive case 3
      result, path = self.checkColumn(col, row - 1, path)
      if result: return True, path
    # if none of the above, base case 2 (not a solution)
    path.pop()
    return False, path

  def getStack():
    return stack

  def returnClearXPath(self):
    # Recursively checks paths to find one that's solvable
    randomizedColumns = random.sample(range(0, 8), 8)
    xCoord = randomizedColumns.pop()
    isSolvable, notApplicable = self.checkColumn(xCoord, 6)
    while not isSolvable:
      xCoord = randomizedColumns.pop()
      isSolvable, notApplicable = self.checkColumn(xCoord, 6)
    return xCoord

  def getPawnLocation(self):
    # Returns the location of the white pawn
    return self._pawnLocation

  def doubleJump(self):
    # Does a double jump if conditions cleared
    if self._pawnLocation.y == 6:
      if not Game.checkForEnemies([
          self._pawnLocation.x, self._pawnLocation.y - 1
      ], self.enemyList) and not Game.checkForEnemies(
          [self._pawnLocation.x, self._pawnLocation.y - 2], self.enemyList):
        self._pawnLocation.y -= 2

  def goUp(self):
    # Moves pawn one square up, if possible
    if self._pawnLocation.y - 1 == 0:
      Game.goThroughPortal(self.enemyList, self._inventory)
    if Game.inBounds(self._pawnLocation.y - 1):
      if not Game.checkForEnemies(
          [self._pawnLocation.x, self._pawnLocation.y - 1], self.enemyList):
        self._pawnLocation.y -= 1

  def goDown(self):
    # Illegal move if pawn, used for testing.
    return
    if Game.inBounds(self._pawnLocation.y + 1):
      self._pawnLocation.y += 1

  def goLeft(self):
    # Illegal move if pawn, used for testing.
    return
    if Game.inBounds(self._pawnLocation.x - 1):
      self._pawnLocation.x -= 1

  def goRight(self):
    # Illegal move if pawn, used for testing.
    return
    if Game.inBounds(self._pawnLocation.x + 1):
      self._pawnLocation.x += 1

  def capturePieceLeft(self):
    """ Called by GUI when button clicked. 
    If rover is standing on a part (not a portal 
    or ship component), pick it up and add it
    to the inventory. """
    tempVar = Game.checkAndDelete(
        [self._pawnLocation.x - 1, self._pawnLocation.y - 1], self.enemyList)
    if tempVar:
      self.enemyList = tempVar
      self._inventory += 1
      if Game.inBounds(self._pawnLocation.x -
                       1) and Game.inBounds(self._pawnLocation.y - 1):
        self._pawnLocation.x -= 1
        self._pawnLocation.y -= 1
    if self._inventory == 9:  #set this to 9 in final version
      Game.runUpgrades(self.enemyList, self.portalList, self._inventory,
                       self._pawnLocation)

  def capturePieceRight(self):
    """ Called by GUI when button clicked. 
    If rover is standing on a part (not a portal 
    or ship component), pick it up and add it
    to the inventory. """
    tempVar = Game.checkAndDelete(
        [self._pawnLocation.x + 1, self._pawnLocation.y - 1], self.enemyList)
    if tempVar:
      self.enemyList = tempVar
      self._inventory += 1
      if Game.inBounds(self._pawnLocation.x +
                       1) and Game.inBounds(self._pawnLocation.y - 1):
        self._pawnLocation.x += 1
        self._pawnLocation.y -= 1
    if self._inventory == 9:  #set this to 9 in final version
      Game.runUpgrades(self.enemyList, self.portalList, self._inventory,
                       self._pawnLocation)

  def getInventory(self):
    #Called by GUI when inventory updates.
    #Returns entire inventory (as a string).

    if self._inventory == 1:
      return "1 Pawn"
    return f"{self._inventory} Pawns"

  def getInventoryInt(self):
    #Returns the inventory as an int.
    return self._inventory
