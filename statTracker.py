class WinLoss:
  def __init__(self):
    self.winLoss = []

  def addWinOrLoss(self, stat):
    self.winLoss.append(stat)

  def clearWinLoss(self):
    self.winLoss = []
