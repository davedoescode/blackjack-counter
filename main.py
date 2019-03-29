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
    theDeal(gameDeck.deck, gameTable.dealer, gameTable.playerHands)
    thePlay(gameDeck.deck, gameTable.dealer, gameTable.playerHands)
    gf.endThePlay()
    dealersPlay(gameDeck.deck, gameTable.dealer, gameTable.playerHands)
    continueGame = False
  
  input('press enter to end game.')
  gf.clear_screen()
  gf.exit()

def theDeal(deck, dealer, players):
  gf.dealFirstHand(deck, dealer, players)
  gf.displayTable(dealer, players)

def thePlay(deck, dealer, players):
  for player in players:
    if player[0] == '[ PLAYER ]':

      isPlayersTurn = True
      while isPlayersTurn:

        playerCount = gf.countPlayerTotal(player[1])
        if playerCount == 'BUST':
          isPlayersTurn = False
          break

        playerAction = gf.getPlayerAction()
        if playerAction.upper() == 'H':
          gf.hitAction(deck, player[1])
        elif playerAction.upper() == 'S':
          isPlayersTurn = False
        gf.displayTable(dealer, players)

    else:
      isPlayersTurn = True

      while isPlayersTurn:
        isPlayersTurn = gf.basicNpcLogic(deck, player[1])
      gf.displayTable(dealer, players)

  gf.displayTable(dealer, players)

def dealersPlay(deck, dealer, players):
  gf.clear_screen()

  isDealersTurn = True
  while isDealersTurn:
    isDealersTurn = gf.basicNpcLogic(deck, dealer)

  gf.displayTable(dealer, players)

if __name__ == '__main__':
  main()
