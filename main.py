import cards
import gameFunctions as gf

def main():
  gf.clear_screen()

  gameDeck = cards.GameDeck()
  gameDeck.shuffleDeck()

  game()

def game():
  continueGame = True

  while continueGame == True:
    userAction = gf.getUserAction()
    continueGame = False
  
  input('press enter to end game.')
  gf.clear_screen()
  gf.exit()

if __name__ == '__main__':
  main()
