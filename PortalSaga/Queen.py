from PortalSaga.Game import *
from GUI.graphics import Point
from PortalSaga.Game import Game
import random

class Queen():

  def __init__(self, enemyList, portalList, inventory, location):
    self.enemyList = enemyList
    self.portalList = portalList
    self._inventory = inventory    

    # Initializes Queen's starting Location
    self._queenLocation = location

  def getQueenLocation(self):
  # Returns the location of the white queen
    return self._queenLocation

  def goUp(self, distance = 1): #Logic encoding the queen's UP movement
  #I will comment this method thoroughly
  #but not so much for the other movement methods.
    temp_location = self._queenLocation.clone()
    #Stores a temp location of the queen's current position
    #This location will be used to test the positions along the queens
    #hypotheical movement path
    for i in range(distance):
      if temp_location.y - 1 == 0:
        Game.goThroughPortal(self.enemyList, self._inventory, True)
        #Checks to see if there are any enemies within the range
        #of movement. If there are any enemies, the queen
        #sees an obsical and the move is canceled.
        return
      if Game.inBounds(temp_location.y - 1):
        if Game.checkForEnemies([temp_location.x, temp_location.y-1], self.enemyList):
          if i == distance-1:
            #This line checks if there are any enemies exactly where the
            #Queen lands, making the capture a legal move.
            temp_location.y -= 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            #This will run checkAndDelete() which checks to make sure there
            #Is an enemy on the tile, and if so, will undraw it and remove
            #it from the array
            self._inventory += 1
            #Increases the inventory size, can be seen in the GUI
          return
        else:
          temp_location.y -= 1
      else:
        #This return statement will run if any of the temp
        #positions are out of the board's bounds.
        return
    self._queenLocation = temp_location.clone()
    

  def goDown(self, distance=1): #Logic encoding the queen's DOWN movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if Game.inBounds(temp_location.y + 1):
        if Game.checkForEnemies([temp_location.x, temp_location.y+1], self.enemyList):
          if i == distance-1:
            temp_location.y += 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.y += 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goLeft(self, distance=1): #Logic encoding the queen's LEFT movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if Game.inBounds(temp_location.x - 1):
        if Game.checkForEnemies([temp_location.x - 1, temp_location.y], self.enemyList):
          if i == distance-1:
            temp_location.x -= 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.x -= 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goRight(self, distance=1): #Logic encoding the queen's RIGHT movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if Game.inBounds(temp_location.x + 1):
        if Game.checkForEnemies([temp_location.x + 1, temp_location.y], self.enemyList):
          if i == distance-1:
            temp_location.x += 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.x += 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goUpLeft(self, distance=1): #Logic for the queen's UPLEFT movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if temp_location.y - 1 == 0:
        Game.goThroughPortal(self.enemyList, self._inventory, True)
        return
      if Game.inBounds(temp_location.y - 1) and Game.inBounds(temp_location.x - 1):
        if Game.checkForEnemies([temp_location.x-1, temp_location.y-1], self.enemyList):
          if i == distance-1:
            temp_location.y -= 1
            temp_location.x -= 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.y -= 1
          temp_location.x -= 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goUpRight(self, distance): #Logic for the queen's UPRIGHT movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if temp_location.y - 1 == 0:
        Game.goThroughPortal(self.enemyList, self._inventory, True)
        return
      if Game.inBounds(temp_location.y - 1) and Game.inBounds(temp_location.x + 1):
        if Game.checkForEnemies([temp_location.x+1, temp_location.y-1], self.enemyList):
          if i == distance-1:
            temp_location.y -= 1
            temp_location.x += 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.y -= 1
          temp_location.x += 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goDownLeft(self, distance=1): #Logic for the queen's DOWNLEFT movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if Game.inBounds(temp_location.y + 1) and Game.inBounds(temp_location.x - 1):
        if Game.checkForEnemies([temp_location.x-1, temp_location.y+1], self.enemyList):
          if i == distance-1:
            temp_location.y += 1
            temp_location.x -= 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.y += 1
          temp_location.x -= 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goDownRight(self, distance=1): #Logic for the queen's DOWNRIGHT movement
    temp_location = self._queenLocation.clone()
    for i in range(distance):
      if Game.inBounds(temp_location.y + 1) and Game.inBounds(temp_location.x + 1):
        if Game.checkForEnemies([temp_location.x+1, temp_location.y+1], self.enemyList):
          if i == distance-1:
            temp_location.y += 1
            temp_location.x += 1
            self._queenLocation = temp_location.clone()
            self.enemyList = Game.checkAndDelete([temp_location.x, temp_location.y], self.enemyList)
            self._inventory += 1
          return
        else:
          temp_location.y += 1
          temp_location.x += 1
      else:
        return
    self._queenLocation = temp_location.clone()

  def goBack(self, numLevels):
    #This function is used to tell Game.py that the Queen has hit
    #the "Back" button. This will then pop the stack a corresponding number of times
    Game.goThroughPortal(self.enemyList, self._inventory, True, numLevels)
  
  def getInventory(self):
    #Called by GUI when inventory updates.
    #Returns entire inventory (as a string). 
    return f"{self._inventory} Pawns"
    

  def getInventoryInt(self):
    #Same as getInventory(), but returns an int instead.
    return self._inventory