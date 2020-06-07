from Source.Monster import Monster

class Farmer(Monster):

  def __init__(self):
    super().__init__()
    self.dropTable = {
      "Bones": (1.0, False, []),
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
      "Big Bones": (1.0, False, []),
      "Limpwurt Root": (0.3, False, []),
      "Dwarven Emblem": (0.5, True, [1])
    }
    self.hasRareDropTable = True

  @staticmethod
  def examine():
    return ("Overgrown brute hailing from the hills.")
