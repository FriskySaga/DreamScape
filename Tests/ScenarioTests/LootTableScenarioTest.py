"""
Example of how a loot table in an RPG may be implemented.
"""

# Python imports
import random, unittest

# Project imports
from Source.AllMonsters import *
from Source.Player import Player
from Source import QuestEnums

class LootTableScenarioTest(unittest.TestCase):
  def setUp(self):
    self.Gavin = Player()
    self.Gavin.markAsActiveQuest(QuestEnums.A_DRUNKEN_DWARF)

  def testLootFarmer(self):
    loot = Farmer().dropLoot(self.Gavin.activeQuestList)
    self.assertTrue("Bones" in loot)
    print("\nFarmer's loot:", loot)
  
  def testLootHillGiant(self):
    loot = HillGiant().dropLoot(self.Gavin.activeQuestList)
    self.assertTrue("Big Bones" in loot)
    print("\nHill Giant's loot:", loot)

unittest.main()