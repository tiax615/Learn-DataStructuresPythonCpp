import time

''' # i7-10875H，win10，python3.7.9
search1 found 0 use: 0.000000
search1 found 999999 use: 0.011968
search2 found 0 use: 0.000000
search2 found 999999 use: 0.033910
search3 found 499999 use: 0.000000
search3 found 0 use: 0.000000 '''

# index
def search1(items, target):
    return items.index(target)

# for
def search2(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i

# binary search
def search3(items, target):
    low = 0;
    high = len(items) - 1
    # i = 0
    while low <= high:
        # i += 1
        mid = (low + high) // 2
        item = items[mid]
        if item == target:
            # print(i)
            return mid
        elif target < item:
            high = mid - 1
        else:
            low = mid + 1

# count
def count_time(func, items, target):
    start = time.time()
    res = func(items, target)
    stop = time.time()
    print('%s found %d use: %f' % (func.__name__, res, stop - start))

def main():
    items = list(range(1000000))

    count_time(search1, items, 0)
    count_time(search1, items, 999999)
    count_time(search2, items, 0)
    count_time(search2, items, 999999)
    count_time(search3, items, 499999)
    count_time(search3, items, 0)

if __name__ == '__main__':
    main()