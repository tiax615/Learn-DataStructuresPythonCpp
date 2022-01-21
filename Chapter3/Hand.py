import sys

sys.path.insert(0, '../Chapter2')
from cardA import *
from deck import *

class Hand:
    '''A labeled collection of cards that can be sorted.'''

    def __init__(self, label=''):
        '''Create an empty collection with the given label.'''
        self.label = label
        self.cards = []

    def add(self, card):
        '''Add card to the hand.'''
        self.cards.append(card)

    def sortSelect(self):
        '''Arrange the cards in descending bridge order.'''
        # 使用两个列表，进行选择排序
        cards0 = self.cards
        cards1 = []
        while cards0 != []:
            next_card = max(cards0)
            cards0.remove(next_card)
            cards1.append(next_card)
        self.cards = cards1

    def sort(self):
        self.cards.sort()
        self.cards.reverse()

    def dump(self):
        '''Print out contents of the Hand.'''
        print(self.label + "'s Cards:")
        for c in self.cards:
            print (' ', c)

def main():
    # h = Hand('North')
    # h.add(Card(5, 'c'))
    # h.add(Card(10, 'd'))
    # h.add(Card(13, 's'))
    # h.dump()

    print(Card(1, 'c') < Card(6, 'd'))

if __name__ == '__main__':
    main()