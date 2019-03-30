import time, os

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
  clear_screen()
  dealerCards = ''
  for card in dealer:
    if dealer.index(card) == (len(dealer)-1):
      dealerCards += card
    else:
      dealerCards += (card + ', ')

  print('---------------')
  print('Dealer:\n' + dealerCards + '\n--> ' + countPlayerTotal(dealer) + ' <--')
  print('---------------')

  for player in players:
    print(player[0] + ':')
    playerCards = ''
    for card in player[1]:
      if player[1].index(card) == (len(player[1])-1):
        playerCards += (card)
      else:
        playerCards += (card + ', ')
    print(playerCards)
    print('--> ' + countPlayerTotal(player[1]) + ' <--')
    print('---------------')

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
  
  if cardTotal > 21:
    return 'BUST'
  else:
    return str(cardTotal)

def getPlayerAction():
  playerPrompt = 'enter one of the following options...\n\thit (a)\n\tstay (s)\nplayer selection: '
  playerAction = input(playerPrompt)
  clear_screen()

  if playerAction.upper() != 'A' and playerAction.upper() != 'S':
    print('invalid selection, try again.')
    time.sleep(1.25)
    clear_screen()
    getPlayerAction()

  return playerAction

def dealFirstHand(cards, dealer, players):
  for player in players:
    player[1].append(cards.dealCard())
  
  dealer.append(cards.dealCard())

  for player in players:
    player[1].append(cards.dealCard())

def hitAction(cards, playerHand):
  playerHand.append(cards.dealCard())

def basicNpcLogic(cards, playerHand):
  if countPlayerTotal(playerHand) == 'BUST':
    return False
  elif int(countPlayerTotal(playerHand)) >= 17:
    return False
  else:
    playerHand.append(cards.dealCard())
    return True

def theDeal(deck, dealer, players):
  dealFirstHand(deck, dealer, players)
  displayTable(dealer, players)

def thePlay(deck, dealer, players):
  for player in players:
    if player[0] == 'PLAYER':

      isPlayersTurn = True
      while isPlayersTurn:

        playerCount = countPlayerTotal(player[1])
        if playerCount == 'BUST':
          isPlayersTurn = False
          break

        playerAction = getPlayerAction()
        if playerAction.upper() == 'A':
          hitAction(deck, player[1])
        elif playerAction.upper() == 'S':
          isPlayersTurn = False
        displayTable(dealer, players)

    else:
      isPlayersTurn = True

      while isPlayersTurn:
        isPlayersTurn = basicNpcLogic(deck, player[1])
      displayTable(dealer, players)

  displayTable(dealer, players)

def dealersPlay(deck, dealer, players):
  clear_screen()

  isDealersTurn = True
  while isDealersTurn:
    isDealersTurn = basicNpcLogic(deck, dealer)

  displayTable(dealer, players)

def displayHandResults(dealer, players):
  clear_screen()
  results = determineResults(dealer, players)
  
  i = 0
  for player in players:
    if player[0] == 'PLAYER':
      print('--------------------')
      if results[i] == 0:
        print(str(i + 1) + ') ' + player[0] + '--> LOSS')
        i += 1
      elif results[i] == 1:
        print(str(i + 1) + ') ' + player[0] + '--> WIN')
        i += 1
      elif results[i] == 2:
        print(str(i + 1) + ') ' + player[0] + '--> PUSH')
        i += 1
      print('--------------------')
    else:
      if results[i] == 0:
        print(str(i + 1) + ') ' + player[0] + '--> LOSS')
        i += 1
      elif results[i] == 1:
        print(str(i + 1) + ') ' + player[0] + '--> WIN')
        i += 1
      elif results[i] == 2:
        print(str(i + 1) + ') ' + player[0] + '--> PUSH')
        i += 1

def endThePlay():
  inputString = 'press enter to end the play, and begin the dealers play.'
  input(inputString)

def determineResults(dealer, players):
  dealerScore = int(countPlayerTotal(dealer))
  if dealerScore == 'BUST':
    dealerScore = 0
  else: 
    dealerScore = int(dealerScore)
  playerScores = []
  results = []

  for player in players:
    playerScores.append(countPlayerTotal(player[1]))

  for score in playerScores:
    if score == 'BUST':
      results.append(0)
    elif int(score) < dealerScore:
      results.append(0)
    elif int(score) > dealerScore:
      results.append(1)
    elif int(score) == dealerScore:
      results.append(2)

  return results

def clear_screen():
	_ = os.system("clear")

def exit():
  os._exit(0)
