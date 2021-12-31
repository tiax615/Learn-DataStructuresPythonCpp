# 第2题，另一种存储方式
class Card(object):
    SUITS = 'cdhs'
    SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = range(1, 14)
    RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine', 'Ten',
                  'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):
        # index in range(0,52)
        self.index = self.RANKS.index(rank) + 13 * self.SUITS.index(suit)

    def suit(self):
        return self.index // 13

    def rank(self):
        return self.index % 13

    def suitName(self):
        return self.SUIT_NAMES[self.suit()]

    def rankName(self):
        return self.RANK_NAMES[self.rank()]

    def __str__(self):
        return self.rankName() + ' of ' + self.suitName()