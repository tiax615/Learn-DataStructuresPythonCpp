import time
import random

''' # i7-10875H，win10，python3.7.9
3 sort use: 0.000000
28 sort use: 0.000000
260 sort use: 0.000000
2660 sort use: 0.000997
26337 sort use: 0.012965
264136 sort use: 0.187181
2642043 sort use: 2.099580
Θ(n) '''

# squeeze
# pre: 传入有序列表，元素是整数
# post: 找出重复项
def squeeze(items):
    res = []
    squeeze = None
    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            if squeeze == items[i]:
                continue
            else:
                squeeze = items[i]
                res.append(squeeze)
    items.clear()
    items.extend(res)

# count
def count_time(items):
    start = time.time()
    squeeze(items)
    stop = time.time()
    print('%d sort use: %f' % (len(items), stop - start))

def main():
    # items0 = [1,3,3,3,5,5,5,7,7,8,8,8,8,9,9,9,10,10,11,12,15,16,17,17]
    # squeeze(items0)
    # print(items0)

    # items1 = random.choices(range(10), k=10)
    # items1.sort()
    # print(items1)
    # squeeze(items1)
    # print(items1)

    items1 = random.choices(range(10), k=10)
    items2 = random.choices(range(100), k=100)
    items3 = random.choices(range(1000), k=1000)
    items4 = random.choices(range(10000), k=10000)
    items5 = random.choices(range(100000), k=100000)
    items6 = random.choices(range(1000000), k=1000000)
    items7 = random.choices(range(10000000), k=10000000)

    itemsList = [items1, items2, items3, items4, items5, items6, items7]
    for items in itemsList:
        items.sort()
        count_time(items)

if __name__ == '__main__':
    main()