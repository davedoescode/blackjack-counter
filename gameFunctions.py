import time, os

def initialDeal(cardDeck):
  pass

def dealCard(cardDeck):
  pass

def getUserAction():
  userPrompt = 'enter one of the following options...\n\thit (h)\n\tstay (s)\nplayer selection: '
  userAction = input(userPrompt)
  clear_screen()

  if userAction.upper() != 'H' and userAction.upper() != 'S':
    print('invalid selection, try again.')
    time.sleep(1.25)
    clear_screen()
    getUserAction()

  return userAction

def clear_screen():
	_ = os.system("clear")

def exit():
  os._exit()
