"""
Example of how a loot table in an RPG may be implemented.
"""

# Python imports
from abc import ABC, abstractmethod
import random

# Project imports
from Source import QuestEnums

class Player:
    def __init__(self):
        self._activeQuestList = []

    @property
    def activeQuestList(self):
      """
      Get the player's active quests.

      :return: The list of quest IDs, as a list of integer
      """
      return self._activeQuestList

    def markAsActiveQuest(self, questID):
      """
      Add a quest to the list of the player's active quests.

      :param questID: The quest ID, as an integer
      """
      self._activeQuestList.append(questID)

class Monster(ABC):

  def __init__(self):
    self.dropTable = {}

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

    self.rollDropTable(toDrop, self.dropTable, False, activeQuestList)
    
    # Roll the rare drop table on a 0.01% chance
    if self.hasRareDropTable:
      if random.random() > 0.0001:
        self.rollDropTable(toDrop, self.rareDropTable, True, activeQuestList)

    return toDrop

  def rollDropTable(self, toDrop, dropTable, isRareDropTable, activeQuestList):
    """
    Roll the drop table.

    :param toDrop: The current list of items to drop as loot, as strings
    :param dropTable: The table of items that can be dropped, as dictionaries
    :param isRareDropTable: Whether given dropTable is the rare drop table, as a boolean
    :param activeQuestList: The list of the player's active quests, as quest IDs

    NOTE toDrop is modified
    """
    alreadyDroppedRareItem = False

    for item, dropProperties in dropTable.items():
      # Defining here for readability
      dropProbability = dropProperties[0]
      itemIsUnique = dropProperties[1]
      dropAssociatedQuestList = dropProperties[2]

      # If the drop is from the rare drop table, only drop a maximum of one rare item per loot
      if isRareDropTable and not alreadyDroppedRareItem:
        alreadyDroppedRareItem = self.addToDropLoot(toDrop, item, dropProbability, True)

      # If the drop is a quest-only item...
      elif dropAssociatedQuestList:
        # Then, loop through each quest that is associated with the drop...
        for quest in dropAssociatedQuestList:
          # And if the player is working the quest, then consider dropping the item.
          # NOTE If the player is working multiple quests relevant to the drop, DON'T drop once for each quest being worked
          if quest in activeQuestList:
            self.addToDropLoot(toDrop, item, dropProbability, itemIsUnique)
            break
      
      # Otherwise, the item is not a quest-only item
      else:
        self.addToDropLoot(toDrop, item, dropProbability, itemIsUnique)

  def addToDropLoot(self, toDrop, item, dropProbability, itemIsUnique):
    """
    Add an item to the current drop loot.

    :param toDrop: The current list of items to drop as loot, as strings
    :param item: The item to drop, as a string
    :param dropProbability: The drop probability of the item, as a float
    :param itemIsUnique: Whether the item is unique, as a boolean
    
    :return: Whether the given item was added to the drop loot, as a boolean

    NOTE toDrop is modified
    """
    # Save the count prior to adding to the drop loot
    numItemsToDrop = len(toDrop)

    # Items with 100% drop probability only drop once
    if dropProbability == 1:
      toDrop.append(item)
    
    # Unique items can only drop once
    elif itemIsUnique:
      if random.random() < dropProbability:
        toDrop.append(item)
    
    # All other items can drop multiple times
    else:
      while random.random() < dropProbability:
        toDrop.append(item)
    
    return len(toDrop) > numItemsToDrop

class Farmer(Monster):

  def __init__(self):
    super().__init__()
    self.dropTable = {
      "Bones": (1, False, []),
      "Potato Seed": (0.3, False, []),
      "Tomato Seed": (0.2, False, []),
      "Stolen Waffle": (1.0, True, [2])
    }
    self.hasRareDropTable = False

  @staticmethod
  def examine():
    return ("This guy sure likes to grow stuff!")
  

class HillGiant(Monster):

  def __init__(self):
    super().__init__()
    self.dropTable = {
      "Big Bones": (1, False, []),
      "Limpwurt Root": (0.3, False, []),
      "Dwarven Emblem": (1.0, True, [1])
    }
    self.hasRareDropTable = True

  @staticmethod
  def examine():
    return ("Overgrown brute hailing from the hills.")


gavin = Player()
gavin.markAsActiveQuest(QuestEnums.A_DRUNKEN_DWARF)
gavinActiveQuests = gavin.activeQuestList
print(Farmer().dropLoot(gavinActiveQuests))
print(HillGiant().dropLoot(gavinActiveQuests))