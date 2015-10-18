# Simpson's paradox

import random

class Player(object):
    def __init__(self, numerFloor=2, denomLimit=100):
        self.numerFloor = numerFloor
        self.denomLimit = denomLimit
        self.numers = []
        self.denoms = []
    
    def add_instance(self, numer, denom):
        self.numers.append(numer)
        self.denoms.append(denom)
    
    def add_random_instance(self):
        '''
        adds a random numerator and denominator
        where floor <= numerator <= limit
        and numerator <= denominator <= limit
        '''
        numer = random.randint(self.numerFloor, self.denomLimit)
        denom = random.randint(numer, self.denomLimit)
        self.add_instance(numer, denom)
    
    def add_random_instances(self, numInstances):
        for i in range(numInstances):
            self.add_random_instance()
    
    def get_num_instances(self):
        assert len(self.numers) == len(self.denoms)
        return len(self.numers)
    
    def get_instance(self, index):
        return (self.numers[index], self.denoms[index])
    
    def get_combined_totals(self):
        return (sum(self.numers), sum(self.denoms))
    
    def get_instance_percentage(self, index):
        return float(self.numers[index])/float(self.denoms[index])
  
    def get_combined_percentage(self):
        return float(sum(self.numers))/float(sum(self.denoms))

    def print_stats(self):
        output = "Instances: "
        fractions = zip(self.numers, self.denoms)
        for i, frac in enumerate(fractions):
            output += "{:>3}/{:<3} \t {:.13f} \t".format(frac[0], frac[1], self.get_instance_percentage(i))
        
        combined = self.get_combined_totals()
        output += "Combined: {:>3}/{:<3} \t {}".format(combined[0], combined[1], self.get_combined_percentage())
                
        print output
        
class SimpsonsParadox(object):
    def __init__(self, players = []):
        self.players = players
    
    def add_player(self, Player):
        self.players.append(Player)  
    
    def print_stats(self):
        for player in self.players:
            player.print_stats()
        print '-------------------'
    
    def check_for_existence_of_paradox_between_two_players(self, printStats = False):
        assert len(self.players) == 2

        p1 = self.players[0]
        p2 = self.players[1]
        
        assert p1.get_num_instances() == p2.get_num_instances()
        
        numInstances = p1.get_num_instances()

        doesLowerPlayerExist = False
        
        for i in range(numInstances):
            p1Percentage = p1.get_instance_percentage(i) 
            p2Percentage = p2.get_instance_percentage(i)
            
            if p1Percentage == p2Percentage:
                continue
            
            doesLowerPlayerExist = True
            
            if p1Percentage < p2Percentage:
                lowerPlayer = p1
                higherPlayer = p2
            else:
                lowerPlayer = p2
                higherPlayer = p1
        
        if not doesLowerPlayerExist:
            return False
        
        for i in range(numInstances):
            if lowerPlayer.get_instance_percentage(i) > higherPlayer.get_instance_percentage(i):
                return False
        
        if lowerPlayer.get_combined_percentage() < higherPlayer.get_combined_percentage():
            return False
        
        if printStats:
            self.print_stats()
    
        return True        

numTrials = 2000
count = 0
numPlayers = 2
numInstances = 2

for trial in xrange(numTrials):
    players = [Player() for p in range(numPlayers)]
    for player in players:
        player.add_random_instances(numInstances)
    
    simpsonsParadox = SimpsonsParadox(players)
    
    if simpsonsParadox.check_for_existence_of_paradox_between_two_players(True):
        count += 1

print count, numTrials, float(count)/numTrials


