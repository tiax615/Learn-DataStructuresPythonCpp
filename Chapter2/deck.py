# 第3题，扑克牌组
import random
from cardA import *

class Deck():
    def __init__(self):
        # 生成52张扑克牌实例
        self.cards = []
        for rank in range(1, 14):
            for suit in 'cdhs':
                self.cards.append(Card(rank, suit))

    def deal(self):
        # 从列表中选择一个随机位置，并“弹出”这张扑克牌
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

    def cardsLeft(self):
        # 返回牌组里剩下的牌数
        return len(self.cards)

def main():
    d = Deck()
    print(d.cardsLeft())
    print(d.deal())
    print(d.cardsLeft())

if __name__ == '__main__':
    main()