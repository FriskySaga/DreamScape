"""
Base class to represent a monster, which is an attackable NPC.
"""

# Python imports
from abc import ABC, abstractmethod
import random

class Monster(ABC):

  def __init__(self):
    """
    NOTE self.dropTable must be defined in subclass
    NOTE self.hasRareDrop must be defined in subclass
    
    EXAMPLE
    self.dropTable = {
      "Bernadette": (0.5, True, [5, 72]),
    }

    KEY
    self.dropTable = {
      "Item Name" : (dropProbability, isItemUnique, associatedQuestIDs)
    }
    """
    self.rareDropTable = {
      "Blue Party Hat": (0.5, True, []),
      "Red Party Hat": (0.5, True, [])
    }

  @staticmethod
  @abstractmethod
  def examine():
    """
    Show examine text on a monster.

    :return: The examine text, as a string
    """
    pass

  def dropLoot(self, activeQuestList):
    """
    Drop loot upon death.

    :param activeQuestList: The list of the player's active quests, as quest IDs

    :return: The items to drop, as a list of strings
    """
    toDrop = []

    self.__rollLootTable(toDrop, self.dropTable, False, activeQuestList)
    
    # Roll the rare drop table on a 0.01% chance
    if self.hasRareDrop:
      if random.random() < 0.0001:
        self.__rollLootTable(toDrop, self.rareDropTable, True, activeQuestList)

    return toDrop

  def __rollLootTable(self, toDrop, dropTable, isRareDropTable, activeQuestList):
    """
    Roll the loot table.

    :param toDrop: The current list of items to drop as loot, as strings
    :param dropTable: The table of items that can be dropped, as dictionaries
    :param isRareDropTable: Whether given dropTable is the rare drop table, as a boolean
    :param activeQuestList: The list of the player's active quests, as quest IDs

    NOTE toDrop is modified

    TODO Refactor method to not need the argument `isRareDropTable`
    """

    # Go through the given drop table
    for item, dropProperties in dropTable.items():

      dropProbability = dropProperties[0]
      isItemUnique = dropProperties[1]
      associatedQuestList = dropProperties[2]
      
      # If the item is not a quest-only item
      if not associatedQuestList:
        if not isRareDropTable:
          self.__addToDropLoot(toDrop, item, dropProbability, isItemUnique)
        
        # If the drop is from the rare drop table, only drop at most one rare item
        else:
          self.__addToDropLoot(toDrop, item, dropProbability, True)
          break
      
      # Otherwise, the drop is a quest-only item...
      else:
        # Then, loop through each quest that is associated with the drop...
        for quest in associatedQuestList:
          # And if the player is working the quest, then consider dropping the item.
          # NOTE If the player is working multiple quests relevant to the drop, DON'T drop once for each quest being worked
          if quest in activeQuestList:
            self.__addToDropLoot(toDrop, item, dropProbability, isItemUnique)
            break

  def __addToDropLoot(self, toDrop, item, dropProbability, isItemUnique):
    """
    Add an item to the current drop loot.

    :param toDrop: The current list of items to drop as loot, as strings
    :param item: The item to drop, as a string
    :param dropProbability: The drop probability of the item, as a float
    :param isItemUnique: Whether the item is unique, as a boolean
    
    :return: Whether the given item was added to the drop loot, as a boolean

    NOTE toDrop is modified
    """
    # Save the count prior to adding to the drop loot
    numItemsToDrop = len(toDrop)

    # Items with 100% drop probability only drop once
    if dropProbability == 1:
      toDrop.append(item)
    
    # Unique items can only drop once
    elif isItemUnique:
      if random.random() < dropProbability:
        toDrop.append(item)
    
    # All other items can drop multiple times
    else:
      while random.random() < dropProbability:
        toDrop.append(item)
    
    return len(toDrop) > numItemsToDrop