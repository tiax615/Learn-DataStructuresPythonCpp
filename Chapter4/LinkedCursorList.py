from LList import LList
from LListCursor import LListCursor

class LinkedCursorList(LList):
    def getCursor(self):
        return LListCursor(self)

def censor(wordList, forbiddenWords):
    cursor = wordList.getCursor()
    while not cursor.done():
        if cursor.getItem() in forbiddenWords:
            # cursor.deleteItem()
            cursor.replaceItem('**')
            cursor.advance()
        else:
            cursor.advance()

def main():
    words = LinkedCursorList("kaige is sb".split())
    for item in words:
        print(item)
    censor(words, ['sb', 'hentai'])
    for item in words:
        print(item)

if __name__ == '__main__':
    main()