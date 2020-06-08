"""
Loot table data structure.

NOTE This class is unused
TODO Integrate this class
TODO Create unit tests
"""

class LootTable:
  def __init__(self, isRareLootTable = False):
    self._isRareLootTable = isRareLootTable
    self._lootTable = {}
  
  @property
  def isRareLootTable(self):
    return self._isRareLootTable
  
  @isRareLootTable.setter
  def isRareLootTable(self, value):
    self._isRareLootTable = value
  
  @property
  def lootTable(self):
    return self._lootTable
  
  @lootTable.setter
  def lootTable(self, value):
    self._lootTable = value