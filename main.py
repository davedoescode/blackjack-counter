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
    print(gameTable.playerHands)
    # playerAction = gf.getPlayerAction()
    # continueGame = False
    continueGame = False
  
  input('press enter to end game.')
  gf.clear_screen()
  gf.exit()

if __name__ == '__main__':
  main()
