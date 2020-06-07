"""
Unit test for various monster classes.
"""

# Python imports
import unittest

# Project imports
from Source.Monsters import *

class FarmerTest(unittest.TestCase):

  def setUp(self):
    self.Billy = Farmer()

  def testDropTable(self):
    """Validate that the drop table make sense.
    """

    # Drop table is not empty
    self.assertTrue(self.Billy.dropTable)

    for k, v in self.Billy.dropTable.items():

      # Validate the key is a string
      self.assertEqual(type(k), str)

      # Validate the value is a three-tuple
      self.assertEqual(type(v), tuple)
      self.assertEqual(len(v), 3)

      # Drop probability does not exceed 100%
      dropProbability = v[0]
      self.assertEqual(type(dropProbability), float)
      self.assertLessEqual(dropProbability, 1.0)

      # Unique item is a boolean value
      isItemUnique = v[1]
      self.assertEqual(type(isItemUnique), bool)

      # Associated quest list only has integers
      associatedQuestList = v[2]
      self.assertEqual(type(associatedQuestList), list)
      for questID in associatedQuestList:
        self.assertEqual(type(questID), int)
    
    # Verify this monster has a rare drop table flag
    self.assertEqual(type(self.Billy.hasRareDropTable), bool)

unittest.main()