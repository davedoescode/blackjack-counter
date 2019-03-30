import cards, table
import gameFunctions as gf

def main():
  gf.clear_screen()
  playGame()

def playGame():
  gameDeck = cards.GameDeck()
  gameDeck.shuffleDeck()
  gameDeck.dealerCut()

  gameTable = table.Table()
  playerPosition = gf.getPlayerPosition()
  gameTable.setPlayerPosition(playerPosition)
  gameTable.fillTablePositions()

  while gameDeck.continueGame == True:
    print(gameTable.playerHands)
    gf.theDeal(gameDeck, gameTable.dealer, gameTable.playerHands)

    gf.thePlay(gameDeck, gameTable.dealer, gameTable.playerHands)
    gf.endThePlay()

    gf.dealersPlay(gameDeck, gameTable.dealer, gameTable.playerHands)
  
    input('press enter to view hand results.')
    gf.displayHandResults(gameTable.dealer, gameTable.playerHands)
    input('press enter to continue to the next hand.')

    gameTable.clearTable()

  input('press enter to end game.')
  gf.clear_screen()
  gf.exit()

if __name__ == '__main__':
  main()
