import time

class Player():
  def __init__(self):
    self.playerHand = ['PLAYER', []]
    self.playerTotal = 0
    self.playerPlusMinus = 0
    self.bet = 0

  def getPlayerTotal(self):
    inputString = 'enter the dollar amount you want to start with: '
    amount = input(inputString)

    if type(amount) != int and amount <= 0:
      print('invalid dollar value, try again.')
      time.sleep(1.25)
      self.getPlayerTotal()
    else:
      self.playerTotal = amount

  def getPlayerBet(self):
    inputString = 'enter the dollar amount you want to bet this hand: '
    amount = input(inputString)

    if type(amount) != int and amount <= 0:
      print('invalid dollar value, try again.')
      time.sleep(1.25)
      self.getPlayerTotal()
    else:
      self.bet = amount

  def clearPlayerBet(self):
    self.bet = 0
    