# 第4题，21点
# 拉斯维加斯赌场里的21点具体规则是什么？：https://www.zhihu.com/question/48528692/answer/614353236
# 21点纸牌游戏：https://zhuanlan.zhihu.com/p/80693152

from deck import *

# 初始牌组，给玩家A和B各发2张牌
# 简化，无庄家。
def run_blackjack():
    deck = Deck()

    print('a get:', deck.deal())
    print('a get:', deck.deal())
    print('b get:', deck.deal())
    print('b get:', deck.deal())

    while True:
        c = input()
        if c == '1':
            print('a get:', deck.deal())
        elif c == '2':
            print('b get:', deck.deal())
        else:
            break

def main():
    while True:
        run_blackjack()

if __name__ == '__main__':
    main()