class Table():
  def __init__(self):
    self.playerHands = [[], [], [], [], [], []]
    self.dealer = []

  def setPlayerPosition(self, position, player):
    self.playerHands[position] = player

  def fillTablePositions(self):
    for j in range(0, 6):
      if self.playerHands[j] == []:
        self.playerHands[j].append('NPC')
        self.playerHands[j].append([])
      elif self.playerHands[j] == 'PLAYER':
        pass
    return self.playerHands

  def clearTable(self):
    self.dealer = []
    for player in self.playerHands:
      player[1] = []
