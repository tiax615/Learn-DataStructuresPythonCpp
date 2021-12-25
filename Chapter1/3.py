import time
import random

''' # i7-10875H，win10，python3.7.9
10000 sort use: 2.134704
100000 sort use: 217.639438
Θ(n^2) '''

# selection sort
def selection_sort(items):
    indexStart = 0
    indexStop = len(items)
    
    while indexStart < indexStop:
        index = indexStart
        minIndex = indexStart

        while index < indexStop:
            if (items[index] < items[minIndex]):
                minIndex = index
            index += 1
        
        temp = items[indexStart]
        items[indexStart] = items[minIndex]
        items[minIndex] = temp
        indexStart += 1

    return items

# selection sort pythonic
def selection_sort_pythonic(items):
    for i in range(len(items)):
        minIndex = i
        for j in range(i + 1, len(items)):
            if items[j] < items[minIndex]:
                minIndex = j
        items[i], items[minIndex] = items[minIndex], items[i]
    return items

# count
def count_time(items):
    start = time.time()
    # selection_sort(items)
    selection_sort_pythonic(items)
    stop = time.time()
    print('%d sort use: %f' % (len(items), stop - start))

def main():
    items0 = random.sample(range(1, 20), 10)
    print(selection_sort_pythonic(items0))

    items1 = random.sample(range(1, 10000001), 10000)
    items2 = random.sample(range(1, 10000001), 100000)
    items3 = random.sample(range(1, 10000001), 1000000)
    items4 = random.sample(range(1, 10000001), 10000000)

    itemsList = [items1, items2, items3, items4]
    for items in itemsList:
        count_time(items)

if __name__ == '__main__':
    main()