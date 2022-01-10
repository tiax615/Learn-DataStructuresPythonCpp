# 第5、6题
from deck import *

cards_list = []
canContinue = False
d = Deck()

# 比较新抽出的卡和已有的卡
def check(new_cards):
    global canContinue
    print('cardsLeft:%d, new_cards:%s, cards_list:%s' % (d.cardsLeft(), str(new_cards), str(cards_list)))
    
    count = 0
    for card in new_cards:
        if card not in cards_list:
            cards_list.append(card)
            count += 1

    if count == 2:
        canContinue = False 
        print('Fail: No same num')

def init(start_num): 
    global canContinue
    for i in range(start_num):
        rank = d.deal().rank()
        print('init get card:', rank)
        if rank not in cards_list:
            cards_list.append(rank) # 记录不重复的卡
    
    if len(cards_list) < start_num: # 如果记录的卡数量少于开始牌数，说明有重复，继续
        canContinue = True
        print('init cards_list:', cards_list)
    else:
        print('Fail: init no same')

def run_double():
    global canContinue
    if d.cardsLeft() < 2:
        canContinue = False
        print('Success: CardsLeft < 2')
    else:
        new_cards = []
        new_cards.append(d.deal().rank())
        new_cards.append(d.deal().rank())
        check(new_cards)

def main():
    global canContinue
    start_num = input()
    init(int(start_num))
    while canContinue:
        run_double()

if __name__ == '__main__':
    main()