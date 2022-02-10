from ListNode import ListNode

class LListCursor:
    def __init__(self, llist):
        self.lst = llist
        
        # create a dummy node at the front of the list
        self.header = ListNode("**DUMMY HEADER NODE**", llist.head)

        # point prev to just before the first actual ListNode
        self.prev = self.header

    def done(self):
        return self.prev.link is None

    def getItem(self):
        return self.prev.link.item

    def advance(self):
        self.prev = self.prev.link

    def deleteItem(self):
        self.prev.link = self.prev.link.link

        # first listnode may have changed, update list head
        self.lst.head = self.header.link

    def replaceItem(self, value):
        self.prev.link.item = value