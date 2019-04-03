import matplotlib.pyplot as plt
import seaborn as sns

def plotWinLoss(stats):
  handsPlayed = range(1, len(stats) + 1)
  chipDiff = []
  totalChips = []
  colors = []

  for i in range(len(stats)):
    if stats[i][0] == 0:
      chipDiffWinOrLoss = stats[i][2] - stats[i-1][2]
      colors.append('r')
    elif stats[i][0] == 1:
      chipDiffWinOrLoss = stats[i][2] - stats[i-1][2]
      colors.append('g')
    elif stats[i][0] == -1:
      chipDiffWinOrLoss = 0
      colors.append('b')

    chipDiff.append(chipDiffWinOrLoss)
    totalChips.append(stats[i][2])

  sns.set()

  plt.subplot(2, 1, 1)
  plt.plot(handsPlayed, totalChips, 'o--', color='g')
  plt.title('Blackjack Statistics', size=12)
  plt.ylabel('Chip Total', size=10)

  plt.subplot(2, 1, 2)
  plt.bar(handsPlayed, chipDiff, width=0.1, color=colors)
  plt.ylabel('Chip Differential Per Hand', size=10)
  plt.xlabel('Hands', size=10)

  plt.show()