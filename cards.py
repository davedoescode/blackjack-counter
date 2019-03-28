import random

standardDeck = [
  'Aa', 'As', 'Ah', 'Ad',
  '2a', '2s', '2h', '2d',
  '3a', '3s', '3h', '3d',
  '4a', '4s', '4h', '4d',
  '5a', '5s', '5h', '5d',
  '6a', '6s', '6h', '6d',
  '7a', '7s', '7h', '7d',
  '8a', '8s', '8h', '8d',
  '9a', '9s', '9h', '9d',
  '10a', '10s', '10h', '10d',
  'Ja', 'Js', 'Jh', 'Jd',
  'Qa', 'Qs', 'Qh', 'Qd',
  'Ka', 'Ks', 'Kh', 'Kd'
  ] * 6

class GameDeck:
  def __init__(self):
    self.deck = standardDeck

  def shuffleDeck(self):
    random.shuffle(self.deck)
    random.shuffle(self.deck)
    random.shuffle(self.deck)
    random.shuffle(self.deck)
    random.shuffle(self.deck)
    random.shuffle(self.deck)

  def dealCard(self):
    return self.deck.pop()
