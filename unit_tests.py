import unittest
from io import StringIO
import sys
from PortalSaga.Game import *
from PortalSaga.Queen import *
from PortalSaga.Pawn import *
from DS.Array import *
#The rubric says we need at least three unit tests. No other explanations are given

class Testing(unittest.TestCase):
  def test_enemyListGeneraton(self):
    g = Game()
    testList = g.generateEnemies()
    len = testList.__len__()
    self.assertTrue(len == 16 or len == 32)
  
  def test_QueenInitialization(self):
    try:
      g = Game()
      enemyList = [0,1]
      portalList = g.generatePortals()
      inventory = 1
      location = [0,0]
      sampleQueen = Queen(enemyList, portalList, inventory, location)
      self.assertTrue(True)
    except:
      self.assertTrue(False)
  
  def test_checkQueenInventory(self):
    g = Game()
    enemyList = [0,1]
    portalList = g.generatePortals()
    inventory = 3
    location = [0,0]
    sampleQueen = Queen(enemyList, portalList, inventory, location)
    self.assertTrue("3 Pawns" == sampleQueen.getInventory())

  def test_checkPawnInventory(self):
    g = Game()
    enemyList = Array(1)
    enemyList.__setitem__(0, [0,1])
    portalList = g.generatePortals()
    inventory = 4
    samplePawn = Pawn(enemyList, portalList, inventory)
    self.assertTrue("4 Pawns" == samplePawn.getInventory())


unittest.main()