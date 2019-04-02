import time
import gameFunctions as gf

class Player():
  def __init__(self):
    self.playerHand = ['PLAYER', [], 0]
    self.playerPlusMinus = 0
    self.bet = 0

  def getPlayerTotal(self):
    inputString = 'enter the dollar amount you want to start with: '
    amount = input(inputString)

    try:
      amount = int(amount)
      if amount < 0:
        print('invalid dollar value, try again.')
        time.sleep(1.25)
        self.getPlayerTotal()
      else:
        self.playerHand[2] = amount
    except:
      print('invalid dollar value, try again.')
      time.sleep(1.25)
      self.getPlayerTotal()

    gf.clear_screen()

  def getPlayerBet(self):
    inputString = 'enter the dollar amount you want to bet this hand, or enter "0" if you want exit: '
    amount = input(inputString)

    try:
      amount = int(amount)
      if  amount < 0:
        print('invalid dollar value, try again.')
        time.sleep(1.25)
        self.getPlayerBet()
      elif amount == 0:
        return amount
      else:
        self.bet = amount
    except:
      print('invalid dollar value, try again.')
      time.sleep(1.25)
      self.getPlayerBet()

  def determineWinLoss(self, playerCards, dealerCards):
    cardTotal = gf.countPlayerTotal(playerCards)
    dealerTotal = gf.countPlayerTotal(dealerCards)

    if cardTotal == 'BUST':
      self.playerHand[2] -= self.bet
      self.playerPlusMinus -= self.bet
    elif dealerTotal == 'BUST':
      self.playerHand[2] += self.bet
      self.playerPlusMinus += self.bet
    elif cardTotal > dealerTotal:
      if cardTotal == 21:
        self.playerHand[2] += self.bet * 1.5
        self.playerPlusMinus += self.bet * 1.5
      else:
        self.playerHand[2] += self.bet
        self.playerPlusMinus += self.bet
    elif cardTotal < dealerTotal:
      self.playerHand[2] -= self.bet
      self.playerPlusMinus -= self.bet
    elif cardTotal == dealerTotal:
      pass

    self.clearPlayerBet()

  def isBroke(self):
    if self.playerHand[2] <= 0:
      return gf.playerIsBroke()
    else:
      return True

  def clearPlayerBet(self):
    self.bet = 0
    