from ListNode import ListNode

class LListIterator:
    def __init__(self, head):
        self.currnode = head
    
    # def next(self):
    def __next__(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

class LList:
    def __init__(self, seq=()):
        self.head = None
        self.size = 0

        # # if passed a sequence, place items in the list
        # for x in seq:
        #     self.append(x)

        if seq == ():
            self.head = None
        else:
            self.head = ListNode(seq[0], None)
            last = self.head
            for item in seq[1:]:
                last.link = ListNode(item, None)
                last = last.link
        self.size = len(seq)

    def __len__(self):
        return self.size

    def _find(self, position):
        assert 0 <= position < self.size
        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
            return node

    def append(self, x):
        newNode = ListNode(x)

        if self.head is not None:
            node = self._find(self.size - 1)
            node.link = newNode
        else:
            self.head = newNode
        self.size += 1

    def __getitem__(self, position):
        node = self._find(position)
        return node.item

    def __setitem__(self, position, value):
        node = self._find(position)
        node.item = value

    def _delete(self, position):
        if position == 0:
            item = self.head.item
            self.head = self.head.link
        else:
            prev_node = self._find(position - 1)
            item = prev_node.link.item
            prev_node.link = prev_node.link.link

        self.size -= 1
        return item

    def __delitem__(self, position):
        assert 0 <= position < self.size
        self._delete(position)

    def pop(self, i=None):
        assert self.size > 0 and (i is None or (0 <= i < self.size))

        if i is None:
            i = self.size - 1
        return self._delete(i)

    def insert(self, i, x):
        assert 0 <= i <= self.size

        if i == 0:
            self.head = ListNode(x, self.head)
        else:
            prev = self._find(i - 1)
            prev.link = ListNode(x, prev.link)
        self.size += 1

    def __copy__(self):
        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    # def __iter__(self):
    #     return LListIterator(self.head)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.item
            node = node.link

def main():
    nums = LList([1,2,3,4])
    for item in nums:
        print(item)

if __name__ == '__main__':
    main()