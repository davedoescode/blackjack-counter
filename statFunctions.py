import matplotlib.pyplot as plt

def plotWinLoss(stats):
  handsPlayed = range(1, len(stats) + 1)
  chipDiff = []
  totalChips = []

  for i in range(len(stats)):
    if stats[i][0] == 0:
      chipDiffWinOrLoss = stats[i][2] - stats[i-1][2]
    elif stats[i][0] == 1:
      chipDiffWinOrLoss = stats[i][2] - stats[i-1][2]
    elif stats[i][0] == -1:
      chipDiffWinOrLoss = 0

    chipDiff.append(chipDiffWinOrLoss)
    totalChips.append(stats[i][2])

  plt.subplot(2, 1, 1)
  plt.plot(handsPlayed, totalChips, 'o-', color='green')
  plt.title('Blackjack Statistics')
  plt.ylabel('Chip Total')

  plt.subplot(2, 1, 2)
  plt.bar(handsPlayed, chipDiff, width=0.1, align='center', color='green')

  plt.show()