#monte carlo simulation of "Likelihood That the Better Team Wins the Series"

import random
import pylab

def plot_world_series(numGames, lowerWinPercentage = .40):    
    wPercentages = []
    for games in range(1,numGames):
        team1seriesWins = 0
        team2seriesWins = 0
        trials = 100
        for i in xrange(trials):
            team1wins = 0
            team2wins = 0
            
            for i in range(games):
                if random.random() < lowerWinPercentage:
                    team2wins += 1
                else:
                    team1wins += 1
            
            if team1wins > team2wins:
                team1seriesWins += 1
            else:
                team2seriesWins += 1
        
        wPercentages.append(team1seriesWins/float(trials))
    pylab.plot(wPercentages)
    pylab.xlabel("Number of Games in Series")
    pylab.ylabel("Likelihood That the Better Team Wins the Series")
    pylab.show()

plot_world_series(100)
