import os
import time
import cards

def main():
  clear_screen()

  gameDeck = cards.gameDeck()
  gameDeck.shuffleDeck()

  game()

def clear_screen():
	_ = os.system("clear")

def game():
  continueGame = True

  while continueGame == True:
    userAction = getUserAction()
    continueGame = False
  
  input('press enter to end game.')
  clear_screen()
  os._exit(0)

def getUserAction():
  userPrompt = 'enter one of the following options...\n\thit (h)\n\tstay (s)\nplayer selection: '
  userAction = input(userPrompt);
  clear_screen()

  if userAction.upper() != 'H' and userAction.upper() != 'S':
    print('invalid selection, try again.')
    time.sleep(1.25)
    clear_screen()
    getUserAction()

  return userAction

if __name__ == '__main__':
  main()