import cards, table
import gameFunctions as gf

def main():
  gf.clear_screen()
  playGame()

def playGame():
  continueGame = True

  gameTable = table.Table()
  playerPosition = gf.getPlayerPosition()
  gameTable.setPlayerPosition(playerPosition)
  gameTable.fillTablePositions()
  
  gameDeck = cards.GameDeck()
  gameDeck.shuffleDeck()

  while continueGame == True:
    gf.theDeal(gameDeck.deck, gameTable.dealer, gameTable.playerHands)
    gf.thePlay(gameDeck.deck, gameTable.dealer, gameTable.playerHands)
    gf.endThePlay()
    gf.dealersPlay(gameDeck.deck, gameTable.dealer, gameTable.playerHands)
    continueGame = False
  
  input('press enter to view hand results.')
  gf.displayHandResults(gameTable.dealer, gameTable.playerHands)
  input('press enter to end game.')
  gameTable.clearTable()
  gameDeck.resetDeck()
  gf.clear_screen()
  gf.exit()

if __name__ == '__main__':
  main()
