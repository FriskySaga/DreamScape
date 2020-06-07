"""
Unit test for Monster class.
"""

# Python imports
import unittest

# Project imports
from Source.Monster import Monster

class MonsterTest(unittest.TestCase):

  def testAbstractClass(self):
    """Ensure the class is abstract.
    """
    try:
      myMonster = Monster()
    except TypeError as e:
      self.assertEqual(str(e),
        "Can't instantiate abstract class Monster with "
        "abstract methods examine")
    else:
      self.assertFalse(True)

unittest.main()