myList = [1,2,3]

items = iter(myList)
while True:
    try:
        item = next(items)
    except StopIteration:
        break
    print(item)