import time
import random

''' # i7-10875H，win10，python3.7.9
10000 sort use: 0.000000
100000 sort use: 0.020982
1000000 sort use: 0.262213
10000000 sort use: 4.074207
Θ(nlogn)'''

# count
def count_time(items):
    start = time.time()
    items.sort()
    stop = time.time()
    print('%d sort use: %f' % (len(items), stop - start))

def main():
    items1 = random.sample(range(1, 10000001), 10000)
    items2 = random.sample(range(1, 10000001), 100000)
    items3 = random.sample(range(1, 10000001), 1000000)
    items4 = random.sample(range(1, 10000001), 10000000)

    itemsList = [items1, items2, items3, items4]
    for items in itemsList:
        count_time(items)

if __name__ == '__main__':
    main()