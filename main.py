import cards, userPlayer, table, statTracker
import gameFunctions as gf
import statFunctions as sf

def main():
  gf.clear_screen()
  playGame()

def playGame():
  hardBreak = True

  gameDeck = cards.GameDeck()
  gameDeck.shuffleDeck()
  gameDeck.dealerCut()

  player = userPlayer.Player()

  gameTable = table.Table()
  gameTable.fillTablePositions()


  playerPosition = gf.getPlayerPosition()
  gameTable.setPlayerPosition(playerPosition, player.playerHand)
  player.getPlayerTotal()

  winLossTracker = statTracker.WinLoss()

  while gameDeck.continueGame == True:

    bet = player.getPlayerBet(player.playerHand[2]) # pylint-ignore
    if bet == 0:
      gameDeck.continueGame = False
      break

    gf.theDeal(gameDeck, gameTable.dealer, gameTable.playerHands)

    gf.thePlay(gameDeck, gameTable.dealer, gameTable.playerHands)
    gf.endThePlay()

    gf.dealersPlay(gameDeck, gameTable.dealer, gameTable.playerHands)

    player.determineWinLoss(player.playerHand[1], gameTable.dealer)

    winLossTracker.addWinOrLoss(player.getWinLossStat(player.playerHand[1], gameTable.dealer, player.playerHand[2]))

    input('press enter to view hand results.')
    gf.displayHandResults(gameTable.dealer, gameTable.playerHands, player.playerHand[2], player.playerPlusMinus)
    input('press enter to continue to the next hand.')

    hardBreak = player.isBroke()
    if hardBreak == False:
      gameDeck.continueGame = False

    gameTable.clearTable()

  winLossStat = winLossTracker.winLoss
  sf.plotWinLoss(winLossStat)
  input('press enter to end game.')
  gf.clear_screen()
  gf.exit()

if __name__ == '__main__':
  main()
