# 第5、6题

from deck import *

def run_double(start_num):
    d = Deck()
    cards_set = {}
    cards_list = []
    for i in range(start_num):
        cards_list.append(d.deal().rank())
        
    cards_set = set(cards_list)
    print(set(cards_set))
    cards_set.append(555)

def main():
    run_double(5)

if __name__ == '__main__':
    main()