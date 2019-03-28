import time, os

def initialDeal(cardDeck):
  pass

def dealCard(cardDeck):
  pass

def getPlayerPosition():
  clear_screen()
  playerPrompt = 'what seat in the range [1, 6] do you want to play at: '

  try:
    playerPosition = int(input(playerPrompt)) - 1
  except:
    print('invalid postion selection, try again ...')
    time.sleep(1.25)
    clear_screen()
    getPlayerPosition()

  if playerPosition >= 0 and playerPosition <= 5:
    clear_screen()
    return playerPosition
  else:
    clear_screen()
    print('invalid postion selection, try again ...')
    time.sleep(1.25)
    clear_screen()
    getPlayerPosition()

def displayTable(dealer, players):
  dealerCards = ''
  for card in dealer:
    if dealer.index(card) == (len(dealer)-1):
      dealerCards += card
    else:
      dealerCards += (card + ', ')

  print('\t\t\t\t\tDealer\n\t\t\t\t\t' + dealerCards + '\n\t\t\t\t\t' + countPlayerTotal(dealer) + '\n')

  playerTitles = ''
  playerHands = ''
  playersCardTotal = ''
  for player in players:
    playerTitles += (player[0] + '\t\t')
    playerCards = ''
    for card in player[1]:
      if player[1].index(card) == (len(player[1])-1):
        playerCards += (card + '\t\t')
      else:
        playerCards += (card + ', ')

    playerHands += (playerCards)

    playerCardTotal = countPlayerTotal(player[1])
    playersCardTotal += (countPlayerTotal(player[1]) + '\t\t')
  
  print(playerTitles)
  print(playerHands)
  print(playersCardTotal + '\n')

def countPlayerTotal(playerHand):
  #TODO: IMPROVE LOGIC IF THE CARD IS AN ACE, MAY BE IN A DIFFERENT FUNCTION
  cardTotal = 0
  for card in playerHand:
    if card[0] in ['J', 'Q', 'K'] or len(card) == 3:
      cardTotal += 10

    elif card[0] == 'A':
      if (cardTotal + 11) > 21:
        cardTotal += 1

      else:
        cardTotal += 11

    else:
      cardTotal += int(card[0])
  
  return str(cardTotal)

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

def dealFirstHand(cards, dealer, players):
  for player in players:
    player[1].append(cards.pop())
  
  dealer.append(cards.pop())

  for player in players:
    player[1].append(cards.pop())

def clear_screen():
	_ = os.system("clear")

def exit():
  os._exit(0)
