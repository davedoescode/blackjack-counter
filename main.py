import cards, userPlayer, table
import gameFunctions as gf

def main():
  gf.clear_screen()
  playGame()

def playGame():
  gameDeck = cards.GameDeck()
  gameDeck.shuffleDeck()
  gameDeck.dealerCut()

  player = userPlayer.Player()

  gameTable = table.Table()
  gameTable.fillTablePositions()


  playerPosition = gf.getPlayerPosition()
  gameTable.setPlayerPosition(playerPosition, player.playerHand)
  player.getPlayerTotal()

  while gameDeck.continueGame == True:

    bet = player.getPlayerBet() # pylint-ignore
    if bet == 0:
      gameDeck.continueGame = False
      break

    gf.theDeal(gameDeck, gameTable.dealer, gameTable.playerHands)

    gf.thePlay(gameDeck, gameTable.dealer, gameTable.playerHands)
    gf.endThePlay()

    gf.dealersPlay(gameDeck, gameTable.dealer, gameTable.playerHands)

    player.determineWinLoss(player.playerHand[1], gameTable.dealer)

    input('press enter to view hand results.')
    gf.displayHandResults(gameTable.dealer, gameTable.playerHands, player.playerHand[2], player.playerPlusMinus)
    input('press enter to continue to the next hand.')

    gameTable.clearTable()

  input('press enter to end game.')
  gf.clear_screen()
  gf.exit()

if __name__ == '__main__':
  main()
