"""
Unit test for all monster classes.

TODO Unit test __rollLootTable()
TODO Unit test __addToDropLoot()
"""

# Python imports
import unittest

# Project imports
from Source.AllMonsters import *
from Source import QuestEnums

class DummyMonsterA(Monster):
  def __init__(self):
    super().__init__()
    self.dropTable = {
      "Ashes": (1.0, False, []),
      "Doric's Ale": (1.0, False, [QuestEnums.A_DRUNKEN_DWARF, QuestEnums.THE_SWORD_OF_THRAZDUIN]),
    }
    self.hasRareDrop = False

  @staticmethod
  def examine():
    return "This monster does not have rare drops."

class DummyMonsterB(Monster):
  def __init__(self):
    super().__init__()
    self.dropTable = {}
    self.hasRareDrop = True

  @staticmethod
  def examine():
    return "This monster only has rare drops."

class GenericMonsterTest(unittest.TestCase):

  def setUp(self):
    self.Farmer = Farmer()
    self.HillGiant = HillGiant()
  
  def testDropTable(self):
    """Validate each drop table.
    """
    self.validateDropTable(self.Farmer)
    self.validateDropTable(self.HillGiant)

  def validateDropTable(self, monster):
    """Validate that the drop table makes sense.
    """
    # NOTE It is acceptable for a drop table to be empty

    for k, v in monster.dropTable.items():

      # Validate the key is a string
      self.assertEqual(type(k), str)

      # Validate the value is a three-tuple
      self.assertEqual(type(v), tuple)
      self.assertEqual(len(v), 3)

      # Drop probability is within the range 0% - 100%
      dropProbability = v[0]
      self.assertEqual(type(dropProbability), float)
      self.assertLessEqual(dropProbability, 1.0)
      self.assertGreater(dropProbability, 0.0)

      # Unique item is a boolean value
      isItemUnique = v[1]
      self.assertEqual(type(isItemUnique), bool)

      # Associated quest list only has integers
      associatedQuestList = v[2]
      self.assertEqual(type(associatedQuestList), list)
      for questID in associatedQuestList:
        self.assertEqual(type(questID), int)
    
    # Verify the monster has a rare drop table flag
    self.assertEqual(type(monster.hasRareDrop), bool)

  def testExamine(self):
    """Validate each examine text.
    """
    self.validateExamine(self.Farmer)
    self.validateExamine(self.HillGiant)

  def validateExamine(self, monster):
    """Validate that the examine text is properly formatted.
    """
    textToExamine = monster.examine()

    # Confirm the examine is a string
    self.assertEqual(type(textToExamine), str)

    # Confirm the examine starts with a capital letter
    self.assertTrue(textToExamine[0].isupper())
    
    # Confirm the examine ends with a valid punctuation symbol
    self.assertTrue(textToExamine.endswith(".")
      or textToExamine.endswith("?")
      or textToExamine.endswith("!"))

  def testDropLoot(self):
    """Validate dropLoot().
    """
    questList = [QuestEnums.A_DRUNKEN_DWARF,
                 QuestEnums.THE_STOLEN_WAFFLE,
                 QuestEnums.THE_SWORD_OF_THRAZDUIN]
    
    # Check that DummyMonsterA always drops only one instance
    # of ashes and one instance of Doric's Ale
    loot = DummyMonsterA().dropLoot(questList)
    self.assertTrue("Ashes" in loot)
    self.assertTrue("Doric's Ale" in loot)
    self.assertEqual(len(loot), 2)
    
    # Check that DummyMonsterB can access the rare drop table
    foundRareDrop = False
    for x in range(1000000):
      loot = DummyMonsterB().dropLoot(questList)
      if len(loot) == 1:
        foundRareDrop = True
        break
      # A maximum of one rare drop should be present, so fail the test otherwise
      elif loot:
        print("AllMonstersUnitTest::testDropLoot() - Multiple rare items: ", dropLoot)
        break
    self.assertTrue(foundRareDrop)

unittest.main()