"""
Unit test for LootTable
"""

"""
Example of how a loot table in an RPG may be implemented.
"""

# Python imports
import random

# Project imports
from Source.Monsters import *
from Source.Player import Player
from Source import QuestEnums

gavin = Player()
gavin.markAsActiveQuest(QuestEnums.A_DRUNKEN_DWARF)
gavinActiveQuests = gavin.activeQuestList
print(Farmer().dropLoot(gavinActiveQuests))
print(HillGiant().dropLoot(gavinActiveQuests))