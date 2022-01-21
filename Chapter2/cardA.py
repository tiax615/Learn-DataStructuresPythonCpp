# 第2题，另一种存储方式
class Card(object):
    SUITS = 'cdhs'
    # 从小到大：梅花、方片、红桃、黑桃（桥牌）
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
        return self.index % 13 + 1

    def suitName(self):
        return self.SUIT_NAMES[self.suit()]

    def rankName(self):
        return self.RANK_NAMES[self.rank() - 1]

    def __str__(self):
        return self.rankName() + ' of ' + self.suitName()

    # 以下为3.4.2新增
    # ==
    def __eq__(self, other):
        return (self.suit() == other.suit()) and (self.rank() == other.rank())

    # <
    # 先判断花色，再判断数字
    def __lt__(self, other):
        if self.suit() == other.suit():
            a = self.rank()
            b = other.rank()
            if a < 2: a += 20
            if b < 2: b += 20
            return a < b
        else:
            return self.suit() < other.suit()

    # !=
    def __ne__(self, other):
        return not(self == other)

    # <=
    def __le__(self, other):
        return self < other or self == other