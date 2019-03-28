class Table():
  def __init__(self):
    self.playerHands = [[], [], [], [], [], []]
    self.dealer = []

  def setPlayerPosition(self, position):
    self.playerHands[position].append('[ PLAYER ]')
    self.playerHands[position].append([])

  def fillTablePositions(self):
    for j in range(0, 6):
      if self.playerHands[j] == []:
        self.playerHands[j].append('npc')
        self.playerHands[j].append([])
      elif self.playerHands[j] == 'player':
        pass
    return self.playerHands
