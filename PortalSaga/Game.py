""" Game to play 'The Portal Saga'. This is the file you edit.
To make more ppm files, open a gif or jpg in xv and save as ppm raw.
"""
from GUI.gameboard import GameBoard
from GUI.graphics import Point
from PortalSaga.Config import Config
from DS.Array import * #ADT 2: enemy pawn array
from DS.Stack import * #ADT 3: stack of maps
import random

stack = Stack() #The stack of the enemy location Array is initialized
class Game:

  def __init__(self, inventory = 0, isQueen = False, comingFromFuture = -1):
    #Initializes the Game/Room
    global stack
    if comingFromFuture != -1 and len(stack) >= comingFromFuture + 1:
      #This checks if the room was entered via portal or via button
      for i in range(comingFromFuture):
        stack.pop()  
      self.enemyList = stack.top()
    else:
      self.enemyList = self.generateEnemies()
      stack.push(self.enemyList)
    self.portalList = self.generatePortals()
    #Generates the list of portals
    global protagonistPiece
    #The protagonistPiece is the name for the user's piece.
    if not isQueen:
      #Checks if the user's piece is a queen yet, if not, it becomes a pawn
      from PortalSaga.Pawn import Pawn
      protagonistPiece = Pawn(self.enemyList, self.portalList, inventory)
    else:
      #If it the isQueen boolean passed to it is True, the queen is generated
      from PortalSaga.Queen import Queen
      protagonistPiece = Queen(self.enemyList, self.portalList, inventory, Point(3,7))

    
    global _gui 
    #Initializes the GUI
    _gui = GameBoard("Chess Adventure", self, protagonistPiece, Config.SIZE)

  def startGame(self):
    #Runs the GUI
    _gui.run()

  def returnProtagonistPiece(self):
    #Allows gameboard.py to access information about the protagonistpiece
    #for example, gameboard.py might want to access the user's inventory.
    global protagonistPiece
    return protagonistPiece

  def returnEnemies(self):
    #Returns the enemy list for gameboard.py to access.
    #Allows for access of enemy indexes for image display.
    return self.enemyList
  
  def generateEnemies(self): 
    """    
    THE GENERATION OF THIS ARRAY IS WHAT I WILL BE DOING BIG O ANALYSIS ON
    """
    # Generates an array of some number of enemies coordinates
    numEnemies = random.randint(10,20)                               #O(1)
    self.enemyList = Array(2)                                        #O(1)
    
    vars = random.sample(range(0,40), numEnemies)                    #O(N) assuming numEnemies is N
    for i, var in enumerate(vars):                                   #O(N) also N
      enemyXCoord = var % 8                                          #O(1)
      enemyYCoord = (var // 8) + 1                                   #O(1)
      self.enemyList.__setitem__(i, [enemyXCoord,enemyYCoord])       #O(1)
    return self.enemyList                                            #O(N) total runtime

  def generatePortals(self):
    # Generates an array of portals on the top row
    self.portalList = Array(8)
    for i in range(0,8):
      self.portalList.__setitem__(i, [i, 0])
    return self.portalList

  def checkForEnemies(point, enemyList):
    # Returns true if the enemy is on the point, otherwise returns false
    return enemyList.search(point)

  def checkAndDelete(point, enemyList):
    # Checks for enemy, and then removes them from board if present
    enemyIndex = enemyList.search2(point)
    if enemyIndex == -1:
      return False
    if enemyIndex != None:
      _gui.erase(enemyIndex)
      enemyList[enemyIndex] = None
      return enemyList

  def getStack(self):
    return stack

  def getGreenCircleImage(self):
    #Returns the image path for the green circle seen in the help button
    return Config.IMAGEPATH + 'greencircle.png'
  
  def getPawnImage(self):
    # Returns the image path for the white pawn
    return Config.IMAGEPATH + 'whitepawn.png'

  def getQueenImage(self):
    # Returns the image path for the white queen
    return Config.IMAGEPATH + 'whitequeen.png'
    
  def getEnemyPawnImage(self):
    # Returns the image path for the black pawn
    return Config.IMAGEPATH + 'blackpawn.png'

  def getPortalImage(self):
    # Returns the image path for the portal
    return Config.IMAGEPATH + 'portal.png'

  def getBoardImage(self):
    # Returns the image path for the background
    return Config.IMAGEPATH + "board.png"
    
  def inBounds(value):
    # Checks if the coordinate is on the grid, returns bool
    if 0 <= value <= 7:
      return True
    return False


  
  def goThroughPortal(enemyList, inventory, isQueen = False, comingFromFuture = -1):
    #Trigger a new enemy list generation
    if isQueen:
      if comingFromFuture != -1: 
        nextRoom = Game(inventory, True, comingFromFuture)
      else:
        nextRoom = Game(inventory, True)
    else: 
      nextRoom = Game(inventory)
    nextRoom.startGame()

  def runUpgrades(enemyList, protalList, inventory, position):
    #This function sets the protagonist piece as a queen.
    #This function is called once the first objective has been met
    from PortalSaga.Queen import Queen
    global protagonistPiece
    protagonistPiece = Queen(enemyList, protalList, inventory, position)

