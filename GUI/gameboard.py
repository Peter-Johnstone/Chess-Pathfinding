""" A square gameboard that draws colored tiles. Includes text fields for
a task and inventory. Includes buttons to play the game.

Uses the graphics class that John Zelle wrote to use with
"Python Programming: An Introduction to Computer Science" (Franklin,
Beedle & Associates). Uses the GraphWin, Rectangle, and Text classes. Adds
in a Button class.

Students do not have to edit this file.

-----------------------------------------------------------------------
COPYRIGHT: Lea Wittie 2012

LICENSE: This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    This is open-source software released under the terms of the
    GPL (http://www.gnu.org/licenses/gpl.html). 

PLATFORMS: The package requires Tkinter and should run on
any platform where Tkinter is available.

INSTALLATION: Put this file somewhere where Python can see it. Also get a
copy of graphics.py as mentioned above.
"""
from GUI.graphics import *
from functools import partial
from DS.Queue import * #ADT 1: Queue of portal images
import time
isQueen = False
class GameBoard:
    """ A game board of size X size squares with fields for tasks and inventory,
        and many buttons. """

    # draw the board
    def __init__(self, title, game, protagonistPiece, size, bkColor= 'lavender', buttonColor = 'lightpink'):

        
      

        global isQueen
        #This global variable helps with the board construction.
        #This is set after a check from the data type of
        #Game.returnProtagonist() peice.
        width = 650
        height = 600
        self.size = size
        self.protagonistPiece = protagonistPiece
        self.game = game 
        self.window = GraphWin(title, width, height)
        self.window.setBackground(bkColor)

        sideOffset = 10  # offset from sides
        lineSpace = 25   # vertical offset between lines
        boxOffset = 5    # offset from side of box
        taskHeight = 100 # height of task window where tasks are listed
        taskWidth = 400
        self.mapSize = (400//self.size)*self.size  # height of map window where map is seen
        invHeight = 300 # height of inv window where inventory is listed
        invWidth = 200
        buttonWidth = 200 # width of the button space
        self.lineSpace = lineSpace
        self.buttonWidth, self.buttonColor = buttonWidth, buttonColor
        
        # This is all formatting for the task window
        taskX = sideOffset
        taskY = sideOffset
        taskLabel = Text(Point(taskX, taskY), "Objective")
        taskLabel.setStyle('bold')
        taskLabel.draw(self.window)
        taskRect = Rectangle(Point(taskX, taskY + lineSpace), Point(taskX + taskWidth, taskY + lineSpace + taskHeight))
        taskRect.setFill("white")
        taskRect.draw(self.window)
        if not isQueen:
          #If not a queen, the initial task is the 9 pawns task
          self.taskWin = Text(Point(taskX + boxOffset, taskY + lineSpace + boxOffset), "Collect 9 pawns")
        elif self.protagonistPiece.getInventoryInt() >= 9 and 29 > self.protagonistPiece.getInventoryInt():
          #If the second task has not been completed, then it is displayed
          self.taskWin = Text(Point(taskX + boxOffset, taskY + lineSpace + boxOffset), "Collect 20 more pawns")
        else:
          #Else the final task is displayed
          self.taskWin = Text(Point(taskX + boxOffset, taskY + lineSpace + boxOffset), "Go back to World 1 to win the game!")
        self.taskWin.draw(self.window)
        

        # bottom left is Room Map
        mapX = sideOffset
        mapY = sideOffset + lineSpace + taskHeight + lineSpace
        self.mapRectX = mapX
        self.mapRectY = mapY + lineSpace
        worldNum = len(game.getStack())
        s = "World #"+ str(worldNum)
        mapLabel = Text(Point(mapX, mapY), s)
        mapLabel.setStyle('bold')
        mapLabel.draw(self.window)
        self.mapRect = Rectangle(Point(mapX, mapY + lineSpace),
                            Point(mapX + self.mapSize,
                                  mapY + lineSpace + self.mapSize))
        self.mapRect.setFill("white")
        self.mapRect.draw(self.window)
        # top right is Inventory
        invX = width - sideOffset - invWidth
        invY = sideOffset
        invLabel = Text(Point(invX, invY), "Captured Pieces")
        invLabel.setStyle('bold')
        invLabel.draw(self.window)
        invRect = Rectangle(Point(invX, invY + lineSpace), Point(invX + invWidth, invY + lineSpace + invHeight))
        invRect.setFill("white")
        invRect.draw(self.window)
        self.invWin = Text(Point(invX + boxOffset, invY + lineSpace + boxOffset), " ")
        self.invWin.draw(self.window)

        # bottom right is buttons
        buttonX = sideOffset + self.mapSize + lineSpace
        buttonY = sideOffset + lineSpace + invHeight + lineSpace
        self.buttonX, self.buttonY = buttonX, buttonY

        # Draw the gameboard
        tileLength = 50
        chessBoard = self.game.getBoardImage()
        self.chessBoard = Image(Point(self.mapRectX + 4*tileLength, self.mapRectY + 4*tileLength), tileLength,tileLength)
        self.chessBoard.setImage(chessBoard)
        self.chessBoard.draw(self.window)
      
        # Buttons if Pawn:
        if not isQueen:
          self.up = Button(Point(buttonX + buttonWidth/2, buttonY), "↑", partial(self.do, self.protagonistPiece.goUp), buttonColor)
          self.doubleJump = Button(Point(buttonX + buttonWidth/2, buttonY + lineSpace*2), "↑↑", partial(self.do, self.protagonistPiece.doubleJump), buttonColor)
          self.capturePieceLeft = Button(Point(buttonX + buttonWidth*1/4, buttonY + lineSpace), "↖", partial(self.do, self.protagonistPiece.capturePieceLeft), buttonColor)
          self.capturePieceRight = Button(Point(buttonX + buttonWidth*3/4, buttonY + lineSpace), "↗", partial(self.do, self.protagonistPiece.capturePieceRight), buttonColor)
          self.printPath = Button(Point(buttonX + buttonWidth/2, buttonY+lineSpace*4), "Show Path", partial(self.do, self.drawPath), "lightgreen")

          #Draws the pawn buttons on the window
          self.up.draw(self.window)
          self.doubleJump.draw(self.window)
          self.capturePieceLeft.draw(self.window)
          self.capturePieceRight.draw(self.window)
          self.printPath.draw(self.window)

        #If the protagonist is a queen, then redrawButtons()
        #Will draw the queen's buttons seperatly
        else:
          self.distance = 1
          self.redrawButtons()
  
        if self.protagonistPiece.getInventoryInt() >= 29:
          self.addBackButton()
        # # Draw new
        # self.left.draw(self.window)
        # self.right.draw(self.window)
        # self.down.draw(self.window)
      
        # bind keyboard's key to callbacks
        self.window._keyboardCallback = self.keypressed
       

        self.images = []
        for x in range(self.size):
            self.images.append([])
            for y in range(self.size):
                self.images[x].append(None)

        self.isUpdating = False


        ## initialize pieces
        enemyList = self.game.returnEnemies()
        portalList = self.game.generatePortals()
        # Portals
        self.portalQueue = Queue() #I made the portal image locations a Queue
        # Black pawns
        self.imageObjects = []   #I made the black pawn image locations a List (superior data type)
        for point in enemyList:
          if point:
            loc = Point(point[0],point[1])
            tileLength = 50
            enemyPawn = self.game.getEnemyPawnImage()
            self.enemyPawn = Image(Point(self.mapRectX + loc.x*tileLength + tileLength//2, self.mapRectY + loc.y*tileLength + tileLength//2), tileLength,tileLength)
            self.enemyPawn.setImage(enemyPawn)
            self.enemyPawn.draw(self.window)
            self.imageObjects.append(self.enemyPawn)
          else:
            self.imageObjects.append(None)
        for point in portalList:
          if point:
            loc = Point(point[0],point[1])
            tileLength = 50
            portal = self.game.getPortalImage()
            self.portal = Image(Point(self.mapRectX + loc.x*tileLength + tileLength//2,
                  self.mapRectY + loc.y*tileLength + tileLength//2),
          tileLength,tileLength)
            self.portal.setImage(portal)
            self.portal.draw(self.window)
            self.portalQueue.enqueue(self.portal)

    def erase(self, index):
      #undraws stuff
      self.imageObjects[index].undraw()
      self.imageObjects[index] = None

    def keypressed(self, ch):
      #Binds the keys to functions depending if the protagonistPiece
      #Is a queen or not
      global isQueen
      if not isQueen:
        if ch in ['w', 'W', u"\u2729"]:
            self.do(self.protagonistPiece.goUp)
        elif ch in ['s', 'S']:
            self.do(self.protagonistPiece.goDown)
        elif ch in ['p', 'P']:
          self.do(self.protagonistPiece.doubleJump)
        elif ch in ['a', 'A']:
            self.do(self.protagonistPiece.goLeft)
        elif ch in ['d', 'D']: 
            self.do(self.protagonistPiece.goRight)
        elif ch in ['k', 'K']:
            self.do(self.protagonistPiece.capturePieceLeft)
        elif ch in ['j', 'J']:
            self.do(self.protagonistPiece.capturePieceRight)
        elif ch in [' ']:
            self.do(self.game.performTask)
        elif ch in ['h', 'H']:
            self.do(self.game.showWayBack)
        elif ch in [chr(27)]:
            self.window.close()
      else:
        if ch in ['w', 'W', u"\u2729"]:
            self.do(self.protagonistPiece.goUp, self.distance)
        elif ch in ['s', 'S']:
            self.do(self.protagonistPiece.goDown, self.distance)
        elif ch in ['a', 'A']:
            self.do(self.protagonistPiece.goLeft, self.distance)
        elif ch in ['d', 'D']: 
            self.do(self.protagonistPiece.goRight, self.distance)
        elif ch in ['q', 'Q']:
            self.do(self.protagonistPiece.goUpLeft, self.distance)
        elif ch in ['e', 'E']:
            self.do(self.protagonistPiece.goUpRight, self.distance)
        elif ch in ['z', 'Z']:
            self.do(self.protagonistPiece.goDownLeft, self.distance)
        elif ch in ['c', 'C']:
            self.do(self.protagonistPiece.goDownRight, self.distance)
        elif ch in [' ']:
            self.do(self.game.performTask)
        
        elif ch in [chr(27)]:
            self.window.close()

    def do(self, fncn, val = None):
        """ Wrapper class that runs the provided function and then
            updates the GUI. """
        if self.isUpdating:
            return
        if val:
          fncn(val)
        else:
          fncn()
        self.updateGUI()

    def updateGUI(self):
      #This updates the GUI
        global isQueen
        """ Update the GUI (tasks, inventory, grid) """
        self.isUpdating = True
        if (self.protagonistPiece != self.game.returnProtagonistPiece()) and not isQueen:
          self.protagonistPiece = self.game.returnProtagonistPiece()
          isQueen = True
          #This updates the isQueen Boolean
          #This is done based on the data type of the protagonistPiece
          #If the data type has changed, then protagonistPiece has turned
          #From pawn to Queen
          self.distance = 1
          self.redrawButtons()
          self.taskWin.undraw()
          self.taskWin = Text(Point(15, 40), "Collect 20 more pawns")
          self.taskWin.draw(self.window)
        if self.protagonistPiece.getInventoryInt() >= 29:
          self.addBackButton()
          self.taskWin.undraw()
          self.taskWin = Text(Point(15,40), "Go back to World 1 to win the game!")
          self.taskWin.draw(self.window)
        if self.protagonistPiece.getInventoryInt() == 29:
          try:
            if self.backButton:
              pass
            pass
          except:
            self.addBackButton()
        tileLength = 50

        
      
        #Sets the image of the protagonistPiece
        if not isQueen:
          piece = self.game.getPawnImage()
          loc = self.protagonistPiece.getPawnLocation()
        else:
          piece = self.game.getQueenImage()
          loc = self.protagonistPiece.getQueenLocation()
        
        try: # decently non-flickery
            self.piece.undraw()
        except Exception:
            pass
        if loc != None and piece != None:
            self.piece = Image(Point(self.mapRectX + loc.x*tileLength + tileLength//2,
                                     self.mapRectY + loc.y*tileLength + tileLength//2),
                               tileLength,tileLength)
            

            
            
            self.piece.setImage(piece)
            self.piece.draw(self.window)
        

        # Update the inventory field
        invText = self.protagonistPiece.getInventory()
        oldInvText = self.invWin.config["text"]
        if invText != None and invText != oldInvText:
            self.invWin.undraw()
            self.invWin.config["text"] = invText
            self.invWin.draw(self.window)

        self.isUpdating = False
        
    def nothing(self):
        """ Called by the help button. Could be replaced by a function
            that actually does something. """
        pass


    def defineNums(self):
      # Makes the number buttons. Peter did this. Nice job Peter.
      self.buttonColor = "greenyellow"
      self.one = Button(Point(self.buttonX + self.buttonWidth*9/32, self.buttonY + self.lineSpace*5), "1", partial(self.do, self.selectNumber, 1), self.buttonColor)
      self.two = Button(Point(self.buttonX + self.buttonWidth*1/2, self.buttonY + self.lineSpace*5), "2", partial(self.do, self.selectNumber, 2), self.buttonColor)
      self.three = Button(Point(self.buttonX + self.buttonWidth*23/32, self.buttonY + self.lineSpace*5), "3", partial(self.do, self.selectNumber, 3), self.buttonColor)
      self.four = Button(Point(self.buttonX + self.buttonWidth*9/32, self.buttonY + self.lineSpace*6.3), "4", partial(self.do, self.selectNumber, 4), self.buttonColor)
      self.five = Button(Point(self.buttonX + self.buttonWidth*1/2, self.buttonY + self.lineSpace*6.3), "5", partial(self.do, self.selectNumber, 5), self.buttonColor)
      self.six = Button(Point(self.buttonX + self.buttonWidth*23/32, self.buttonY + self.lineSpace*6.3), "6", partial(self.do, self.selectNumber, 6), self.buttonColor)
      self.seven = Button(Point(self.buttonX + self.buttonWidth*9/32, self.buttonY + self.lineSpace*7.6), "7", partial(self.do, self.selectNumber, 7), self.buttonColor)
      self.eight = Button(Point(self.buttonX + self.buttonWidth*1/2, self.buttonY + self.lineSpace*7.6), "8", partial(self.do, self.selectNumber, 8), self.buttonColor)
      self.nine = Button(Point(self.buttonX + self.buttonWidth*23/32, self.buttonY + self.lineSpace*7.6), "9", partial(self.do, self.selectNumber, 9), self.buttonColor)

    def drawNums(self):
      # Draw
      for numButton in [self.one, self.two,self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]:
        try:
          numButton.draw(self.window)
        except:
          pass

    #These are all of the buttons for the queen's movement
    def defineDirections(self):
      self.buttonColor = "lightpink"
      self.up = Button(Point(self.buttonX + self.buttonWidth/2, self.buttonY), "↑", partial(self.do, self.protagonistPiece.goUp, self.distance), self.buttonColor)
      self.left = Button(Point(self.buttonX + self.buttonWidth*9/32, self.buttonY + self.lineSpace*1.3), "←", partial(self.do, self.protagonistPiece.goLeft, self.distance), self.buttonColor)
      self.right = Button(Point(self.buttonX + self.buttonWidth*23/32, self.buttonY + self.lineSpace*1.3), "→", partial(self.do, self.protagonistPiece.goRight, self.distance), self.buttonColor)
      self.down = Button(Point(self.buttonX + self.buttonWidth/2, self.buttonY + self.lineSpace*2.6), "↓", partial(self.do, self.protagonistPiece.goDown, self.distance), self.buttonColor)
      self.leftUp = Button(Point(self.buttonX + self.buttonWidth*9/32, self.buttonY), "↖", partial(self.do, self.protagonistPiece.goUpLeft, self.distance), self.buttonColor)
      self.rightUp = Button(Point(self.buttonX + self.buttonWidth*23/32, self.buttonY), "↗", partial(self.do, self.protagonistPiece.goUpRight, self.distance), self.buttonColor)
      self.leftDown = Button(Point(self.buttonX + self.buttonWidth*9/32, self.buttonY+self.lineSpace*2.6), "↙", partial(self.do, self.protagonistPiece.goDownLeft, self.distance), self.buttonColor)
      self.rightDown = Button(Point(self.buttonX + self.buttonWidth*23/32, self.buttonY+self.lineSpace*2.6), "↘", partial(self.do, self.protagonistPiece.goDownRight, self.distance), self.buttonColor)
      # Draw new
      self.up.draw(self.window)
      self.left.draw(self.window)
      self.right.draw(self.window)
      self.down.draw(self.window)
      self.leftUp.draw(self.window)
      self.rightUp.draw(self.window)
      self.leftDown.draw(self.window)
      self.rightDown.draw(self.window)
      
    def redrawButtons(self):
      # Erase old
      try:
        self.up.undraw()
        self.doubleJump.undraw()
        self.capturePieceLeft.undraw()
        self.capturePieceRight.undraw()
        self.printPath.undraw()
      except:
        pass
      self.defineDirections()
      
      # Numbers
      self.defineNums()
      self.one.bkcolor = "sandybrown"
      self.drawNums()
      
    def addBackButton(self):
      try:
        self.backButton.undraw()
      except:
        pass
      self.backButton = Button(Point(self.buttonX + self.buttonWidth/2, self.buttonY + self.lineSpace*1.3), "↻", partial(self.do, self.protagonistPiece.goBack, self.distance), "turquoise")
      self.backButton.draw(self.window)

      

  

    def selectNumber(self, num):
      #Rewrites the distance traveled by the directional keys based on the number buttons.
      self.defineNums()
      
      button_mapping = {
        1: self.one,
        2: self.two,
        3: self.three,
        4: self.four,
        5: self.five,
        6: self.six,
        7: self.seven,
        8: self.eight,
        9: self.nine
      }
      self.distance = num
      self.defineDirections()

      
      button_mapping[num].bkcolor = "sandybrown"
      #Makes the selected distance button orange colored.
      self.drawNums()



    def drawPath(self):
      #Uses recursion to find a path forwards for those new to the rules of chess.
      #No shame if you need to use this feature.
      circleImages = []
      circlePositions = []
      pawnLoc = self.protagonistPiece.getPawnLocation()
      isSolvable, circlePositions = self.protagonistPiece.checkColumn(pawnLoc.x, pawnLoc.y, [])
      if isSolvable:
        for point in circlePositions:
          if point[1]<pawnLoc.y:
            loc = Point(point[0],point[1])
            tileLength = 50
            greenCircle = self.game.getGreenCircleImage()
            self.greenCircle = Image(Point(self.mapRectX + loc.x*tileLength + tileLength//2,
                self.mapRectY + loc.y*tileLength + tileLength//2),
          tileLength,tileLength)
            self.greenCircle.setImage(greenCircle)
            self.greenCircle.draw(self.window)
            circleImages.append(self.greenCircle)
        time.sleep(2)
        for image in circleImages:
          image.undraw()
      else:
        #Execues if there are no possible paths. This will never happen
        #naturally, we designed the game so that there are no forced
        #dead ends. However, the user can make dead ends occur.
        self.noPathWarning = Text(Point(self.buttonX + self.buttonWidth/4.5, self.buttonY*1.4), "NO PATH FOUND")
        self.noPathWarning.draw(self.window)
        self.printPath.undraw()
        self.printPath.bkcolor = "orangered"
        self.printPath.draw(self.window)
        time.sleep(1.5)
        self.noPathWarning.undraw()

  
    def run(self):
        """ Repeatedly wait for a click.. Keeps the game running. """
        self.updateGUI()

        while(self.window.isOpen()):
            try:
                pt = self.window.getMouse()
            except Exception:
                pass
        

   
