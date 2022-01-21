# 简答题1

from Hand import *

def print52():
    deck = Deck()
    for card in deck.cards:
        print(card)

def print13Random():
    deck = Deck()
    for i in range(13):
        print(deck.deal())

def main():
    # print52()
    print13Random()

'''略'''

if __name__ == '__main__':
    main()