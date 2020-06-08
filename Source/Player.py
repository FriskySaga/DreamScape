"""
Class to represent a Player

TODO Create unit tests
"""

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