import time, os

def initialDeal(cardDeck):
  pass

def dealCard(cardDeck):
  pass

def getPlayerPosition():
  clear_screen()
  playerPrompt = 'what seat in the range [1, 6] do you want to play at: '
  playerPosition = input(playerPrompt)
  try:
    playerPosition = int(playerPosition) - 1
  except:
    print('invalid postion selection, try again ...')
    time.sleep(1.25)
    clear_screen()
    getPlayerPosition()

  if playerPosition >= 0 and playerPosition <= 5:
    return playerPosition
  else:
    clear_screen()
    print('invalid postion selection, try again ...')
    time.sleep(1.25)
    clear_screen()
    getPlayerPosition()

def getPlayerAction():
  clear_screen()
  playerPrompt = 'enter one of the following options...\n\thit (h)\n\tstay (s)\nplayer selection: '
  playerAction = input(playerPrompt)
  clear_screen()

  if playerAction.upper() != 'H' and playerAction.upper() != 'S':
    print('invalid selection, try again.')
    time.sleep(1.25)
    clear_screen()
    getPlayerAction()

  return playerAction

def clear_screen():
	_ = os.system("clear")

def exit():
  os._exit(0)
