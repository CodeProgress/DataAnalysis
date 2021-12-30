import random

class BJDeck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.deck = self.build_deck()
        self.shuffle()

    def build_deck(self):
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        if self.num_decks > 1:
            deck = deck * self.num_decks
        assert len(deck) == self.num_decks * 52
        return deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if self.deck:
            return self.deck.pop()
        return None

class BlackJack:
    def __init__(self, deck):
        self.deck = deck

    def play_round(self):
        pass
        # deal to player and dealer
        # player plays until completion
        # dealer plays until completion
        # compare
        # choose winner
        # update strategy grid

    def hit(self):
        pass

    def double(self):
        pass

    def stand(self):
        pass

    def split(self):
        pass

bjd = BJDeck(2)
print(bjd.deck)

# Goal: build strategy grid using Monte Carlo simulated roll-outs.
# Below example grid adapted from https://github.com/kensingtoine/blackjack/blob/master/basic-strategy.txt
# Also see: https://en.wikipedia.org/wiki/Blackjack#Blackjack_strategy

# -	    2	3	4	5	6	7	8	9	T	A
# 5-8	H	H	H	H	H	H	H	H	H	H
# 9	    H	D	D	D	D	H	H	H	H	H
# 10	D	D	D	D	D	D	D	D	H	H
# 11	D	D	D	D	D	D	D	D	D	H
# 12	H	H	S	S	S	H	H	H	H	H
# 13	S	S	S	S	S	H	H	H	H	H
# 14	S	S	S	S	S	H	H	H	H	H
# 15	S	S	S	S	S	H	H	H	H	H
# 16	S	S	S	S	S	H	H	H	H	H
# 17+	S	S	S	S	S	S	S	S	S	S
# A-2	H	H	H	D	D	H	H	H	H	H
# A-3	H	H	H	D	D	H	H	H	H	H
# A-4	H	H	D	D	D	H	H	H	H	H
# A-5	H	H	D	D	D	H	H	H	H	H
# A-6	H	D	D	D	D	H	H	H	H	H
# A-7	S	D	D	D	D	S	S	H	H	H
# A-8+  S	S	S	S	S	S	S	S	S	S
# A-A	P	P	P	P	P	P	P	P	P	P
# 2-2	P	P	P	P	P	P	H	H	H	H
# 3-3	P	P	P	P	P	P	H	H	H	H
# 4-4	H	H	H	P	P	H	H	H	H	H
# 5-5	D	D	D	D	D	D	D	D	H	H
# 6-6	P	P	P	P	P	H	H	H	H	H
# 7-7	P	P	P	P	P	P	H	H	H	H
# 8-8	P	P	P	P	P	P	P	P	P	P
# 9-9	P	P	P	P	P	S	P	P	S	S
# T-T	S	S	S	S	S	S	S	S	S	S
#
# H = Hit
# D = Double
# S = Stand
# P = Split
